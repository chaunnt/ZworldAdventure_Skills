---
name: cach-quan-ly-du-lieu-quy-trinh-tim-kiem-loc-data-khach-hang
description: Quy trình tìm kiếm và lọc data khách hàng (doanh nghiệp, cá nhân, đối tác) trong kho data private ZWorldAdventur_Data, từ lúc lấy repo đến lúc lưu kết quả. Dùng khi người dùng hỏi "tìm doanh nghiệp", "lọc danh sách khách hàng", "tra MST/SĐT/email", "có data về ... không", hoặc bất kỳ việc nào cần data khách hàng.
license: Xem LICENSE ở thư mục gốc repo
metadata:
  version: "1.0.0"
  language: vi
  category: cach-quan-ly-du-lieu
  level: quy-trinh
  uses: "cach-to-chuc-cong-viec-clone-push-repo-github-nong-an-toan, cach-quan-ly-du-lieu-tra-cuu-chi-muc-truoc-khi-mo-file, cach-quan-ly-du-lieu-doc-excel-danh-sach-doanh-nghiep, cach-quan-ly-du-lieu-luu-ket-qua-loc-va-du-lieu-tam, cach-quan-ly-du-lieu-nhap-bo-du-lieu-vao-kho-kem-readme-chi-muc"
  summary: "[Quy trình] Tìm/lọc data khách hàng: lấy kho data private → đọc chỉ mục → mở đúng file → lọc → lưu kết quả, không đi tìm lại."
  keywords: "tìm kiếm khách hàng, lọc data khách hàng, tra mã số thuế, danh sách doanh nghiệp, kho data"
---

# Quy trình tìm kiếm, lọc data khách hàng

Kho data: repo **private** `chaunnt/ZWorldAdventur_Data`. Mọi data khách hàng, data đối tác và data tạm đều nằm trong đó. **Luôn tra kho trước**, chỉ tìm nguồn bên ngoài khi chỉ mục cho thấy kho chưa có.

## Thứ tự gọi skill

| Bước | Skill | Việc |
|---|---|---|
| 1 | `cach-to-chuc-cong-viec-clone-push-repo-github-nong-an-toan` | Clone kho data `--depth 3` (đã có bản clone thì `git pull`) |
| 2 | `cach-quan-ly-du-lieu-tra-cuu-chi-muc-truoc-khi-mo-file` | Đọc `catalog.json`/`structure.json` để chọn file, hoặc chạy `scripts/search.py` |
| 3 | `cach-quan-ly-du-lieu-doc-excel-danh-sach-doanh-nghiep` | Mở **đúng** file đã chọn và lọc theo điều kiện |
| 4 | `cach-quan-ly-du-lieu-luu-ket-qua-loc-va-du-lieu-tam` | Lưu kết quả vào `04_ket-qua-loc/` kèm README |
| 5 (nếu có data mới từ nguồn ngoài) | `cach-quan-ly-du-lieu-nhap-bo-du-lieu-vao-kho-kem-readme-chi-muc` | Nhập vào kho để lần sau khỏi phải tìm lại |

## Điểm quyết định

- Chỉ mục không có data phù hợp → báo người dùng là kho chưa có, rồi hỏi nguồn hoặc tìm ở nguồn ngoài. Tìm được thì làm bước 5.
- Kết quả lọc chỉ dùng một lần và ít dòng → có thể trả lời thẳng trong chat, nhưng vẫn nên lưu ở bước 4 nếu sau này có thể cần lại.
- Không đưa data khách hàng ra chỗ public: artifact chia sẻ, repo skill, web.
