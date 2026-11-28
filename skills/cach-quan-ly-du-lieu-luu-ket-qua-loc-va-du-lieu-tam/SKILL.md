---
name: cach-quan-ly-du-lieu-luu-ket-qua-loc-va-du-lieu-tam
description: Lưu kết quả tìm kiếm/lọc data và data tạm vào kho data private ZWorldAdventur_Data theo quy ước thư mục có ngày, kèm README ghi nguồn, điều kiện lọc, số dòng, hạn xoá. Dùng sau khi lọc xong data khách hàng, hoặc khi cần giữ tạm data giữa các bước hay các phiên làm việc.
license: Xem LICENSE ở thư mục gốc repo
metadata:
  version: "1.0.0"
  language: vi
  category: cach-quan-ly-du-lieu
  level: don-le
  summary: "[Đơn lẻ] Lưu kết quả lọc vào 04_ket-qua-loc/ và data tạm vào 03_du-lieu-tam/ theo thư mục <ngày>_<mô-tả> kèm README."
  keywords: "kết quả lọc, data tạm, lưu tạm, xuất csv, README kết quả"
---

# Lưu kết quả lọc và dữ liệu tạm

## Quy ước

| Loại | Thư mục | README bắt buộc ghi |
|---|---|---|
| Kết quả lọc | `04_ket-qua-loc/<YYYY-MM-DD>_<mo-ta-cu-the>/` | Lọc từ file nào (đường dẫn), điều kiện lọc, số dòng, mục đích/ai yêu cầu |
| Data tạm | `03_du-lieu-tam/<YYYY-MM-DD>_<mo-ta-cu-the>/` | Mục đích, ngày tạo, **khi nào có thể xoá** |

Tên mô tả cần cụ thể. Ví dụ: `2026-11-28_dn-phuong-x-co-email-tai-san-tren-10-ty`, không đặt kiểu `ket-qua-1`.

## Các bước

1. Xuất kết quả ra CSV `utf-8-sig`. Nếu người dùng cần Excel thì xuất xlsx. Đặt tên file mô tả rõ nội dung.
2. Viết README theo bảng trên. Có script lọc thì lưu kèm (`loc.py`) để chạy lại được.
3. Chạy `python3 scripts/build_catalog.py`, commit, push.
4. Mỗi lần mở kho, xem `03_du-lieu-tam/`: mục nào đã quá hạn xoá thì hỏi người dùng trước khi xoá.
