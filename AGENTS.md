# Hướng dẫn cho AI agent

Repo này chứa các **skill** theo chuẩn Agent Skills. Mỗi skill nằm trong `skills/<ten-skill>/SKILL.md`.

## Cách dùng skill

1. Đọc danh sách skill và mô tả trong `skills.json` (hoặc phần frontmatter `description` của từng `SKILL.md`).
2. Khi yêu cầu của người dùng khớp với `description` của một skill, đọc toàn bộ `SKILL.md` của skill đó và làm theo.
3. Chỉ mở các tệp trong `references/`, `assets/`, `scripts/` của skill khi `SKILL.md` chỉ dẫn.

## Danh sách skill

| Skill | Dùng khi |
|---|---|
| `skills/the-thuc-van-ban/` | Soạn, định dạng, rà soát văn bản QPPL / công văn theo NĐ 78/2025/NĐ-CP |
| `skills/viet-skill/` | Tạo hoặc sửa skill trong repo này, đóng gói cho Claude/ChatGPT/Gemini |

## Khi chỉnh sửa repo

- Tạo/sửa skill theo `skills/viet-skill/SKILL.md`.
- Sau khi sửa, chạy `python3 scripts/build_skills.py` và commit cả `dist/`, `skills.json`, `index.html`, `.claude-plugin/marketplace.json`.
