# SKILL: cach-quan-ly-du-lieu-nhap-bo-du-lieu-vao-kho-kem-readme-chi-muc

> Tệp này gộp toàn bộ skill thành một tài liệu duy nhất để dùng với ChatGPT, Gemini hoặc model bất kỳ.
> Hãy làm theo phần HƯỚNG DẪN CHÍNH; các phần TÀI LIỆU KÈM THEO là tài liệu tra cứu được nhắc tới trong hướng dẫn.
> Nguồn: https://github.com/chaunnt/ZworldAdventure_Skills/tree/main/skills/cach-quan-ly-du-lieu-nhap-bo-du-lieu-vao-kho-kem-readme-chi-muc

**Mô tả / khi nào dùng:** Đưa một bộ data (file Excel/CSV/JSON khách hàng, đối tác, tham chiếu) vào kho data private ZWorldAdventur_Data đúng thư mục, kèm README, cập nhật structure.json và catalog.json, commit và push. Dùng khi người dùng gửi file data, khi tìm được data từ nguồn ngoài, hoặc nói "lưu data này vào repo".

---

## HƯỚNG DẪN CHÍNH (SKILL.md)

# Nhập bộ dữ liệu vào kho kèm README và chỉ mục

## Cây thư mục kho (cấp 1)

| Thư mục | Đặt gì |
|---|---|
| `01_khach-hang/doanh-nghiep/`, `01_khach-hang/ca-nhan/` | Data khách hàng gốc, chia `<chu-de>/<nam>/<dia-ban>_<dot>/` |
| `02_doi-tac/<ten-doi-tac>/<YYYY-MM>/` | Data đối tác, file đối soát |
| `03_du-lieu-tam/<YYYY-MM-DD>_<mo-ta>/` | Data tạm |
| `04_ket-qua-loc/<YYYY-MM-DD>_<mo-ta>/` | Kết quả lọc |
| `05_tham-chieu/` | Danh mục tra cứu dùng chung |

Tên thư mục viết chữ thường, không dấu, nối bằng `-`, dùng `_` để tách cấp ý nghĩa. Ví dụ: `quy-phong-chong-thien-tai/2026/<ten-phuong>_dot-2`.

## Các bước

1. Chọn thư mục đích theo `structure.json`, đường dẫn **càng cụ thể càng tốt**. Giữ nguyên tên file gốc (`git mv` nếu file đã có trong repo).
2. Tạo `README.md` ở thư mục lá, ghi: tên file, nguồn, ngày nhận, sheet và cột chính, dòng tiêu đề, lưu ý (vd. cột là công thức). Nội dung README này được đưa vào `catalog.json`, nên cần viết rõ để chỉ đọc chỉ mục là đủ.
3. Có thư mục mới → thêm node vào `structure.json` và ghi `purpose`. Mỗi thư mục cha cũng có README.
4. Chạy `python3 scripts/build_catalog.py`.
5. Commit với message `[thư-mục] mô tả ngắn`, rồi push.

## Lưu ý

- Chỉ lưu vào kho **private**. Kiểm tra lại visibility nếu không chắc.
- Không sửa file gốc trong `01_`/`02_`. Bản đã xử lý để ở `04_`.
