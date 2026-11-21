#!/usr/bin/env python3
"""Kiểm tra và đóng gói các skill trong skills/ cho nhiều nền tảng.

Chỉ dùng thư viện chuẩn Python 3.8+.

    python3 scripts/build_skills.py          # kiểm tra + build vào dist/, cập nhật skills.json, index.html, marketplace
    python3 scripts/build_skills.py --check  # chỉ kiểm tra hợp lệ (trả mã lỗi 1 nếu có lỗi)
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"
REPO_SLUG = "chaunnt/ZworldAdventure_Skills"
MARKETPLACE_NAME = "zworld-skills"

ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TEXT_EXT = {".md", ".txt", ".html", ".htm", ".json", ".csv", ".py", ".sh", ".js", ".css", ".yaml", ".yml", ".xml", ".svg"}
ZIP_DATE = (2025, 1, 1, 0, 0, 0)


# ---------------------------------------------------------------- frontmatter
def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Đọc frontmatter YAML đơn giản (khoá: giá trị, một cấp lồng, chuỗi gấp >-)."""
    if not text.startswith("---"):
        raise ValueError("SKILL.md phải bắt đầu bằng frontmatter '---'")
    end = text.find("\n---", 3)
    if end < 0:
        raise ValueError("Thiếu dòng '---' đóng frontmatter")
    block, body = text[3:end].strip("\n"), text[end + 4:].lstrip("\n")
    data: dict = {}
    parent = None
    folding_key = None
    for raw in block.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        line = raw.strip()
        if folding_key and indent > 0:
            target = data[parent] if parent and isinstance(data.get(parent), dict) and folding_key in data[parent] else data
            target[folding_key] = (target[folding_key] + " " + line).strip()
            continue
        folding_key = None
        key, _, value = line.partition(":")
        key, value = key.strip(), _strip_comment(value.strip())
        if indent == 0:
            if value in ("", ">", ">-", "|", "|-"):
                if value == "":
                    data[key] = {}
                    parent = key
                else:
                    data[key] = ""
                    folding_key, parent = key, None
            else:
                data[key] = _unquote(value)
                parent = None
        elif parent is not None:
            data[parent][key] = _unquote(value)
    return data, body


def _strip_comment(v: str) -> str:
    if v.startswith(("'", '"')):
        return v
    return re.sub(r"\s+#.*$", "", v)


def _unquote(v: str) -> str:
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        return v[1:-1]
    return v


def validate(skill_dir: Path) -> tuple[dict, str, list[str]]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return {}, "", [f"{skill_dir.name}: thiếu SKILL.md"]
    try:
        meta, body = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    except ValueError as e:
        return {}, "", [f"{skill_dir.name}: {e}"]
    name = meta.get("name", "")
    desc = meta.get("description", "")
    if not NAME_RE.match(name) or len(name) > 64:
        errors.append(f"{skill_dir.name}: 'name' phải là chữ thường/số/gạch nối, ≤ 64 ký tự")
    if name != skill_dir.name:
        errors.append(f"{skill_dir.name}: 'name' ({name}) phải trùng tên thư mục")
    if not desc:
        errors.append(f"{skill_dir.name}: thiếu 'description'")
    elif len(desc) > 1024:
        errors.append(f"{skill_dir.name}: 'description' dài {len(desc)} > 1024 ký tự")
    if "<" in desc or ">" in desc:
        errors.append(f"{skill_dir.name}: 'description' không được chứa < hoặc >")
    extra = set(meta) - ALLOWED_KEYS
    if extra:
        errors.append(f"{skill_dir.name}: khoá frontmatter không hỗ trợ: {', '.join(sorted(extra))}")
    lines = body.count("\n")
    if lines > 500:
        print(f"  ! {skill_dir.name}: SKILL.md có {lines} dòng (> 500), nên chuyển bớt sang references/")
    for ref in re.findall(r"`((?:references|assets|scripts)/[\w./-]+\.\w+)`", body):
        if not (skill_dir / ref).exists() and not (ROOT / ref).exists():
            print(f"  ! {skill_dir.name}: SKILL.md nhắc tới tệp không tồn tại: {ref}")
    return meta, body, errors


# ---------------------------------------------------------------- html → text
class HtmlToText(HTMLParser):
    BLOCK = {"p", "div", "section", "header", "footer", "main", "article", "nav", "ul", "ol", "dl", "table", "tr", "br", "figure", "figcaption"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.skip = 0
        self.pre = 0
        self.json_block = False
        self.list_stack: list[list] = []
        self.cells: list[str] | None = None
        self.cell_buf: list[str] | None = None
        self.img_depth = 0  # >0: đang ở trong phần tử role="img" (đã in aria-label, bỏ phần vẽ)

    def _emit(self, s: str) -> None:
        (self.cell_buf if self.cell_buf is not None else self.out).append(s)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.img_depth:
            if tag not in ("br", "img", "hr", "meta", "input"):
                self.img_depth += 1
            return
        if a.get("role") == "img":
            self.out.append(f"\n[Hình: {a.get('aria-label', '')}]\n")
            self.img_depth = 1
            return
        if tag in ("style", "noscript"):
            self.skip += 1
        elif tag == "script":
            if a.get("type") == "application/json":
                self.json_block = True
                self.out.append("\n```json\n")
            else:
                self.skip += 1
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "pre":
            self.pre += 1
            self.out.append("\n```\n")
        elif tag in ("ul", "ol"):
            self.list_stack.append([tag, 0])
        elif tag == "li":
            depth = max(len(self.list_stack) - 1, 0)
            if self.list_stack and self.list_stack[-1][0] == "ol":
                self.list_stack[-1][1] += 1
                bullet = f"{self.list_stack[-1][1]}."
            else:
                bullet = "-"
            self.out.append("\n" + "  " * depth + bullet + " ")
        elif tag == "table":
            self.table_rows = 0
        elif tag == "tr":
            self.cells = []
        elif tag in ("td", "th"):
            self.cell_buf = []
        elif tag == "dt":
            self.out.append("\n- **")
        elif tag == "dd":
            self.out.append(": ")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "code" and not self.pre:
            self._emit("`")
        elif tag in self.BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if self.img_depth:
            self.img_depth -= 1
            return
        if tag in ("style", "noscript"):
            self.skip = max(self.skip - 1, 0)
        elif tag == "script":
            if self.json_block:
                self.json_block = False
                self.out.append("\n```\n")
            else:
                self.skip = max(self.skip - 1, 0)
        elif tag == "pre":
            self.pre = max(self.pre - 1, 0)
            self.out.append("\n```\n")
        elif tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
            self.out.append("\n")
        elif tag in ("td", "th") and self.cell_buf is not None and self.cells is not None:
            self.cells.append(re.sub(r"\s+", " ", "".join(self.cell_buf)).strip())
            self.cell_buf = None
        elif tag == "tr" and self.cells is not None:
            self.out.append("\n| " + " | ".join(self.cells) + " |")
            self.table_rows = getattr(self, "table_rows", 0) + 1
            if self.table_rows == 1:
                self.out.append("\n|" + "---|" * len(self.cells))
            self.cells = None
        elif tag == "dt":
            self.out.append("**")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "code" and not self.pre:
            self._emit("`")
        elif tag in self.BLOCK or tag.startswith("h") and tag[1:].isdigit():
            self.out.append("\n")

    def handle_data(self, data):
        if self.skip or self.img_depth:
            return
        if self.pre or self.json_block:
            self.out.append(data)
        else:
            self._emit(re.sub(r"\s+", " ", data))

    def text(self) -> str:
        t = "".join(self.out)
        t = re.sub(r"[ \t]+\n", "\n", t)
        t = re.sub(r"\n[ \t]+(?=[^\s\-0-9|])", "\n", t)
        return re.sub(r"\n{3,}", "\n\n", t).strip()


def html_to_text(src: str) -> str:
    p = HtmlToText()
    p.feed(src)
    return p.text()


# ---------------------------------------------------------------- build
def skill_files(skill_dir: Path) -> list[Path]:
    return sorted(p for p in skill_dir.rglob("*") if p.is_file() and not p.name.startswith("."))


def build_zip(skill_dir: Path, out: Path) -> None:
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in skill_files(skill_dir):
            info = zipfile.ZipInfo(f"{skill_dir.name}/{f.relative_to(skill_dir).as_posix()}", ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, f.read_bytes())


def build_prompt(skill_dir: Path, meta: dict, body: str) -> str:
    name = meta["name"]
    parts = [
        f"# SKILL: {name}",
        "",
        "> Tệp này gộp toàn bộ skill thành một tài liệu duy nhất để dùng với ChatGPT, Gemini hoặc model bất kỳ.",
        "> Hãy làm theo phần HƯỚNG DẪN CHÍNH; các phần TÀI LIỆU KÈM THEO là tài liệu tra cứu được nhắc tới trong hướng dẫn.",
        f"> Nguồn: https://github.com/{REPO_SLUG}/tree/main/skills/{name}",
        "",
        f"**Mô tả / khi nào dùng:** {meta.get('description', '')}",
        "",
        "---",
        "",
        "## HƯỚNG DẪN CHÍNH (SKILL.md)",
        "",
        body.strip(),
    ]
    order = {"references": 0, "assets": 1, "scripts": 2}
    for f in sorted(skill_files(skill_dir), key=lambda f: (order.get(f.relative_to(skill_dir).parts[0], 3), f.as_posix())):
        rel = f.relative_to(skill_dir).as_posix()
        if rel == "SKILL.md" or f.suffix.lower() not in TEXT_EXT:
            continue
        src = f.read_text(encoding="utf-8")
        parts += ["", "---", "", f"## TÀI LIỆU KÈM THEO: `{rel}`", ""]
        if rel.startswith("references/") and f.suffix.lower() in (".html", ".htm"):
            parts.append(html_to_text(src))
        elif f.suffix.lower() == ".md":
            parts.append(src.strip())
        else:
            lang = f.suffix.lstrip(".").lower()
            parts += [f"(Tệp mẫu — sao chép nguyên văn khi tạo đầu ra.)", "", f"````{lang}", src.rstrip(), "````"]
    return "\n".join(parts) + "\n"


def update_index(skills: list[dict]) -> None:
    index = ROOT / "index.html"
    if not index.exists():
        return
    cards = []
    for s in skills:
        n = html.escape(s["name"])
        files = "".join(
            f'<li><a href="skills/{n}/{html.escape(f)}">{html.escape(f)}</a></li>' for f in s["files"]
        )
        cards.append(
            f"""      <article class="card" id="skill-{n}">
        <header><h3>{html.escape(s.get('title') or n)}</h3><code>{n}</code> <span class="ver">v{html.escape(s['version'])}</span></header>
        <p>{html.escape(s['description'])}</p>
        <details><summary>Tệp trong skill ({len(s['files'])})</summary><ul>{files}</ul></details>
        <p class="dl">
          <a class="btn" href="dist/{n}/{n}.zip" download>Tải .zip (Claude)</a>
          <a class="btn" href="dist/{n}/{n}.prompt.md" download>Tải .prompt.md (ChatGPT, Gemini…)</a>
          <a class="btn ghost" href="skills/{n}/SKILL.md">Xem SKILL.md</a>
        </p>
      </article>"""
        )
    text = index.read_text(encoding="utf-8")
    new = re.sub(
        r"(<!-- SKILLS:START -->)(.*?)(<!-- SKILLS:END -->)",
        lambda m: m.group(1) + "\n" + "\n".join(cards) + "\n      " + m.group(3),
        text,
        flags=re.S,
    )
    new = re.sub(r'(<span id="skill-count">)\d*(</span>)', rf"\g<1>{len(skills)}\g<2>", new)
    index.write_text(new, encoding="utf-8")


def update_marketplace(skills: list[dict]) -> None:
    path = ROOT / ".claude-plugin" / "marketplace.json"
    path.parent.mkdir(exist_ok=True)
    data = {
        "name": MARKETPLACE_NAME,
        "owner": {"name": REPO_SLUG.split("/")[0]},
        "metadata": {"description": "Bộ skill cho Z-World Adventure", "version": "1.0.0"},
        "plugins": [
            {
                "name": MARKETPLACE_NAME,
                "description": "Tất cả skill của Z-World Adventure",
                "source": "./",
                "strict": False,
                "skills": [f"./skills/{s['name']}" for s in skills],
            }
        ],
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def first_heading(body: str) -> str:
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return m.group(1).strip() if m else ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="chỉ kiểm tra, không build")
    args = ap.parse_args()

    dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir()) if SKILLS_DIR.exists() else []
    all_errors: list[str] = []
    results = []
    for d in dirs:
        meta, body, errors = validate(d)
        all_errors += errors
        print(f"{'✗' if errors else '✓'} {d.name}")
        if not errors:
            results.append((d, meta, body))
    if all_errors:
        print("\nLỗi:\n  " + "\n  ".join(all_errors))
        return 1
    if args.check:
        print(f"\n{len(results)} skill hợp lệ.")
        return 0

    summary = []
    for d, meta, body in results:
        out = DIST_DIR / d.name
        out.mkdir(parents=True, exist_ok=True)
        build_zip(d, out / f"{d.name}.zip")
        (out / f"{d.name}.prompt.md").write_text(build_prompt(d, meta, body), encoding="utf-8")
        md = meta.get("metadata") if isinstance(meta.get("metadata"), dict) else {}
        summary.append(
            {
                "name": meta["name"],
                "title": first_heading(body),
                "description": meta["description"],
                "version": md.get("version", "0.0.0"),
                "language": md.get("language", ""),
                "source": md.get("source", ""),
                "path": f"skills/{d.name}",
                "files": [f.relative_to(d).as_posix() for f in skill_files(d)],
                "dist": {"claude_zip": f"dist/{d.name}/{d.name}.zip", "prompt": f"dist/{d.name}/{d.name}.prompt.md"},
            }
        )
    (ROOT / "skills.json").write_text(json.dumps({"skills": summary}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    update_index(summary)
    update_marketplace(summary)
    print(f"\nĐã build {len(summary)} skill vào dist/, cập nhật skills.json, index.html, .claude-plugin/marketplace.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
