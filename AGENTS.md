# Hướng dẫn cho AI agent

Repo này là thư viện **skill** theo chuẩn Agent Skills. Đọc từ nông đến sâu, dừng khi đủ thông tin — không tải toàn bộ repo:

1. **`llms.txt`** — mỗi skill một dòng (tên, đường dẫn `SKILL.md`, tóm tắt). Bản JSON: `skills.json`.
   Khi có nhiều skill, `llms.txt` chỉ liệt kê danh mục; danh sách chi tiết nằm ở `danh-muc/<slug>/llms.txt`.
2. Chọn skill khớp yêu cầu → đọc **`skills/<ten>/SKILL.md`** và làm theo.
3. Chỉ mở tệp trong `skills/<ten>/references/` khi `SKILL.md` chỉ dẫn.

## Danh sách skill (sinh tự động)

<!-- SKILLS:START -->
| Skill | Danh mục | Tóm tắt |
|---|---|---|
| [`cach-viet-van-ban-quy-pham-phap-luat-ndcp78-2025`](skills/cach-viet-van-ban-quy-pham-phap-luat-ndcp78-2025/SKILL.md) | Cách viết văn bản | Thể thức, kỹ thuật trình bày văn bản QPPL theo NĐ 78/2025/NĐ-CP: cỡ chữ, vị trí, số ký hiệu, ký, nơi nhận, sơ đồ A4. |
| [`cach-viet-van-ban-skill-ai-da-nen-tang`](skills/cach-viet-van-ban-skill-ai-da-nen-tang/SKILL.md) | Cách viết văn bản | Quy chuẩn tạo skill đa nền tảng (Claude, ChatGPT, Gemini), chuyển tài liệu/PDF thành skill và đóng gói. |
<!-- SKILLS:END -->

## Khi chỉnh sửa repo

- Tạo/sửa skill theo `skills/cach-viet-van-ban-skill-ai-da-nen-tang/SKILL.md`. Danh mục khai báo trong `categories.json`.
- Sau khi sửa, chạy `python3 scripts/build_skills.py` rồi commit mọi thay đổi.
- Các tệp sau là **sinh tự động, không sửa tay**: `llms.txt`, `skills.json`, `index.html`, `huong-dan.html`,
  `danh-muc/**`, `skills/*/index.html`, `sitemap.xml`, `robots.txt`, `dist/**`, `.claude-plugin/marketplace.json`,
  và khối giữa `SKILLS:START/END` trong `README.md`, `AGENTS.md`.
