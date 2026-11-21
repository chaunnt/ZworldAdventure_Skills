# ZworldAdventure_Skills

Thư viện **skill cho AI agent** của Z-World Adventure, viết theo chuẩn mở [Agent Skills](https://agentskills.io) —
dùng được với Claude, ChatGPT, Gemini, Codex, Cursor, Copilot...

- Website: https://chaunnt.github.io/ZworldAdventure_Skills/ (bật GitHub Pages: Settings → Pages → Deploy from branch `main`, thư mục `/`)
- Cho AI: [`llms.txt`](llms.txt) · [`skills.json`](skills.json) · [`AGENTS.md`](AGENTS.md)

## Skill hiện có

<!-- SKILLS:START -->
| Skill | Danh mục | Tóm tắt |
|---|---|---|
| [`cach-viet-van-ban-quy-pham-phap-luat-ndcp78-2025`](skills/cach-viet-van-ban-quy-pham-phap-luat-ndcp78-2025/SKILL.md) | Cách viết văn bản | Thể thức, kỹ thuật trình bày văn bản QPPL theo NĐ 78/2025/NĐ-CP: cỡ chữ, vị trí, số ký hiệu, ký, nơi nhận, sơ đồ A4. |
| [`cach-viet-van-ban-skill-ai-da-nen-tang`](skills/cach-viet-van-ban-skill-ai-da-nen-tang/SKILL.md) | Cách viết văn bản | Quy chuẩn tạo skill đa nền tảng (Claude, ChatGPT, Gemini), chuyển tài liệu/PDF thành skill và đóng gói. |
<!-- SKILLS:END -->

## Cấu trúc

```
skills/<ten-skill>/        # nguồn: SKILL.md + references/ (+ scripts/); index.html là trang sinh tự động
categories.json            # khai báo danh mục
scripts/build_skills.py    # kiểm tra + đóng gói + sinh điều hướng (gọi scripts/sitegen.py)
dist/<ten-skill>/          # bản build: <ten>.zip (Claude), <ten>.prompt.md (ChatGPT, Gemini, model khác)
llms.txt, skills.json      # danh mục rút gọn cho LLM / máy đọc
index.html, huong-dan.html, danh-muc/   # website (SEO: sitemap.xml, robots.txt, JSON-LD, canonical)
AGENTS.md                  # hướng dẫn cho agent (CLAUDE.md, GEMINI.md trỏ về đây)
.claude-plugin/            # marketplace để cài bằng Claude Code
```

## Lớp điều hướng cho AI (tiết kiệm token)

`llms.txt` (1 dòng/skill) → `danh-muc/<slug>/llms.txt` (khi nhiều skill) → `skills/<ten>/SKILL.md` → `references/...`

## Import nhanh

- **Claude.ai**: Settings → Capabilities → Skills → Upload `dist/<ten>/<ten>.zip`.
- **Claude Code**: `/plugin marketplace add chaunnt/ZworldAdventure_Skills` → `/plugin install zworld-skills@zworld-skills`.
- **ChatGPT (Custom GPT/Project)**, **Gemini (Gem)**: upload `dist/<ten>/<ten>.prompt.md` vào Knowledge.
- **Codex / Gemini CLI / agent khác**: chép `skills/<ten>/` vào thư mục skills của công cụ, hoặc clone repo.

Chi tiết: [`huong-dan.html`](huong-dan.html), [`skills/cach-viet-van-ban-skill-ai-da-nen-tang/references/nen-tang.md`](skills/cach-viet-van-ban-skill-ai-da-nen-tang/references/nen-tang.md).

## Thêm skill mới

```bash
mkdir -p skills/<ten-skill> && cp skills/cach-viet-van-ban-skill-ai-da-nen-tang/assets/SKILL.template.md skills/<ten-skill>/SKILL.md
# điền nội dung, khai báo metadata.category (categories.json) và metadata.summary
python3 scripts/build_skills.py
```
