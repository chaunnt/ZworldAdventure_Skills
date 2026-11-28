# SKILL: cach-quan-ly-du-lieu-doc-excel-danh-sach-doanh-nghiep

> Tệp này gộp toàn bộ skill thành một tài liệu duy nhất để dùng với ChatGPT, Gemini hoặc model bất kỳ.
> Hãy làm theo phần HƯỚNG DẪN CHÍNH; các phần TÀI LIỆU KÈM THEO là tài liệu tra cứu được nhắc tới trong hướng dẫn.
> Nguồn: https://github.com/chaunnt/ZworldAdventure_Skills/tree/main/skills/cach-quan-ly-du-lieu-doc-excel-danh-sach-doanh-nghiep

**Mô tả / khi nào dùng:** Đọc và lọc file Excel danh sách doanh nghiệp/người lao động của cơ quan nhà nước, loại có dòng tiêu đề lớn, ô gộp, cột công thức (vd. DS nộp Quỹ phòng chống thiên tai), bằng Python openpyxl. Dùng khi cần lọc theo MST, phường, tên DN, số tiền trong các file xlsx kiểu này.

---

## HƯỚNG DẪN CHÍNH (SKILL.md)

# Đọc Excel danh sách doanh nghiệp

## Đặc điểm loại file này (rút ra từ việc đọc file thật)

- Dòng 1 là tiêu đề lớn (ô gộp, có `\n`). **Dòng tiêu đề cột nằm ở dòng 2 hoặc 3**, mỗi sheet một khác. Xem `dong_tieu_de` trong `catalog.json`, hoặc tìm dòng đầu tiên có ít nhất 3 ô không rỗng.
- Tên cột chứa `\n` (vd. `"Tên doanh nghiệp \nnộp thuế"`), nên trước khi so khớp cần thay `\n` bằng dấu cách và strip.
- **MST là chuỗi, có số 0 ở đầu** (`0301234567` (ví dụ giả)). Không ép kiểu sang int.
- STT thường là float (`1.0`).
- Cột số tiền là **công thức** (`=ROUND(IF(J3<=500000,...))`). Đọc `data_only=True` thì có thể ra `None` nếu file chưa được Excel tính lại. Khi đó tự tính lại theo công thức: đọc `data_only=False` để xem công thức gốc.
- Thường có 2 sheet: `Doanh nghiep` (MST, tên, địa chỉ, email, SĐT, tài sản) và `NLĐ` (tên DN, địa chỉ, MST, số lao động). Muốn nối hai sheet thì dùng MST làm khoá.
- Tên DN viết không thống nhất giữa các sheet ("CÔNG TY TNHH" và "CTY TNHH"). Khi so khớp nên chuẩn hoá: viết thường, bỏ dấu, `cty`→`cong ty`.

## Mẫu code

```python
import openpyxl, unicodedata
def norm(s): s=unicodedata.normalize("NFD",str(s or "").lower()); return "".join(c for c in s if unicodedata.category(c)!="Mn").replace("đ","d")
wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
ws = wb["Doanh nghiep"]; rows = list(ws.iter_rows(values_only=True))
hdr_i = next(i for i,r in enumerate(rows[:10]) if sum(v not in (None,"") for v in r) >= 3)
cols = [str(v or "").replace("\n"," ").strip() for v in rows[hdr_i]]
data = [dict(zip(cols, r)) for r in rows[hdr_i+1:] if any(r)]
kq = [d for d in data if "phuong x" in norm(d.get("Tên phường/xã"))]
```

Dùng `read_only=True` với file lớn. Muốn xuất kết quả thì ghi CSV UTF-8 có BOM (`utf-8-sig`) để Excel mở không lỗi font.
