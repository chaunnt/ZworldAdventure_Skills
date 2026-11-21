---
name: viet-noi-dung-van-ban-quy-pham-phap-luat-ndcp78-2025
description: Soạn thảo, định dạng và rà soát thể thức, kỹ thuật trình bày văn bản quy phạm pháp luật Việt Nam (luật, pháp lệnh, nghị quyết, nghị định, quyết định, thông tư, thông tư liên tịch, lệnh) theo Nghị định 78/2025/NĐ-CP. Dùng khi người dùng yêu cầu viết hoặc trình bày văn bản QPPL, Quốc hiệu - Tiêu ngữ, số ký hiệu, tên văn bản, căn cứ ban hành, chương/điều/khoản/điểm, chữ ký TM./KT., nơi nhận, phụ lục, sơ đồ bố trí trang A4, hoặc kiểm tra văn bản có đúng thể thức NĐ 78/2025 không.
license: Xem LICENSE ở thư mục gốc repo
metadata:
  version: "1.1.0"
  language: vi
  category: phap-ly-van-ban
  summary: "Thể thức, kỹ thuật trình bày văn bản QPPL theo NĐ 78/2025/NĐ-CP: cỡ chữ, vị trí, số ký hiệu, ký, nơi nhận, sơ đồ A4."
  keywords: "văn bản quy phạm pháp luật, thể thức văn bản, Nghị định 78/2025/NĐ-CP, trình bày văn bản, nghị định, thông tư, quyết định"
  source: "Nghị định số 78/2025/NĐ-CP ngày 01/4/2025 của Chính phủ - Phụ lục thể thức, kỹ thuật trình bày văn bản QPPL (bản đăng trên Báo điện tử Chính phủ, 09/04/2025)"
---

# Viết nội dung văn bản quy phạm pháp luật theo NĐ 78/2025/NĐ-CP

Skill này giúp bạn (agent) **soạn mới** hoặc **rà soát** một văn bản sao cho đúng thể thức
và kỹ thuật trình bày theo Nghị định 78/2025/NĐ-CP.

## Tài liệu trong skill

| Tệp | Khi nào đọc |
|---|---|
| `SKILL.md` (tệp này) | Luôn đọc. Có quy trình, bảng tra nhanh, checklist. |
| `references/quy-dinh-chi-tiet.html` | Khi cần câu chữ đầy đủ của quy định (số ký hiệu từng loại văn bản, ký thay/thay mặt, địa danh, phụ lục, sửa đổi bổ sung). |
| `references/so-do-bo-tri.html` | Khi cần biết **vị trí** từng thành phần trên trang A4. Sơ đồ đã được mô tả hoàn toàn bằng lời + toạ độ phần trăm + JSON, không cần nhìn hình. |

Thứ tự đọc để tiết kiệm token: tệp này → (nếu cần) đúng mục trong `references/`. Các tệp `.html` là HTML5 thuần,
đọc được như văn bản; nếu không mở được tệp phụ, quy tắc quan trọng nhất đã có trong bảng tra nhanh bên dưới.

## Phạm vi và lưu ý về nguồn

- Nguồn gốc của skill: Phụ lục về thể thức, kỹ thuật trình bày **văn bản quy phạm pháp luật (QPPL)**
  ban hành kèm NĐ 78/2025/NĐ-CP.
- Phạm vi: chỉ **văn bản QPPL**. Công văn và văn bản hành chính khác thuộc Nghị định 30/2020/NĐ-CP về công tác
  văn thư — không nằm trong skill này; nếu người dùng cần, hãy nói rõ và chỉ dùng phần bố cục chung một cách thận trọng.
- Khi quy định cho phép một khoảng (ví dụ cỡ chữ 13–14), hãy chọn **một giá trị và dùng thống nhất**
  trong toàn văn bản (mặc định đề xuất: nội dung 14, các thành phần khác theo bảng).
- Không bịa số hiệu, ngày ban hành, tên người ký, căn cứ pháp lý. Thiếu thông tin thì để chỗ trống
  dạng `[...]` và liệt kê cho người dùng điền.

## Quy trình làm việc

1. **Xác định loại văn bản** (luật, pháp lệnh, nghị quyết QH/UBTVQH/HĐND, nghị định, quyết định,
   thông tư, thông tư liên tịch, nghị quyết liên tịch, lệnh/quyết định Chủ tịch nước).
   Loại văn bản quyết định: cấu trúc số ký hiệu, có/không có địa danh–ngày ở đầu, từ khoá
   "QUYẾT NGHỊ/QUYẾT ĐỊNH/LỆNH", cách ký (TM./KT.), vị trí chữ ký.
2. **Thu thập dữ liệu**: tên cơ quan ban hành, số thứ tự, năm, chữ viết tắt, địa danh, ngày ký,
   tên gọi (trích yếu), căn cứ, nội dung, người ký và chức vụ, nơi nhận, phụ lục.
3. **Dựng khung trang** theo `references/so-do-bo-tri.html` (A4 dọc, lề trái 30–35 mm, lề trên/dưới/phải 15–20 mm).
4. **Điền thành phần thể thức** theo bảng tra nhanh (cỡ chữ, kiểu chữ, căn lề, đường kẻ).
5. **Trình bày nội dung**: Phần/Chương/Mục/Điều/Khoản/Điểm đúng ký số (La Mã / Ả Rập / chữ cái tiếng Việt).
6. **Tự kiểm tra** bằng checklist, rồi trả kết quả theo mục "Định dạng đầu ra".

Khi **rà soát** văn bản có sẵn: đi lần lượt từng ô 1→11 của sơ đồ và từng dòng của checklist, báo lỗi theo
dạng `Ô số – thành phần – sai ở đâu – sửa thành gì`.

## Quy định chung

- Khổ giấy **A4 (210 × 297 mm)**, trình bày theo **chiều dài** (dọc). Phụ lục có bảng biểu được phép xoay ngang.
- **Lề**: trên, dưới, phải **15–20 mm**; trái **30–35 mm**.
  *(Hình sơ đồ trong bản gốc ghi lề trên/dưới 20–25 mm — chênh với lời văn; ưu tiên lời văn 15–20 mm.
  Xem chi tiết trong `so-do-bo-tri.html`.)*
- **Phông**: Times New Roman, Unicode TCVN 6909:2001, **màu đen**.
- **Số trang**: số Ả Rập, cỡ 13, đứng, **canh giữa ở lề trên**, **không hiện số ở trang 1**.
  Văn bản ban hành kèm theo và từng Phụ lục đánh số trang riêng.

## Bảng tra nhanh thành phần thể thức

Quy ước: **IN HOA** = toàn bộ chữ in hoa; *in thường* = chữ thường, viết hoa theo chính tả.
"Đứng" = không nghiêng. Ô số = số trên sơ đồ bố trí.

| Ô | Thành phần | Chữ | Cỡ | Kiểu | Vị trí / ghi chú |
|---|---|---|---|---|---|
| 1 | Quốc hiệu `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` | IN HOA | 12–13 | đứng, đậm | Trên cùng, bên phải trang 1 |
| 1 | Tiêu ngữ `Độc lập - Tự do - Hạnh phúc` | in thường, viết hoa chữ đầu mỗi cụm | 13–14 | đứng, đậm | Canh giữa ngay dưới Quốc hiệu; gạch nối có cách chữ; **đường kẻ liền dài bằng dòng chữ** ở dưới |
| 2 | Tên cơ quan / chức danh ban hành | IN HOA, **một dòng** | 12–13 | đứng, đậm | Trên cùng, bên trái; **đường kẻ liền dài 1/3–1/2 dòng chữ**, canh giữa ở dưới. Lệnh/QĐ Chủ tịch nước: hình Quốc huy phía trên |
| 3 | Từ `Số:` | in thường | 13 | đứng | Canh giữa dưới tên cơ quan; số < 10 thêm `0` (vd `05`) |
| 3 | Ký hiệu (vd `/2025/NĐ-CP`) | IN HOA | 13 | đứng | Viết liền, không cách; `/` giữa số–năm–ký hiệu; `-` giữa các nhóm viết tắt |
| 4 | Địa danh, ngày tháng năm | in thường | 13–14 | **nghiêng** | Cùng dòng với số ký hiệu, canh giữa dưới Quốc hiệu–Tiêu ngữ; dấu `,` sau địa danh. **Không** áp dụng cho văn bản của QH, UBTVQH, HĐND |
| 5 | Tên loại văn bản (vd `NGHỊ ĐỊNH`) | IN HOA | 14 | đứng, đậm | Canh giữa |
| 5 | Tên gọi / trích yếu | in thường | 13–14 | đứng, đậm | Dưới tên loại, canh giữa; **đường kẻ 1/3–1/2** ở dưới |
| 5 | Tên luật, pháp lệnh | IN HOA | 14 | đứng, đậm | Tên loại và tên gọi trên các dòng riêng |
| 5 | Chú thích văn bản kèm theo `(Kèm theo ...)` | in thường, trong ngoặc đơn | 13–14 | **nghiêng** | Liền dưới tên văn bản, canh giữa; đường kẻ 1/3–1/2 ở dưới |
| 6 | Căn cứ ban hành | in thường | 14 | **nghiêng** | Dưới tên văn bản; mỗi căn cứ một dòng, cuối dòng `;` |
| 6 | Dòng "[Cơ quan] ban hành [tên văn bản]" (luật, pháp lệnh, NQ liên tịch) | in thường | 13–14 | nghiêng | Dưới căn cứ, kết thúc `.` |
| 6 | `QUYẾT NGHỊ:` / `QUYẾT ĐỊNH:` / `LỆNH:` / `NAY…` | IN HOA | 13 | đứng, đậm | Dòng riêng, canh giữa, có `:` |
| 6 | Nội dung | in thường | 13–14 | đứng | Canh đều hai lề; thụt đầu dòng 1–1,27 cm; cách đoạn ≥ 6 pt; giãn dòng từ đơn đến 1,5 lines |
| 6 | `Phần I`, `Chương I` | in thường | 13–14 | đứng, đậm | Dòng riêng, canh giữa; số **La Mã** |
| 6 | Tên phần, chương | IN HOA | 14 | đứng, đậm | Dưới, canh giữa |
| 6 | `Mục 1`, `Tiểu mục 1` | in thường | 13–14 | đứng, đậm | Dòng riêng, canh giữa; số **Ả Rập** |
| 6 | Tên mục, tiểu mục | IN HOA | 13–14 | đứng, đậm | Dưới, canh giữa |
| 6 | `Điều 1. Tên điều` | in thường | 13–14 | đứng, đậm | Lùi trái 1–1,27 cm; số Ả Rập + `.` |
| 6 | Khoản `1.` | in thường | 13–14 | đứng | Số Ả Rập + `.`; khoản có tên thì số + tên trên một dòng riêng |
| 6 | Điểm `a)` | in thường | 13–14 | đứng | Chữ cái tiếng Việt + `)`: a, b, c, d, đ, e, g, h, i, k, l, m, n, o, p, q, r, s, t, u, v, x, y |
| — | Thông tin thông qua (luật/NQ QH, NQ HĐND) | in thường | 13–14 | nghiêng | Dưới điều cuối; khoá = La Mã, kỳ họp = Ả Rập (trừ "kỳ họp thứ nhất"). Luật/NQ QH: **đường kẻ liền từ lề trái đến lề phải** ngăn cách điều cuối với dòng này |
| 7a | Quyền hạn (`TM.`, `KT.`, `Q.`) và chức vụ người ký | IN HOA | 13 | đứng, đậm | Phía phải, dưới điều cuối (xem quy tắc ký) |
| 7c | Chữ ký | — | — | — | Giữa 7a và 7b |
| 7b | Họ và tên người ký | in thường | 13–14 | đứng, đậm | Canh giữa so với chức vụ |
| 8 | Dấu | — | — | — | Đóng sau khi ký; theo sơ đồ, hình tròn dấu trùm lên phần bên trái của chữ ký (7c) |
| 9 | `Nơi nhận:` | in thường | **12** | **nghiêng, đậm** | Dòng riêng, ngang hàng dòng chức vụ (7a), sát lề trái |
| 9 | Danh sách nơi nhận | in thường | **11** | đứng | Mỗi nơi một dòng, đầu dòng `-` sát lề trái, cuối dòng `;` |
| 9 | Dòng lưu | in thường | 11 | đứng | Dòng cuối: `- Lưu: VT, [viết tắt đơn vị soạn thảo], [số bản lưu].` |
| 10 | Dấu chỉ mức độ mật | — | — | — | Bên trái, dưới số ký hiệu (theo pháp luật bảo vệ bí mật nhà nước) |
| 11 | Ký hiệu người đánh máy, số lượng bản phát hành | — | — | — | Cuối khối nơi nhận, góc dưới bên phải khối đó |
| — | Số trang | Ả Rập | 13 | đứng | Canh giữa lề trên, ẩn ở trang 1 |
| PL | `Phụ lục I` | in thường | 13–14 | đứng, đậm | Dòng riêng, canh giữa; ≥ 2 phụ lục thì đánh số La Mã |
| PL | Tên phụ lục | IN HOA | 13–14 | đứng, đậm | Canh giữa |
| PL | Thông tin chỉ dẫn `(Kèm theo ... số ..., ngày ... của ...)` | in thường | 13–14 | nghiêng | Canh giữa, dưới tên phụ lục |

## Số, ký hiệu theo loại văn bản (tóm tắt)

- Luật, NQ Quốc hội, pháp lệnh, NQ UBTVQH: loại văn bản + số thứ tự + năm + viết tắt cơ quan + **số khoá Quốc hội**.
- Nghị quyết liên tịch, thông tư liên tịch: số + năm + viết tắt loại văn bản + viết tắt các cơ quan cùng ban hành (nối bằng `-`).
- Lệnh, quyết định Chủ tịch nước: số + năm + viết tắt loại văn bản + viết tắt chức danh (`CTN`).
- Văn bản QPPL khác: số + năm + viết tắt loại văn bản + viết tắt cơ quan/chức danh.
  Ví dụ thực tế: `Số: 78/2025/NĐ-CP`.
- Số thứ tự đánh theo **từng loại văn bản, từng năm**, bắt đầu từ `01` ngày 01/01, kết thúc 31/12; năm ghi đủ 4 chữ số.

## Ngày tháng và địa danh

- Viết đủ: `Hà Nội, ngày 05 tháng 01 năm 2025` — ngày < 10 và **tháng 1, 2** thêm `0`; tháng 3–12 không thêm
  (`ngày 01 tháng 4 năm 2025`, `ngày 15 tháng 12 năm 2025`).
- Cơ quan trung ương: địa danh là tỉnh/thành phố trực thuộc TW nơi đóng trụ sở. Cơ quan địa phương: tên chính thức
  của đơn vị hành chính. Đơn vị hành chính đặt theo tên người, chữ số, sự kiện lịch sử: ghi **tên đầy đủ**.

## Quy tắc ký (tóm tắt)

- Ký thay mặt tập thể: `TM. CHÍNH PHỦ` / `TM. ỦY BAN NHÂN DÂN` / `TM. HỘI ĐỒNG THẨM PHÁN` rồi dòng chức vụ
  (`THỦ TƯỚNG`, `CHỦ TỊCH`, `CHÁNH ÁN`).
- Cấp phó ký thay: `KT. [CHỨC VỤ NGƯỜI ĐỨNG ĐẦU]` rồi dòng chức vụ cấp phó (vd `KT. BỘ TRƯỞNG` / `THỨ TRƯỞNG`).
- QĐ Thủ tướng, thông tư Bộ trưởng/Thủ trưởng cơ quan ngang bộ, Chánh án TANDTC, Viện trưởng VKSNDTC,
  Tổng KTNN: ghi chức vụ người ký.
- Thông tư liên tịch: cơ quan **chủ trì ký bên phải**, cơ quan cùng ký bên trái.
- Nghị quyết liên tịch: chữ ký các bên đặt cân đối hai bên, ghi rõ tên cơ quan + chức vụ, có `TM.`.
- Luật/NQ Quốc hội: chức vụ người ký chứng thực ở bên phải, dưới dòng thông tin thông qua.
  NQ HĐND: Chủ tịch HĐND ký chứng thực.

## Checklist tự kiểm tra

- [ ] A4 dọc; lề trái 30–35 mm, các lề khác 15–20 mm; Times New Roman, màu đen.
- [ ] Quốc hiệu IN HOA đậm 12–13, bên phải; Tiêu ngữ đậm 13–14 có gạch nối cách chữ, có đường kẻ dài bằng dòng chữ.
- [ ] Tên cơ quan IN HOA đậm một dòng bên trái, đường kẻ 1/3–1/2.
- [ ] `Số:` 13 thường; ký hiệu IN HOA 13, viết liền; số < 10 có `0`; năm đủ 4 số.
- [ ] Địa danh–ngày nghiêng, cùng dòng với số (trừ VB của QH/UBTVQH/HĐND); ngày/tháng 1–2 có `0`.
- [ ] Tên loại IN HOA đậm 14; tên gọi đậm 13–14; đường kẻ 1/3–1/2.
- [ ] Căn cứ nghiêng 14, mỗi căn cứ một dòng, kết thúc `;`.
- [ ] Từ khoá QUYẾT NGHỊ/QUYẾT ĐỊNH/LỆNH (nếu có) IN HOA đậm 13, canh giữa, có `:`.
- [ ] Nội dung 13–14, canh đều, thụt 1–1,27 cm, cách đoạn ≥ 6 pt, giãn dòng 1–1,5.
- [ ] Chương/Phần số La Mã; Mục/Điều/Khoản số Ả Rập; Điểm chữ cái tiếng Việt + `)`.
- [ ] Chức vụ người ký IN HOA đậm 13, có TM./KT. đúng trường hợp; họ tên đậm 13–14 canh giữa chức vụ.
- [ ] `Nơi nhận:` nghiêng đậm 12, danh sách cỡ 11, `-` đầu dòng, `;` cuối dòng, dòng `Lưu:` kết thúc `.`.
- [ ] Số trang canh giữa lề trên, ẩn trang 1; phụ lục đánh số trang riêng.
- [ ] Phụ lục: được dẫn chiếu trong văn bản; ≥ 2 phụ lục đánh số La Mã; có thông tin chỉ dẫn nghiêng.

## Định dạng đầu ra

- **DOCX / PDF / HTML**: A4 dọc; lề theo mm; cỡ chữ theo pt; phần đầu (ô 1–4) và phần ký (ô 7–9) dùng bảng 2 cột
  không viền như mô tả ở mục 7 của `references/so-do-bo-tri.html`; số trang ở lề trên, ẩn trang 1.
- **Văn bản thuần** (chat): trình bày đúng thứ tự thành phần, ghi chú định dạng trong ngoặc vuông,
  ví dụ `[IN HOA, đậm, 13, canh giữa]`.
