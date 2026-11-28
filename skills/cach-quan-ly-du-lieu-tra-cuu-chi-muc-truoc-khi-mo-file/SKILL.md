---
name: cach-quan-ly-du-lieu-tra-cuu-chi-muc-truoc-khi-mo-file
description: Tra cứu kho data ZWorldAdventur_Data bằng chỉ mục (catalog.json, structure.json) và script search.py thay vì mở từng file để dò. Dùng mỗi khi cần biết kho có data gì, file nào chứa thông tin cần tìm, hoặc tìm một MST/tên/SĐT cụ thể.
license: Xem LICENSE ở thư mục gốc repo
metadata:
  version: "1.0.0"
  language: vi
  category: cach-quan-ly-du-lieu
  level: don-le
  summary: "[Đơn lẻ] Đọc catalog.json/structure.json để chọn đúng file, tìm giá trị bằng scripts/search.py; KHÔNG mở từng file để dò."
  keywords: "chỉ mục, catalog.json, structure.json, search.py, tra cứu kho data"
---

# Tra cứu chỉ mục trước khi mở file

Người dùng đã yêu cầu rõ: **đọc chỉ mục, không mở từng file để tìm kiếm.** Mở lần lượt từng file Excel vừa tốn thời gian vừa tốn token.

## Các tệp chỉ mục ở gốc kho data

| Tệp | Chứa gì | Khi nào đọc |
|---|---|---|
| `catalog.json` | Mỗi file data: `duong_dan`, `mo_ta` (lấy từ README thư mục), `sheets[]` gồm `cot`, `dong_tieu_de`, `so_dong_du_lieu` | Luôn đọc đầu tiên |
| `structure.json` | Cây thư mục và `purpose` của từng thư mục | Khi cần biết nên tìm hoặc lưu ở đâu |
| `<thu-muc>/README.md` | Nguồn, ngày nhận, lưu ý của bộ data | Khi `mo_ta` trong catalog chưa đủ |

## Các bước

1. Đọc `catalog.json` và chọn file theo `mo_ta` cùng `cot`.
2. Cần tìm một giá trị cụ thể → chạy **một** lệnh:
   ```bash
   python3 scripts/search.py "từ khoá" [--dir 01_khach-hang] [--limit 50]
   ```
   Lệnh tìm không phân biệt hoa thường và dấu (gõ "cong ty abc" vẫn khớp "CÔNG TY ABC"). Kết quả có dạng `file | sheet | dòng | nội dung`.
3. Chỉ mở file mà chỉ mục hoặc kết quả search trỏ tới.
4. Thấy chỉ mục thiếu hoặc sai → sửa README của thư mục đó, chạy `python3 scripts/build_catalog.py`, rồi commit.
