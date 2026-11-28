#!/usr/bin/env python3
"""Kiểm tra, đóng gói các skill trong skills/ và sinh lớp điều hướng (llms.txt, trang web, sitemap).

Chỉ dùng thư viện chuẩn Python 3.9+.

    python3 scripts/build_skills.py          # kiểm tra + build dist/ + sinh llms.txt, skills.json, trang HTML, sitemap...
    python3 scripts/build_skills.py --check  # chỉ kiểm tra hợp lệ (trả mã lỗi 1 nếu có lỗi)

Đổi địa chỉ website (vd khi dùng tên miền riêng): đặt biến môi trường SITE_BASE_URL.
"""
from __future__ import annotations

import argparse
import html
import json
import os
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
SITE = {
    "site_name": "Z-World Skills",
    "site_description": "Thư viện skill (Agent Skills) cho AI agent của Z-World Adventure: hướng dẫn nghiệp vụ "
                        "đóng gói sẵn, dùng được với Claude, ChatGPT, Gemini, Codex và các agent khác.",
    "keywords": "agent skills, AI agent, Claude skills, ChatGPT, Gemini, llms.txt, Z-World Adventure",
    "base_url": os.environ.get("SITE_BASE_URL", "https://chaunnt.github.io/ZworldAdventure_Skills/"),
    "repo_url": f"https://github.com/{REPO_SLUG}",
    "repo_slug": REPO_SLUG,
}
SUMMARY_MAX = 160
GENERATED_IN_SKILL = {"index.html"}  # tệp sinh tự động trong thư mục skill, không đưa vào gói

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


def load_categories() -> dict:
    path = ROOT / "categories.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


# Repo public: chặn thông tin cá nhân / data khách hàng cụ thể lọt vào skill.
PII_PATTERNS = {
    "email": re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"),
    "số điện thoại": re.compile(r"(?<![\d/])(?:\+84|0)[35789]\d{8}(?![\d/])"),
    "MST/CCCD/số tài khoản": re.compile(r"(?<![\d/.])\d{10}(?:-\d{3})?(?![\d/])|(?<![\d/.])\d{12}(?![\d/])"),
}
PII_ALLOW = re.compile(r"@example\.(com|org|vn)$|^0301234567$|^000000000000$|^0900000000$")


def scan_personal_data(skill_dir: Path) -> list[str]:
    """Báo lỗi nếu tệp trong skill chứa email/SĐT/MST/CCCD thật. Ví dụ giả hợp lệ: ...@example.com, 0301234567, 0900000000."""
    errs = []
    for f in skill_dir.rglob("*"):
        if not f.is_file() or f.name in GENERATED_IN_SKILL or f.suffix.lower() not in TEXT_EXT:
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        for label, pat in PII_PATTERNS.items():
            for m in pat.finditer(text):
                if not PII_ALLOW.search(m.group(0)):
                    errs.append(f"{skill_dir.name}: {f.relative_to(skill_dir)} có thể chứa {label} thật "
                                f"('{m.group(0)}') — repo public, thay bằng dữ liệu giả")
    return errs


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
    md = meta.get("metadata") if isinstance(meta.get("metadata"), dict) else {}
    cats = load_categories()
    if md.get("category") not in cats:
        errors.append(f"{skill_dir.name}: metadata.category '{md.get('category')}' chưa có trong categories.json")
    cat = md.get("category", "")
    if cat and not name.startswith(cat + "-"):
        errors.append(f"{skill_dir.name}: tên skill phải bắt đầu bằng slug danh mục '{cat}-' (Quy chuẩn đặt tên skill)")
    if re.search(r"(^|-)(helper|tool|misc|chung|moi|test|v\d+)(-|$)", name):
        errors.append(f"{skill_dir.name}: tên chứa từ mơ hồ bị cấm (helper, tool, misc, chung, moi, test, vN)")
    summ = md.get("summary", "")
    if not summ:
        errors.append(f"{skill_dir.name}: thiếu metadata.summary (1 câu ≤ {SUMMARY_MAX} ký tự)")
    elif len(summ) > SUMMARY_MAX:
        errors.append(f"{skill_dir.name}: metadata.summary dài {len(summ)} > {SUMMARY_MAX} ký tự")
    extra = set(meta) - ALLOWED_KEYS
    if extra:
        errors.append(f"{skill_dir.name}: khoá frontmatter không hỗ trợ: {', '.join(sorted(extra))}")
    errors += scan_personal_data(skill_dir)
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
    return sorted(
        p for p in skill_dir.rglob("*")
        if p.is_file() and not p.name.startswith(".") and "__pycache__" not in p.parts
        and p.relative_to(skill_dir).as_posix() not in GENERATED_IN_SKILL
    )


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


def doc_table(body: str) -> list[tuple[str, str]]:
    """Lấy bảng 'Tài liệu trong skill' (| `tệp` | khi nào đọc |) để làm 'thứ tự đọc cho AI'."""
    rows = []
    for m in re.finditer(r"^\|\s*`([^`]+)`[^|]*\|\s*(.+?)\s*\|\s*$", body, re.M):
        when = re.sub(r"\*\*|`", "", m.group(2))
        rows.append((m.group(1), when))
    return rows


def outline(body: str) -> list[str]:
    return [h.strip() for h in re.findall(r"^##\s+(.+)$", body, re.M)]


def replace_block(path: Path, marker: str, content: str) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    new = re.sub(rf"(<!-- {marker}:START -->)(.*?)(<!-- {marker}:END -->)",
                 lambda m: m.group(1) + "\n" + content + "\n" + m.group(3), text, flags=re.S)
    path.write_text(new, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="chỉ kiểm tra, không build")
    args = ap.parse_args()

    dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir() and not d.name.startswith(("_", "."))) if SKILLS_DIR.exists() else []
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

    categories = load_categories()
    skills = []
    for d, meta, body in results:
        out = DIST_DIR / d.name
        out.mkdir(parents=True, exist_ok=True)
        build_zip(d, out / f"{d.name}.zip")
        (out / f"{d.name}.prompt.md").write_text(build_prompt(d, meta, body), encoding="utf-8")
        md = meta.get("metadata") if isinstance(meta.get("metadata"), dict) else {}
        skills.append({
            "name": meta["name"], "title": first_heading(body) or meta["name"], "description": meta["description"],
            "category": md["category"], "summary": md["summary"], "keywords": md.get("keywords", ""),
            "version": md.get("version", "0.0.0"), "source": md.get("source", ""),
            "files": [f.relative_to(d).as_posix() for f in skill_files(d)],
            "docs": doc_table(body), "outline": outline(body),
        })
    # xoá bản build của skill đã bị xoá/đổi tên
    names = {s["name"] for s in skills}
    if DIST_DIR.exists():
        for old in DIST_DIR.iterdir():
            if old.is_dir() and old.name not in names:
                for f in old.iterdir():
                    f.unlink()
                old.rmdir()
    order = {k: i for i, k in enumerate(categories)}
    skills.sort(key=lambda s: (order.get(s["category"], 999), s["title"]))

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import sitegen  # scripts/sitegen.py
    sitegen.Site(ROOT, SITE, categories, skills).build()
    update_marketplace(skills)
    table = "\n".join(["| Skill | Danh mục | Tóm tắt |", "|---|---|---|"] + [
        f"| [`{s['name']}`](skills/{s['name']}/SKILL.md) | {categories[s['category']]['title']} | {s['summary']} |" for s in skills])
    replace_block(ROOT / "README.md", "SKILLS", table)
    replace_block(ROOT / "AGENTS.md", "SKILLS", table)
    print(f"\nĐã build {len(skills)} skill. Sinh lại: dist/, llms.txt, skills.json, index.html, huong-dan.html, "
          "danh-muc/, skills/*/index.html, sitemap.xml, robots.txt, marketplace.json, README.md, AGENTS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
