# Cách import skill vào từng nền tảng

Mọi skill nằm ở `skills/<ten>/`. Sau khi chạy `python3 scripts/build_skills.py`, thư mục `dist/<ten>/` có:

| Tệp | Dùng cho |
|---|---|
| `<ten>.zip` | Claude (claude.ai, Claude Desktop), API Skills — zip chứa thư mục `<ten>/` với `SKILL.md` ở trong |
| `<ten>.prompt.md` | ChatGPT, Gemini, hoặc bất kỳ model nào: một tệp duy nhất gồm SKILL.md + toàn bộ references đã chuyển thành văn bản |

> Giao diện các sản phẩm thay đổi thường xuyên; tên menu dưới đây có thể khác đôi chút theo phiên bản.

## Claude

- **claude.ai / Claude Desktop**: Settings → Capabilities → Skills → *Upload skill* → chọn `dist/<ten>/<ten>.zip`.
- **Claude Code** (một trong các cách):
  - Cài cả bộ qua plugin marketplace của repo:
    `/plugin marketplace add chaunnt/ZworldAdventure_Skills` rồi `/plugin install zworld-skills@zworld-skills`.
  - Hoặc sao chép thư mục: `cp -r skills/<ten> ~/.claude/skills/` (dùng cho mọi dự án)
    hoặc vào `.claude/skills/` của một dự án.
- **Claude API / Agent SDK**: upload thư mục skill qua Skills API, hoặc đặt trong `.claude/skills/` của dự án dùng Agent SDK.

## ChatGPT

- **Custom GPT** (Explore GPTs → Create → Configure):
  - *Instructions*: dán câu sau (giới hạn ký tự của ô này nhỏ, nên không dán cả skill):
    `Bạn làm việc theo skill trong tệp <ten>.prompt.md ở Knowledge. Luôn đọc và tuân thủ tệp đó trước khi trả lời.`
  - *Knowledge*: upload `dist/<ten>/<ten>.prompt.md`.
- **Project trong ChatGPT**: thêm `<ten>.prompt.md` vào Project files và dán câu trên vào Project instructions.
- **Codex CLI / agent hỗ trợ Agent Skills**: sao chép `skills/<ten>/` vào thư mục skills của công cụ
  (thường `~/.codex/skills/` hoặc `.agents/skills/` trong dự án — xem tài liệu phiên bản đang dùng).
- **Một lần dùng nhanh**: dán nội dung `<ten>.prompt.md` vào đầu cuộc trò chuyện.

## Gemini

- **Gem** (Gemini → Gems → New Gem): *Instructions* dán câu tương tự như ChatGPT; *Knowledge* upload `<ten>.prompt.md`
  (hoặc dán thẳng nội dung `<ten>.prompt.md` vào Instructions nếu đủ chỗ).
- **Gemini CLI**: phiên bản mới hỗ trợ Agent Skills — sao chép `skills/<ten>/` vào thư mục skills của Gemini CLI
  (thường `~/.gemini/skills/` hoặc `.gemini/skills/`); hoặc tham chiếu `AGENTS.md`/`GEMINI.md` trỏ tới skill.
- **Google AI Studio / Vertex**: dán `<ten>.prompt.md` vào *System instructions*.

## Agent khác (Cursor, GitHub Copilot, Windsurf, agent tự viết...)

- Clone repo; tệp `AGENTS.md` ở gốc repo liệt kê các skill và hướng dẫn agent đọc `skills/<ten>/SKILL.md` khi phù hợp.
- Với agent tự viết: nạp `description` của mọi skill (từ `skills.json`) vào system prompt; khi một skill khớp yêu cầu
  thì nạp `SKILL.md` của nó; chỉ nạp references khi SKILL.md yêu cầu.
