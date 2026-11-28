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
| [`cach-to-chuc-cong-viec-chia-nho-viec-va-ghi-kinh-nghiem-skill`](skills/cach-to-chuc-cong-viec-chia-nho-viec-va-ghi-kinh-nghiem-skill/SKILL.md) | Cách tổ chức công việc | [Quy trình] Gốc của mọi việc: tra skill có sẵn, chia việc lớn thành skill đơn lẻ + skill quy trình, ghi kinh nghiệm lại vào repo. |
| [`cach-to-chuc-cong-viec-clone-push-repo-github-nong-an-toan`](skills/cach-to-chuc-cong-viec-clone-push-repo-github-nong-an-toan/SKILL.md) | Cách tổ chức công việc | [Đơn lẻ] Clone repo GitHub depth 3, kiểm tra public/private trước khi lưu data, commit + push an toàn từ bản clone nông. |
| [`cach-quan-ly-du-lieu-luu-ket-qua-loc-va-du-lieu-tam`](skills/cach-quan-ly-du-lieu-luu-ket-qua-loc-va-du-lieu-tam/SKILL.md) | Cách quản lý dữ liệu | [Đơn lẻ] Lưu kết quả lọc vào 04_ket-qua-loc/ và data tạm vào 03_du-lieu-tam/ theo thư mục <ngày>_<mô-tả> kèm README. |
| [`cach-quan-ly-du-lieu-nhap-bo-du-lieu-vao-kho-kem-readme-chi-muc`](skills/cach-quan-ly-du-lieu-nhap-bo-du-lieu-vao-kho-kem-readme-chi-muc/SKILL.md) | Cách quản lý dữ liệu | [Đơn lẻ] Nhập file data vào kho private đúng thư mục: tạo README thư mục lá, cập nhật structure.json, build catalog.json, commit. |
| [`cach-quan-ly-du-lieu-quy-trinh-tim-kiem-loc-data-khach-hang`](skills/cach-quan-ly-du-lieu-quy-trinh-tim-kiem-loc-data-khach-hang/SKILL.md) | Cách quản lý dữ liệu | [Quy trình] Tìm/lọc data khách hàng: lấy kho data private → đọc chỉ mục → mở đúng file → lọc → lưu kết quả, không đi tìm lại. |
| [`cach-quan-ly-du-lieu-tra-cuu-chi-muc-truoc-khi-mo-file`](skills/cach-quan-ly-du-lieu-tra-cuu-chi-muc-truoc-khi-mo-file/SKILL.md) | Cách quản lý dữ liệu | [Đơn lẻ] Đọc catalog.json/structure.json để chọn đúng file, tìm giá trị bằng scripts/search.py; KHÔNG mở từng file để dò. |
| [`cach-quan-ly-du-lieu-doc-excel-danh-sach-doanh-nghiep`](skills/cach-quan-ly-du-lieu-doc-excel-danh-sach-doanh-nghiep/SKILL.md) | Cách quản lý dữ liệu | [Đơn lẻ] Đọc/lọc Excel DS doanh nghiệp kiểu cơ quan nhà nước: tìm dòng tiêu đề, MST dạng chuỗi, cột công thức ra None. |
<!-- SKILLS:END -->

## Quy trình làm việc chung

- Bắt đầu mọi việc: đọc skill `cach-to-chuc-cong-viec-chia-nho-viec-va-ghi-kinh-nghiem-skill`. Kết thúc việc: ghi kinh nghiệm thành skill **đơn lẻ** (`metadata.level: don-le`, summary bắt đầu bằng `[Đơn lẻ]`) và skill **quy trình** (`level: quy-trinh`, `uses:` liệt kê skill đơn lẻ, summary bắt đầu bằng `[Quy trình]`).
- Tên skill phải cụ thể, đọc là hiểu (5-15 từ không dấu cũng được, ≤ 64 ký tự).
- **Repo public, không làm lộ thông tin cá nhân**: không ghi tên, MST, CCCD, SĐT, email, địa chỉ của người hay doanh nghiệp cụ thể, cũng không ghi token hay mật khẩu. Ví dụ dùng dữ liệu giả. Data thật để ở kho private `chaunnt/ZWorldAdventur_Data`.

## Khi chỉnh sửa repo

- Tạo/sửa skill theo `skills/cach-viet-van-ban-skill-ai-da-nen-tang/SKILL.md`. Danh mục khai báo trong `categories.json`.
- Sau khi sửa, chạy `python3 scripts/build_skills.py` rồi commit mọi thay đổi.
- Các tệp sau là **sinh tự động, không sửa tay**: `llms.txt`, `skills.json`, `index.html`, `huong-dan.html`,
  `danh-muc/**`, `skills/*/index.html`, `sitemap.xml`, `robots.txt`, `dist/**`, `.claude-plugin/marketplace.json`,
  và khối giữa `SKILLS:START/END` trong `README.md`, `AGENTS.md`.
