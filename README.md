# ZworldAdventure_Skills

Bộ **skill cho AI agent** của Z-World Adventure, viết theo chuẩn mở [Agent Skills](https://agentskills.io) —
dùng được với Claude, ChatGPT, Gemini, Codex, Cursor, Copilot...

👉 Trang giới thiệu: mở [`index.html`](index.html) (hoặc bật GitHub Pages cho repo).

## Skill hiện có

| Skill | Mô tả |
|---|---|
| [`the-thuc-van-ban`](skills/the-thuc-van-ban/SKILL.md) | Soạn, định dạng, rà soát văn bản QPPL và công văn theo Nghị định 78/2025/NĐ-CP (kèm sơ đồ bố trí mô tả bằng lời, mẫu HTML5 khổ A4) |
| [`viet-skill`](skills/viet-skill/SKILL.md) | Tạo skill mới chuẩn đa nền tảng, chuyển tài liệu/PDF thành skill, đóng gói cho từng model |

## Cấu trúc

```
skills/<ten-skill>/      # nguồn: SKILL.md + references/ + assets/ (+ scripts/)
dist/<ten-skill>/        # bản build: <ten>.zip (Claude), <ten>.prompt.md (ChatGPT, Gemini, model khác)
scripts/build_skills.py  # kiểm tra + build + cập nhật index.html, skills.json, marketplace
AGENTS.md                # hướng dẫn cho agent (CLAUDE.md, GEMINI.md trỏ về đây)
.claude-plugin/          # marketplace để cài bằng Claude Code
```

## Import nhanh

- **Claude.ai**: Settings → Capabilities → Skills → Upload `dist/<ten>/<ten>.zip`.
- **Claude Code**: `/plugin marketplace add chaunnt/ZworldAdventure_Skills` → `/plugin install zworld-skills@zworld-skills`.
- **ChatGPT (Custom GPT/Project)** và **Gemini (Gem)**: upload `dist/<ten>/<ten>.prompt.md` vào Knowledge, Instructions ghi
  “Làm việc theo skill trong tệp <ten>.prompt.md”.
- **Codex / Gemini CLI / agent khác**: chép `skills/<ten>/` vào thư mục skills của công cụ, hoặc clone repo (đã có `AGENTS.md`).

Chi tiết: [`skills/viet-skill/references/nen-tang.md`](skills/viet-skill/references/nen-tang.md).

## Thêm skill mới

```bash
mkdir -p skills/<ten-skill> && cp skills/viet-skill/assets/SKILL.template.md skills/<ten-skill>/SKILL.md
python3 scripts/build_skills.py
```
