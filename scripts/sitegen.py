"""Sinh lớp điều hướng cho người, công cụ tìm kiếm và AI agent.

Được gọi từ build_skills.py. Đầu ra (đều là tệp sinh tự động, không sửa tay):
    llms.txt, danh-muc/<slug>/llms.txt      – danh mục rút gọn cho LLM (1 dòng/skill)
    skills.json                              – danh mục máy đọc
    index.html, huong-dan.html               – trang chủ, trang hướng dẫn
    danh-muc/<slug>/index.html, page-N.html  – trang danh mục có phân trang
    skills/<ten>/index.html                  – trang giới thiệu từng skill
    sitemap.xml, robots.txt, .nojekyll
"""
from __future__ import annotations

import html
import json
import math
from pathlib import Path

E = html.escape

HOME_PER_CATEGORY = 8      # số skill tối đa mỗi danh mục hiển thị trên trang chủ
PAGE_SIZE = 20             # số skill mỗi trang danh mục
LLMS_INLINE_LIMIT = 80     # quá số này, llms.txt gốc chỉ liệt kê danh mục và trỏ tới llms.txt của từng danh mục


# ------------------------------------------------------------------ helpers
def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _jsonld(obj: dict) -> str:
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def _page_name(n: int) -> str:
    return "index.html" if n == 1 else f"page-{n}.html"


class Site:
    def __init__(self, root: Path, cfg: dict, categories: dict, skills: list[dict]):
        self.root, self.cfg, self.categories, self.skills = root, cfg, categories, skills
        self.base = cfg["base_url"].rstrip("/") + "/"
        self.by_cat: dict[str, list[dict]] = {k: [] for k in categories}
        for s in skills:
            self.by_cat.setdefault(s["category"], []).append(s)
        self.urls: list[str] = []

    # ---------------------------------------------------------- urls
    def abs(self, rel: str) -> str:
        return self.base + rel

    @staticmethod
    def cat_rel(slug: str, page: int = 1) -> str:
        return f"danh-muc/{slug}/" + ("" if page == 1 else _page_name(page))

    @staticmethod
    def skill_rel(name: str) -> str:
        return f"skills/{name}/"

    # ---------------------------------------------------------- layout
    def layout(self, *, rel_path: str, title: str, description: str, body: str, keywords: str = "",
               jsonld: list[dict] | None = None, extra_head: str = "", nav: str = "") -> str:
        depth = rel_path.count("/")
        up = "../" * depth
        canonical = self.abs(rel_path.removesuffix("index.html"))
        self.urls.append(canonical)
        site = self.cfg["site_name"]
        full_title = title if title == site else f"{title} | {site}"
        navs = [("", "Trang chủ", "home"), ("danh-muc/", "Danh mục", "cat"), ("huong-dan.html", "Hướng dẫn", "guide"),
                ("llms.txt", "llms.txt", "llms")]
        nav_html = "".join(
            f'<a href="{up}{href}"{" aria-current=\"page\"" if key == nav else ""}>{E(label)}</a>' for href, label, key in navs
        )
        ld = "".join(_jsonld(x) for x in (jsonld or []))
        return f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full_title)}</title>
<meta name="description" content="{E(description)}">
{f'<meta name="keywords" content="{E(keywords)}">' if keywords else ''}
<meta name="robots" content="index, follow, max-snippet:-1">
<link rel="canonical" href="{E(canonical)}">
<link rel="alternate" type="text/plain" title="llms.txt — danh mục cho AI" href="{up}llms.txt">
<link rel="alternate" type="application/json" title="Danh mục skill (JSON)" href="{up}skills.json">
<link rel="sitemap" type="application/xml" href="{up}sitemap.xml">
{extra_head}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{E(site)}">
<meta property="og:locale" content="vi_VN">
<meta property="og:title" content="{E(full_title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:url" content="{E(canonical)}">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="{up}static/site.css">
{ld}
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="{up}">{E(site)}</a>
  <nav aria-label="Điều hướng chính">{nav_html}</nav>
</div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">{E(site)} · <a href="{E(self.cfg['repo_url'])}">Mã nguồn GitHub</a> ·
<a href="{up}llms.txt">llms.txt</a> · <a href="{up}skills.json">skills.json</a> · <a href="{up}sitemap.xml">sitemap.xml</a></div></footer>
</body>
</html>
"""

    def crumbs(self, items: list[tuple[str, str]], up: str) -> tuple[str, dict]:
        """items: [(rel_url, label)] – phần tử cuối là trang hiện tại."""
        lis = []
        for i, (rel, label) in enumerate(items):
            if i == len(items) - 1:
                lis.append(f'<li aria-current="page">{E(label)}</li>')
            else:
                lis.append(f'<li><a href="{up}{rel}">{E(label)}</a></li>')
        ld = {
            "@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": label, "item": self.abs(rel)}
                for i, (rel, label) in enumerate(items)
            ],
        }
        return f'<ol class="crumbs" aria-label="Breadcrumb">{"".join(lis)}</ol>', ld

    def skill_items(self, skills: list[dict], up: str) -> str:
        out = []
        for s in skills:
            n = E(s["name"])
            out.append(
                f'<li><h3><a href="{up}{self.skill_rel(s["name"])}">{E(s["title"])}</a></h3>'
                f'<p>{E(s["summary"])}</p>'
                f'<p class="meta"><code>{n}</code> · <span class="ver">v{E(s["version"])}</span> · '
                f'<a href="{up}skills/{n}/SKILL.md" type="text/markdown">SKILL.md</a></p></li>'
            )
        return '<ul class="list">' + "".join(out) + "</ul>"

    def item_list_ld(self, skills: list[dict], name: str, offset: int = 0) -> dict:
        return {
            "@context": "https://schema.org", "@type": "ItemList", "name": name, "numberOfItems": len(skills),
            "itemListElement": [
                {"@type": "ListItem", "position": offset + i + 1, "url": self.abs(self.skill_rel(s["name"])), "name": s["title"]}
                for i, s in enumerate(skills)
            ],
        }

    # ---------------------------------------------------------- pages
    def home(self) -> None:
        cfg = self.cfg
        sections = []
        for slug, cat in self.categories.items():
            items = self.by_cat.get(slug, [])
            if not items:
                continue
            more = ""
            if len(items) > HOME_PER_CATEGORY:
                more = f'<a class="more" href="{self.cat_rel(slug)}">Xem tất cả {len(items)} skill →</a>'
            sections.append(
                f'<section id="{E(slug)}" aria-labelledby="h-{E(slug)}"><div class="cat-head">'
                f'<h2 id="h-{E(slug)}"><a href="{self.cat_rel(slug)}">{E(cat["title"])}</a></h2>'
                f'<p>{len(items)} skill</p></div><p class="lead">{E(cat["summary"])}</p>'
                f'{self.skill_items(items[:HOME_PER_CATEGORY], "")}{more}</section>'
            )
        body = f"""<h1>{E(cfg['site_name'])}: thư viện skill cho AI agent</h1>
<p class="lead">{E(cfg['site_description'])}</p>
<aside class="ai-box" aria-label="Hướng dẫn cho AI agent">
  <p><strong>Dành cho AI agent — đọc từ nông đến sâu, dừng khi đủ:</strong></p>
  <ol>
    <li><a href="llms.txt"><code>llms.txt</code></a> — mỗi skill một dòng (hoặc <a href="skills.json"><code>skills.json</code></a>).</li>
    <li>Chọn đúng skill → mở <code>skills/&lt;ten&gt;/SKILL.md</code>.</li>
    <li>Chỉ mở tệp trong <code>references/</code> khi SKILL.md chỉ dẫn. Không tải toàn bộ repo.</li>
  </ol>
</aside>
{''.join(sections)}
<p><a href="huong-dan.html">Cách cài skill vào Claude, ChatGPT, Gemini và cách viết skill mới →</a></p>"""
        ld = [
            {"@context": "https://schema.org", "@type": "WebSite", "name": cfg["site_name"], "url": self.base,
             "inLanguage": "vi", "description": cfg["site_description"]},
            self.item_list_ld(self.skills, "Danh sách skill"),
        ]
        _write(self.root / "index.html", self.layout(
            rel_path="index.html", title=cfg["site_name"], description=cfg["site_description"], body=body,
            keywords=cfg.get("keywords", ""), jsonld=ld, nav="home"))

    def category_index(self) -> None:
        rows = "".join(
            f'<li><h3><a href="../{self.cat_rel(slug)}">{E(c["title"])}</a></h3><p>{E(c["summary"])}</p>'
            f'<p class="meta">{len(self.by_cat.get(slug, []))} skill · <a href="../danh-muc/{E(slug)}/llms.txt">llms.txt</a></p></li>'
            for slug, c in self.categories.items()
        )
        crumbs, ld = self.crumbs([("", "Trang chủ"), ("danh-muc/", "Danh mục")], "../")
        body = f'{crumbs}<h1>Danh mục skill</h1><p class="lead">{len(self.categories)} danh mục, {len(self.skills)} skill.</p><ul class="list">{rows}</ul>'
        _write(self.root / "danh-muc/index.html", self.layout(
            rel_path="danh-muc/index.html", title="Danh mục skill",
            description="Danh sách danh mục skill cho AI agent: " + ", ".join(c["title"] for c in self.categories.values()),
            body=body, jsonld=[ld], nav="cat"))

    def category_pages(self) -> None:
        import shutil
        for old in (self.root / "danh-muc").glob("*/"):
            if old.is_dir() and old.name not in self.categories:
                shutil.rmtree(old)  # danh mục đã bị xoá/đổi tên
        for slug, cat in self.categories.items():
            items = self.by_cat.get(slug, [])
            pages = max(1, math.ceil(len(items) / PAGE_SIZE))
            folder = self.root / "danh-muc" / slug
            for old in folder.glob("page-*.html"):
                old.unlink()
            for p in range(1, pages + 1):
                chunk = items[(p - 1) * PAGE_SIZE: p * PAGE_SIZE]
                up = "../../"
                trail = [("", "Trang chủ"), ("danh-muc/", "Danh mục"), (self.cat_rel(slug), cat["title"])]
                if p > 1:
                    trail.append((self.cat_rel(slug, p), f"Trang {p}"))
                crumbs, bld = self.crumbs(trail, up)
                pager = ""
                head = ""
                if pages > 1:
                    links = []
                    for i in range(1, pages + 1):
                        links.append(f'<span aria-current="page">{i}</span>' if i == p else f'<a href="{_page_name(i) if i > 1 else "./"}">{i}</a>')
                    pager = f'<nav class="pager" aria-label="Phân trang">{"".join(links)}</nav>'
                    if p > 1:
                        head += f'<link rel="prev" href="{E(self.abs(self.cat_rel(slug, p - 1)))}">'
                    if p < pages:
                        head += f'<link rel="next" href="{E(self.abs(self.cat_rel(slug, p + 1)))}">'
                title = cat["title"] + (f" – trang {p}" if p > 1 else "")
                body = (f'{crumbs}<h1>{E(title)}</h1><p class="lead">{E(cat["summary"])}</p>'
                        f'<p class="meta">{len(items)} skill · Bản rút gọn cho AI: <a href="llms.txt">llms.txt</a></p>'
                        f'{self.skill_items(chunk, up)}{pager}')
                _write(folder / _page_name(p), self.layout(
                    rel_path=f"danh-muc/{slug}/{_page_name(p)}", title=title, description=cat["summary"], body=body,
                    jsonld=[bld, self.item_list_ld(chunk, cat["title"], (p - 1) * PAGE_SIZE)], extra_head=head, nav="cat"))
            # llms.txt của danh mục
            lines = [f"# {cat['title']}", "", f"> {cat['summary']}", "",
                     "Mỗi dòng là một skill. Mở SKILL.md của skill phù hợp; chỉ mở references/ khi SKILL.md chỉ dẫn.", "",
                     "## Skills", ""]
            lines += [f"- [{s['name']}]({self.abs('skills/' + s['name'] + '/SKILL.md')}): {s['summary']}" for s in items]
            _write(folder / "llms.txt", "\n".join(lines) + "\n")

    def skill_pages(self) -> None:
        for s in self.skills:
            n = s["name"]
            cat = self.categories[s["category"]]
            up = "../../"
            crumbs, bld = self.crumbs([("", "Trang chủ"), (self.cat_rel(s["category"]), cat["title"]),
                                       (self.skill_rel(n), s["title"])], up)
            docs = "".join(
                f'<li><a href="{E(f)}"><code>{E(f)}</code></a> — {E(when)}</li>' for f, when in s["docs"]
            ) or '<li><a href="SKILL.md"><code>SKILL.md</code></a></li>'
            outline = "".join(f"<li>{E(h)}</li>" for h in s["outline"])
            listed = {f for f, _ in s["docs"]}
            rest = [f for f in s["files"] if f not in listed]
            files = "".join(f'<li><a href="{E(f)}"><code>{E(f)}</code></a></li>' for f in rest)
            meta_rows = [("Tên kỹ thuật", f"<code>{E(n)}</code>"), ("Phiên bản", E(s["version"])),
                         ("Danh mục", f'<a href="{up}{self.cat_rel(s["category"])}">{E(cat["title"])}</a>')]
            if s.get("source"):
                meta_rows.append(("Nguồn", E(s["source"])))
            if s.get("keywords"):
                meta_rows.append(("Từ khoá", E(s["keywords"])))
            kv = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in meta_rows)
            body = f"""{crumbs}
<h1>{E(s['title'])}</h1>
<p class="lead">{E(s['summary'])}</p>
<div class="btns">
  <a class="btn" href="SKILL.md" type="text/markdown">Đọc SKILL.md</a>
  <a class="btn ghost" href="{up}dist/{E(n)}/{E(n)}.zip" download>Tải .zip (Claude)</a>
  <a class="btn ghost" href="{up}dist/{E(n)}/{E(n)}.prompt.md" download>Tải .prompt.md (ChatGPT, Gemini…)</a>
</div>
<section aria-labelledby="h-when"><h2 id="h-when">Khi nào dùng</h2><p>{E(s['description'])}</p></section>
<div class="grid">
  <section class="card" aria-labelledby="h-order"><h2 id="h-order">Thứ tự đọc cho AI</h2><ol>{docs}</ol></section>
  <section class="card" aria-labelledby="h-outline"><h2 id="h-outline">Mục lục SKILL.md</h2><ul>{outline}</ul></section>
  <section class="card" aria-labelledby="h-meta"><h2 id="h-meta">Thông tin</h2><dl class="kv">{kv}</dl></section>
  {f'<section class="card" aria-labelledby="h-files"><h2 id="h-files">Tệp khác trong skill</h2><ul>{files}</ul></section>' if files else ''}
</div>"""
            ld = {
                "@context": "https://schema.org", "@type": "TechArticle", "headline": s["title"],
                "name": n, "description": s["summary"], "abstract": s["description"], "inLanguage": "vi",
                "version": s["version"], "keywords": s.get("keywords", ""), "url": self.abs(self.skill_rel(n)),
                "isPartOf": {"@type": "WebSite", "name": self.cfg["site_name"], "url": self.base},
                "encoding": {"@type": "MediaObject", "contentUrl": self.abs(f"skills/{n}/SKILL.md"), "encodingFormat": "text/markdown"},
            }
            if s.get("source"):
                ld["isBasedOn"] = s["source"]
            head = f'<link rel="alternate" type="text/markdown" title="SKILL.md" href="SKILL.md">'
            _write(self.root / "skills" / n / "index.html", self.layout(
                rel_path=f"skills/{n}/index.html", title=s["title"], description=s["summary"], body=body,
                keywords=s.get("keywords", ""), jsonld=[bld, ld], extra_head=head, nav="cat"))

    def guide(self) -> None:
        r = self.cfg["repo_slug"]
        crumbs, bld = self.crumbs([("", "Trang chủ"), ("huong-dan.html", "Hướng dẫn")], "")
        body = f"""{crumbs}
<h1>Hướng dẫn sử dụng và viết skill</h1>
<p class="lead">Mỗi skill viết một lần theo chuẩn mở Agent Skills, dùng được trên nhiều nền tảng.
Bản đóng gói nằm trong <code>dist/&lt;ten&gt;/</code>: <code>.zip</code> cho Claude, <code>.prompt.md</code> (một tệp gộp) cho ChatGPT, Gemini và model khác.</p>
<section aria-labelledby="h-struct"><h2 id="h-struct">Cấu trúc một skill</h2>
<pre>skills/&lt;ten-skill&gt;/
├── SKILL.md        # frontmatter (name, description, metadata.category, metadata.summary) + hướng dẫn
├── index.html      # trang giới thiệu (sinh tự động)
├── references/     # tài liệu tra cứu chi tiết (.html, .md) — chỉ đọc khi SKILL.md chỉ dẫn
└── scripts/        # mã hỗ trợ (tuỳ chọn)</pre></section>
<section aria-labelledby="h-platform"><h2 id="h-platform">Cài đặt theo nền tảng</h2>
<div class="grid">
  <div class="card"><h3>Claude</h3><ul>
    <li><strong>claude.ai / Desktop:</strong> Settings → Capabilities → Skills → Upload tệp <code>.zip</code>.</li>
    <li><strong>Claude Code:</strong> <code>/plugin marketplace add {E(r)}</code> rồi <code>/plugin install zworld-skills@zworld-skills</code>.</li>
    <li>Hoặc chép thư mục skill vào <code>~/.claude/skills/</code>.</li></ul></div>
  <div class="card"><h3>ChatGPT</h3><ul>
    <li><strong>Custom GPT / Project:</strong> upload <code>.prompt.md</code> vào Knowledge.</li>
    <li>Instructions: “Làm việc theo skill trong tệp &lt;tên&gt;.prompt.md ở Knowledge.”</li>
    <li><strong>Codex:</strong> chép thư mục skill vào thư mục skills của Codex.</li></ul></div>
  <div class="card"><h3>Gemini</h3><ul>
    <li><strong>Gem:</strong> upload <code>.prompt.md</code> vào Knowledge hoặc dán vào Instructions.</li>
    <li><strong>AI Studio:</strong> dán <code>.prompt.md</code> vào System instructions.</li>
    <li><strong>Gemini CLI:</strong> chép thư mục skill vào thư mục skills của Gemini CLI.</li></ul></div>
  <div class="card"><h3>Agent khác</h3><ul>
    <li>Đọc <a href="llms.txt"><code>llms.txt</code></a> hoặc <a href="skills.json"><code>skills.json</code></a> trước, rồi mới mở SKILL.md cần thiết.</li>
    <li>Clone repo: <code>AGENTS.md</code> ở gốc chỉ cho Cursor, Copilot, Windsurf… cách dùng skill.</li></ul></div>
</div>
<p>Chi tiết: <a href="skills/cach-viet-van-ban-skill-ai-da-nen-tang/references/nen-tang.md"><code>skills/cach-viet-van-ban-skill-ai-da-nen-tang/references/nen-tang.md</code></a>.</p></section>
<section aria-labelledby="h-write"><h2 id="h-write">Viết skill mới</h2><ol>
  <li>Dùng skill <a href="skills/cach-viet-van-ban-skill-ai-da-nen-tang/">cach-viet-van-ban-skill-ai-da-nen-tang</a> hoặc chép <code>skills/cach-viet-van-ban-skill-ai-da-nen-tang/assets/SKILL.template.md</code>.</li>
  <li>Khai báo <code>metadata.category</code> (có trong <code>categories.json</code>) và <code>metadata.summary</code> ≤ 160 ký tự.</li>
  <li>Chạy <code>python3 scripts/build_skills.py</code> — tự sinh lại trang, <code>llms.txt</code>, sitemap, gói tải về.</li>
  <li>Commit toàn bộ thay đổi.</li></ol></section>"""
        _write(self.root / "huong-dan.html", self.layout(
            rel_path="huong-dan.html", title="Hướng dẫn sử dụng và viết skill",
            description="Cách cài skill vào Claude, ChatGPT, Gemini, Codex và cách viết skill mới chuẩn đa nền tảng.",
            body=body, jsonld=[bld], nav="guide"))

    # ---------------------------------------------------------- machine-readable
    def llms(self) -> None:
        cfg = self.cfg
        L = [f"# {cfg['site_name']}", "", f"> {cfg['site_description']}", "",
             "Cách đọc để tiết kiệm token:",
             "1. Lướt danh sách dưới đây (mỗi skill một dòng: tên, đường dẫn SKILL.md, tóm tắt) và chọn skill khớp yêu cầu.",
             "2. Mở SKILL.md của skill đó và làm theo. Chỉ mở tệp trong references/ khi SKILL.md chỉ dẫn.",
             "3. Không tải toàn bộ repo hay mọi skill cùng lúc.", "",
             f"Danh mục máy đọc (JSON): {self.abs('skills.json')}", ""]
        inline = len(self.skills) <= LLMS_INLINE_LIMIT
        for slug, cat in self.categories.items():
            items = self.by_cat.get(slug, [])
            if not items:
                continue
            L += [f"## {cat['title']}", "", f"{cat['summary']} ({len(items)} skill)", ""]
            if inline:
                L += [f"- [{s['name']}]({self.abs('skills/' + s['name'] + '/SKILL.md')}): {s['summary']}" for s in items]
            else:
                L.append(f"- [Danh sách skill]({self.abs(self.cat_rel(slug) + 'llms.txt')})")
            L.append("")
        L += ["## Optional", "",
              f"- [Hướng dẫn cài đặt theo nền tảng]({self.abs('skills/cach-viet-van-ban-skill-ai-da-nen-tang/references/nen-tang.md')}): Claude, ChatGPT, Gemini, Codex",
              f"- [Mã nguồn]({cfg['repo_url']}): repo GitHub", ""]
        _write(self.root / "llms.txt", "\n".join(L))

    def catalog(self) -> None:
        data = {
            "name": self.cfg["site_name"], "base_url": self.base, "llms_txt": self.abs("llms.txt"),
            "usage": "Chọn skill theo summary; tải skill_md; chỉ mở references khi SKILL.md chỉ dẫn.",
            "categories": [
                {"slug": k, "title": c["title"], "summary": c["summary"], "count": len(self.by_cat.get(k, [])),
                 "page": self.abs(self.cat_rel(k)), "llms_txt": self.abs(self.cat_rel(k) + "llms.txt")}
                for k, c in self.categories.items()
            ],
            "skills": [
                {"name": s["name"], "title": s["title"], "category": s["category"], "summary": s["summary"],
                 "keywords": s.get("keywords", ""), "version": s["version"],
                 "skill_md": self.abs(f"skills/{s['name']}/SKILL.md"), "page": self.abs(self.skill_rel(s["name"])),
                 "claude_zip": self.abs(f"dist/{s['name']}/{s['name']}.zip"),
                 "prompt_md": self.abs(f"dist/{s['name']}/{s['name']}.prompt.md")}
                for s in self.skills
            ],
        }
        _write(self.root / "skills.json", json.dumps(data, ensure_ascii=False, indent=2) + "\n")

    def seo_files(self) -> None:
        extra = [self.abs("llms.txt")] + [self.abs(f"skills/{s['name']}/SKILL.md") for s in self.skills]
        urls = sorted(set(self.urls)) + extra
        xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        xml += [f"  <url><loc>{E(u)}</loc></url>" for u in urls]
        xml.append("</urlset>")
        _write(self.root / "sitemap.xml", "\n".join(xml) + "\n")
        _write(self.root / "robots.txt",
               "# Cho phép mọi công cụ tìm kiếm và AI crawler đọc thư viện skill.\n"
               "# Danh mục rút gọn cho LLM: " + self.abs("llms.txt") + "\n"
               "User-agent: *\nAllow: /\n\nSitemap: " + self.abs("sitemap.xml") + "\n")
        _write(self.root / ".nojekyll", "")

    def build(self) -> None:
        self.home()
        self.category_index()
        self.category_pages()
        self.skill_pages()
        self.guide()
        self.llms()
        self.catalog()
        self.seo_files()
