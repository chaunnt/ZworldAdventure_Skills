# SKILL: the-thuc-van-ban

> Tệp này gộp toàn bộ skill thành một tài liệu duy nhất để dùng với ChatGPT, Gemini hoặc model bất kỳ.
> Hãy làm theo phần HƯỚNG DẪN CHÍNH; các phần TÀI LIỆU KÈM THEO là tài liệu tra cứu được nhắc tới trong hướng dẫn.
> Nguồn: https://github.com/chaunnt/ZworldAdventure_Skills/tree/main/skills/the-thuc-van-ban

**Mô tả / khi nào dùng:** Soạn thảo, định dạng và rà soát thể thức, kỹ thuật trình bày văn bản quy phạm pháp luật và văn bản hành chính Việt Nam (luật, nghị định, nghị quyết, thông tư, quyết định, lệnh, công văn...) theo Nghị định 78/2025/NĐ-CP. Dùng khi người dùng yêu cầu viết công văn, soạn văn bản nhà nước, trình bày Quốc hiệu - Tiêu ngữ, số ký hiệu, tên văn bản, căn cứ, điều khoản, chữ ký, nơi nhận, phụ lục, hoặc kiểm tra một văn bản có đúng thể thức không.

---

## HƯỚNG DẪN CHÍNH (SKILL.md)

# Thể thức, kỹ thuật trình bày văn bản (NĐ 78/2025/NĐ-CP)

Skill này giúp bạn (agent) **soạn mới** hoặc **rà soát** một văn bản sao cho đúng thể thức
và kỹ thuật trình bày theo Nghị định 78/2025/NĐ-CP.

## Tài liệu trong skill

| Tệp | Khi nào đọc |
|---|---|
| `SKILL.md` (tệp này) | Luôn đọc. Có quy trình, bảng tra nhanh, checklist. |
| `references/quy-dinh-chi-tiet.html` | Khi cần câu chữ đầy đủ của quy định (số ký hiệu từng loại văn bản, ký thay/thay mặt, địa danh, phụ lục, sửa đổi bổ sung). |
| `references/so-do-bo-tri.html` | Khi cần biết **vị trí** từng thành phần trên trang A4. Sơ đồ đã được mô tả hoàn toàn bằng lời + toạ độ phần trăm + JSON, không cần nhìn hình. |
| `assets/mau-van-ban-qppl.html` | Mẫu HTML5 khổ A4 cho văn bản QPPL (nghị định/quyết định/thông tư). Sao chép rồi điền nội dung. |
| `assets/mau-cong-van.html` | Mẫu HTML5 khổ A4 cho công văn hành chính. |

Các tệp `.html` là HTML5 thuần, đọc được như văn bản; nếu môi trường không mở được tệp phụ, mọi quy tắc
quan trọng nhất đã có trong bảng tra nhanh bên dưới.

## Phạm vi và lưu ý về nguồn

- Nguồn gốc của skill: Phụ lục về thể thức, kỹ thuật trình bày **văn bản quy phạm pháp luật (QPPL)**
  ban hành kèm NĐ 78/2025/NĐ-CP.
- **Công văn hành chính** (không phải văn bản QPPL) về pháp lý chịu sự điều chỉnh của
  **Nghị định 30/2020/NĐ-CP về công tác văn thư**. Bố cục trang (sơ đồ ô số 1–11), phông chữ, lề và
  phần lớn quy tắc về cơ bản giống nhau, nên skill vẫn áp dụng được; những điểm riêng của công văn
  (trích yếu "V/v", "Kính gửi") được ghi rõ là **ngoài tài liệu nguồn** — hãy nhắc người dùng đối chiếu
  NĐ 30/2020 nếu văn bản cần độ chính xác pháp lý.
- Khi quy định cho phép một khoảng (ví dụ cỡ chữ 13–14), hãy chọn **một giá trị và dùng thống nhất**
  trong toàn văn bản (mặc định đề xuất: nội dung 14, các thành phần khác theo bảng).
- Không bịa số hiệu, ngày ban hành, tên người ký, căn cứ pháp lý. Thiếu thông tin thì để chỗ trống
  dạng `[...]` và liệt kê cho người dùng điền.

## Quy trình làm việc

1. **Xác định loại văn bản** (luật, pháp lệnh, nghị quyết QH/UBTVQH/HĐND, nghị định, quyết định,
   thông tư, thông tư liên tịch, nghị quyết liên tịch, lệnh/quyết định Chủ tịch nước, công văn...).
   Loại văn bản quyết định: cấu trúc số ký hiệu, có/không có địa danh–ngày ở đầu, từ khoá
   "QUYẾT NGHỊ/QUYẾT ĐỊNH/LỆNH", cách ký (TM./KT.), vị trí chữ ký.
2. **Thu thập dữ liệu**: tên cơ quan ban hành, số thứ tự, năm, chữ viết tắt, địa danh, ngày ký,
   tên gọi (trích yếu), căn cứ, nội dung, người ký và chức vụ, nơi nhận, phụ lục.
3. **Dựng khung trang** theo `references/so-do-bo-tri.html` (A4 dọc, lề trái 30–35 mm, lề trên/dưới/phải 15–20 mm).
4. **Điền thành phần thể thức** theo bảng tra nhanh (cỡ chữ, kiểu chữ, căn lề, đường kẻ).
5. **Trình bày nội dung**: Phần/Chương/Mục/Điều/Khoản/Điểm đúng ký số (La Mã / Ả Rập / chữ cái tiếng Việt).
6. **Tự kiểm tra** bằng checklist cuối tệp, rồi trả kết quả (HTML theo mẫu, DOCX, hoặc văn bản thuần
   kèm chú thích định dạng — tuỳ người dùng yêu cầu).

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

## Công văn hành chính (bổ sung, ngoài tài liệu nguồn)

Áp dụng toàn bộ bố cục và định dạng ở trên, cộng thêm các điểm sau (theo thông lệ NĐ 30/2020/NĐ-CP —
cần đối chiếu khi yêu cầu độ chính xác pháp lý):

- Công văn **không có tên loại văn bản** (ô 5 trống); thay vào đó là **trích yếu** bắt đầu bằng `V/v` đặt canh giữa
  ngay dưới số ký hiệu (ô 3), chữ in thường, cỡ 12–13, đứng.
- Dưới phần đầu là dòng `Kính gửi:` (một nơi nhận thì cùng dòng; nhiều nơi thì liệt kê mỗi nơi một dòng có `-`).
- Ký hiệu công văn thường là `Số: [số]/[viết tắt cơ quan]-[viết tắt đơn vị soạn thảo]` (không có năm, không có tên loại).

## Định dạng đầu ra

- **HTML/PDF**: sao chép `assets/mau-van-ban-qppl.html` hoặc `assets/mau-cong-van.html`, thay các chỗ `[...]`.
  Mẫu đã có `@page` A4, lề, phông, đường kẻ, bảng hai cột phần đầu và khối chữ ký/nơi nhận; in ra PDF từ trình duyệt.
- **DOCX**: dùng cùng thông số (lề tính theo mm, cỡ chữ pt, bảng không viền 2 cột cho phần đầu và phần ký).
- **Văn bản thuần** (chat): trình bày theo đúng thứ tự thành phần và ghi chú định dạng trong ngoặc vuông,
  ví dụ `[IN HOA, đậm, 13, canh giữa]`.

---

## TÀI LIỆU KÈM THEO: `references/quy-dinh-chi-tiet.html`

Quy định thể thức chi tiết

# Thể thức, kỹ thuật trình bày văn bản quy phạm pháp luật

Viết lại có cấu trúc từ Phụ lục của Nghị định số 78/2025/NĐ-CP ngày 01/4/2025 của Chính phủ quy định chi tiết một số điều và biện pháp để tổ chức, hướng dẫn thi hành Luật Ban hành văn bản quy phạm pháp luật (bản đăng trên Báo điện tử Chính phủ ngày 09/04/2025). Nội dung giữ sát nguyên văn; các khối *thông số* là phần tóm tắt để tra cứu nhanh.

1. Quy định chung
2. Phần mở đầu, Quốc hiệu, Tiêu ngữ
3. Tên cơ quan ban hành
4. Số, ký hiệu
5. Tên văn bản
6. Điều khoản bổ sung
7. Địa danh, ngày tháng năm
8. Ký văn bản
9. Dấu và nơi nhận
10. Căn cứ ban hành
11. Nội dung văn bản
12. Phụ lục
13. Sơ đồ bố trí (tệp riêng)

## I. Quy định chung

1. Văn bản được trình bày trên trang giấy khổ **A4 (210 mm × 297 mm)**.
2. Kiểu trình bày: theo **chiều dài** của khổ A4. Phần phụ lục có bảng, biểu thì có thể trình bày theo chiều rộng.
3. Định lề trang: cách mép trên, mép dưới và mép phải **15–20 mm**; cách mép trái **30–35 mm**.
4. Phông chữ: phông chữ tiếng Việt, kiểu chữ **Times New Roman**, bộ mã ký tự Unicode theo TCVN 6909:2001, **màu đen**.
5. Cỡ chữ và kiểu chữ: theo quy định cụ thể cho từng thành phần thể thức (các mục II, III dưới đây).
6. Vị trí trình bày các thành phần thể thức: theo sơ đồ bố trí.
7. Trang được đánh số thứ tự bằng **số Ả Rập, cỡ chữ 13, kiểu chữ đứng**, **không hiển thị số trang thứ nhất**, đặt **canh giữa theo chiều ngang trong phần lề trên**. Số trang của văn bản ban hành kèm theo được đánh số riêng cho từng văn bản. Số trang của Phụ lục được đánh số riêng theo từng Phụ lục.

## II. Các thành phần thể thức chính

### 1. Phần mở đầu, Quốc hiệu và Tiêu ngữ

a) Phần mở đầu của văn bản QPPL gồm: Quốc hiệu; Tiêu ngữ; tên cơ quan, người có thẩm quyền ban hành; số, ký hiệu; tên văn bản; căn cứ ban hành.

b) Phần mở đầu của văn bản *được ban hành kèm theo* văn bản khác (quy chế, quy định) gồm: Quốc hiệu; Tiêu ngữ; tên cơ quan, người có thẩm quyền ban hành; tên văn bản. Dưới tên văn bản được ban hành kèm theo phải ghi rõ tên, số, ký hiệu và ngày, tháng, năm ban hành của văn bản ban hành kèm theo.

c) Quốc hiệu `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM`:

- **Chữ**: IN HOA
- **Cỡ**: 12–13
- **Kiểu**: đứng, đậm
- **Vị trí**: phía trên cùng, bên phải trang đầu tiên

d) Tiêu ngữ `Độc lập - Tự do - Hạnh phúc`:

- **Chữ**: in thường; chữ cái đầu các cụm từ viết hoa; giữa các cụm có gạch nối (-), có cách chữ
- **Cỡ**: 13–14
- **Kiểu**: đứng, đậm
- **Vị trí**: canh giữa, liền phía dưới Quốc hiệu
- **Đường kẻ**: phía dưới có đường kẻ ngang, nét liền, độ dài bằng độ dài dòng chữ

### 2. Tên cơ quan, người có thẩm quyền ban hành

a) Là tên chính thức, đầy đủ của cơ quan hoặc chức danh nhà nước của người có thẩm quyền ban hành theo Luật Ban hành văn bản QPPL.

- **Chữ**: IN HOA, trên **một dòng**
- **Cỡ**: 12–13
- **Kiểu**: đứng, đậm
- **Vị trí**: đặt cân đối ở phía trên cùng, bên trái trang đầu tiên
- **Đường kẻ**: phía dưới, nét liền, dài 1/3–1/2 dòng chữ, đặt ở giữa, cân đối so với dòng chữ

Đối với lệnh, quyết định của Chủ tịch nước: phía trên chức danh Chủ tịch nước trình bày hình **Quốc huy**.

### 3. Số, ký hiệu

a) Luật, nghị quyết của Quốc hội, pháp lệnh, nghị quyết của UBTVQH: loại văn bản, số thứ tự, năm ban hành, tên viết tắt cơ quan ban hành và **số khóa Quốc hội**.

b) Nghị quyết liên tịch, thông tư liên tịch: số thứ tự, năm ban hành, tên viết tắt loại văn bản, tên viết tắt các cơ quan cùng ban hành.

- NQ liên tịch giữa UBTVQH với Đoàn Chủ tịch UBTW MTTQ Việt Nam; NQ liên tịch giữa UBTVQH, Chính phủ với Đoàn Chủ tịch UBTW MTTQ Việt Nam: đánh số theo hệ thống quản lý văn bản QPPL của **UBTVQH**.
- NQ liên tịch giữa Chính phủ với Đoàn Chủ tịch UBTW MTTQ Việt Nam: đánh số theo hệ thống của **Chính phủ**.

c) Lệnh, quyết định của Chủ tịch nước: số thứ tự, năm ban hành, tên viết tắt loại văn bản, chữ viết tắt chức danh nhà nước của người có thẩm quyền.

d) Văn bản QPPL khác: số thứ tự, năm ban hành, tên viết tắt loại văn bản, chữ viết tắt cơ quan ban hành hoặc chức danh nhà nước của người có thẩm quyền.

đ) Kỹ thuật trình bày:

- Đặt **canh giữa dưới tên cơ quan** (hoặc chức danh) ban hành. Các ký tự trình bày **liền nhau, không cách chữ**.
- Ký hiệu gồm chữ viết tắt tên loại văn bản và chữ viết tắt tên cơ quan/chức danh (quy định cụ thể, ngắn gọn, dễ hiểu). Trình bày **IN HOA, cỡ 13, đứng**. Giữa số và ký hiệu có `/`; giữa các nhóm chữ viết tắt có `-`, không cách chữ.
- Số ghi bằng chữ số Ả Rập, gồm số thứ tự đăng ký theo từng loại văn bản do cơ quan ban hành trong một năm và năm ban hành; bắt đầu liên tiếp từ số `01` ngày 01 tháng 01, kết thúc ngày 31 tháng 12 hằng năm; năm ghi đầy đủ các số.
- Từ `Số`: in thường, cỡ 13, đứng, sau có dấu hai chấm `:`; số nhỏ hơn 10 ghi thêm `0` phía trước.
- Số khóa Quốc hội thể hiện bằng số La Mã. Giữa số, năm ban hành và ký hiệu có `/`; giữa các nhóm chữ viết tắt trong ký hiệu văn bản của Chủ tịch nước, nghị quyết liên tịch có `-`, không cách chữ.

Ví dụ: `Số: 78/2025/NĐ-CP` (nghị định thứ 78 năm 2025 của Chính phủ).

### 4. Tên văn bản

a) Tên **luật, pháp lệnh**: IN HOA, cỡ 14, đứng, đậm, canh giữa; tên loại văn bản và tên gọi trình bày trên các dòng riêng.

b) Văn bản khác:

- Tên loại văn bản: IN HOA, cỡ 14, đứng, đậm, canh giữa.
- Tên gọi văn bản: in thường, cỡ 13–14, đứng, đậm; đặt dưới tên loại, canh giữa.
- Dưới tên gọi có đường kẻ ngang, nét liền, dài 1/3–1/2 dòng chữ, đặt ở giữa.

c) Văn bản được ban hành kèm theo: nội dung chú thích về việc ban hành kèm theo đặt trong **ngoặc đơn**, in thường, cỡ 13–14, **nghiêng**, canh giữa, liền dưới tên văn bản; dưới có đường kẻ ngang nét liền dài 1/3–1/2 dòng chữ, đặt ở giữa.

### 5. Đánh số điều khoản bổ sung trong văn bản sửa đổi, bổ sung

Căn cứ nội dung bổ sung để xác định vị trí của điều khoản bổ sung. Số thứ tự của phần, chương, mục, tiểu mục, điều, khoản được bổ sung gồm **phần số** (theo số thứ tự trong văn bản được sửa đổi) và **phần chữ** (theo bảng chữ cái tiếng Việt, đặt sau số chỉ điều, khoản đứng liền trước). Ví dụ: bổ sung sau Điều 5 → `Điều 5a`, `Điều 5b`; bổ sung sau khoản 2 → `khoản 2a`.

### 6. Địa danh, ngày tháng năm ban hành

a) Địa danh:

- Cơ quan nhà nước ở trung ương (nếu có): tên tỉnh, thành phố trực thuộc trung ương nơi cơ quan đóng trụ sở.
- Cơ quan nhà nước ở địa phương: tên gọi chính thức của đơn vị hành chính của cơ quan ban hành.
- Đơn vị hành chính đặt theo tên người, bằng chữ số hoặc sự kiện lịch sử: ghi tên gọi đầy đủ.
- Trừ văn bản của Quốc hội, UBTVQH, HĐND: địa danh và ngày tháng năm trình bày **cùng một dòng với số, ký hiệu**, in thường, cỡ 13–14, **nghiêng**; sau địa danh có dấu phẩy; đặt phía dưới, ở giữa, cân đối với Quốc hiệu và Tiêu ngữ.

b) Ngày tháng năm ban hành là ngày văn bản được thông qua hoặc ký ban hành. Phải viết đầy đủ; dùng số Ả Rập; số nhỏ hơn 10 và các tháng 1, 2 thêm `0` phía trước. Ví dụ: `Hà Nội, ngày 05 tháng 02 năm 2025`; `Hà Nội, ngày 01 tháng 4 năm 2025`.

c) Thông tin về thời điểm Quốc hội thông qua luật, nghị quyết; HĐND thông qua nghị quyết: in thường, cỡ 13–14, nghiêng, đặt phía dưới điều cuối cùng. Số khóa Quốc hội, HĐND dùng số La Mã; số kỳ họp dùng số Ả Rập, trừ kỳ họp thứ nhất. Điều cuối cùng của luật, nghị quyết của Quốc hội và thông tin thời điểm thông qua được phân cách bằng **đường kẻ ngang liền từ lề trái đến lề phải**.

### 7. Ký văn bản

a) Chức vụ của người có thẩm quyền ký theo quy định của pháp luật và phải thể hiện đầy đủ.

- Luật, nghị quyết của Quốc hội: chức vụ người ký chứng thực đặt cân đối bên phải, dưới phần thông tin thời điểm thông qua.
- Pháp lệnh, NQ UBTVQH, quyết định Chủ tịch nước: bên phải, dưới điều cuối cùng. Lệnh Chủ tịch nước: dưới nội dung cuối cùng của lệnh.
- Nghị quyết liên tịch: dưới điều cuối cùng, theo chiều ngang, đặt cân đối đều hai bên trang.
- Nghị định, NQ Chính phủ, NQ Hội đồng Thẩm phán TANDTC, quyết định UBND: bên phải, dưới điều cuối cùng.
- Thủ tướng thay mặt Chính phủ; Chánh án TANDTC thay mặt Hội đồng Thẩm phán; Chủ tịch UBND thay mặt UBND ký, ghi `TM.` trước "Chính phủ", "Hội đồng Thẩm phán", "Ủy ban nhân dân". Cấp phó ký thay thì ghi `KT.` trước chức vụ của người có thẩm quyền.
- Nghị quyết liên tịch: ghi rõ tên cơ quan và chức vụ người ký. Chủ tịch Quốc hội thay mặt UBTVQH, Thủ tướng thay mặt Chính phủ, Chủ tịch UBTW MTTQ thay mặt Đoàn Chủ tịch ký, ghi `TM.` trước tên tập thể.
- QĐ Thủ tướng; thông tư của Bộ trưởng, Thủ trưởng cơ quan ngang bộ, Chánh án TANDTC, Viện trưởng VKSNDTC, Tổng KTNN: ghi chức vụ người ký; cấp phó ký thay ghi `KT.`.
- Thông tư liên tịch: các người đứng đầu cùng ký; cơ quan **chủ trì bên phải**, cơ quan cùng ký bên trái.
- Nghị quyết HĐND: Chủ tịch HĐND ký chứng thực.

b) Chức vụ người ký: IN HOA, cỡ 13, đứng, đậm. Các chữ `TM.`, `KT.`, `Q.` hoặc quyền hạn và chức vụ: IN HOA, cỡ 13, đứng, đậm.

c) Họ và tên người ký: in thường, cỡ 13–14, đứng, đậm, đặt ở giữa, cân đối so với quyền hạn, chức vụ.

### 8. Dấu và nơi nhận

a) Dấu đóng sau khi người có thẩm quyền ký, theo pháp luật về công tác văn thư. Văn bản có nội dung bí mật nhà nước: xác định và đóng dấu mức độ mật theo pháp luật bảo vệ bí mật nhà nước.

b) Tùy nội dung, nơi nhận có thể gồm: cơ quan giám sát, kiểm tra việc thi hành; cơ quan công báo; cơ quan trực tiếp chịu trách nhiệm thi hành; cơ quan, tổ chức, cá nhân khác có liên quan; đơn vị lưu văn bản và đơn vị soạn thảo.

c) Trình bày:

- Từ `Nơi nhận`: dòng riêng, ngang hàng dòng "quyền hạn, chức vụ của người ký", sát lề trái, sau có `:`; in thường, **cỡ 12, nghiêng, đậm**.
- Danh sách: in thường, **cỡ 11, đứng**; mỗi cơ quan/nhóm một dòng, đầu dòng gạch `-` sát lề trái, cuối dòng `;`.
- Dòng cuối: `Lưu` + `:` + `VT` + `,` + chữ viết tắt đơn vị soạn thảo + số lượng bản lưu, kết thúc bằng `.`.

## III. Phần nội dung văn bản

### 1. Căn cứ ban hành

In thường, **cỡ 14, nghiêng**, dưới tên văn bản; sau mỗi căn cứ xuống dòng, cuối dòng có `;`.

- a) Luật, pháp lệnh, nghị quyết liên tịch: dưới căn cứ trình bày "tên cơ quan (các cơ quan) + *ban hành* + tên văn bản", in thường, cỡ 13–14, nghiêng, kết thúc bằng dấu chấm.
- b) Nghị quyết Quốc hội, NQ UBTVQH: căn cứ trình bày dưới tên cơ quan ban hành; dưới căn cứ là `QUYẾT NGHỊ:` – IN HOA, cỡ 13, đứng, đậm, dòng riêng, canh giữa.
- c) Lệnh, quyết định Chủ tịch nước: căn cứ dưới tên cơ quan ban hành; dưới căn cứ là `LỆNH:` hoặc `NAY…` (với lệnh), `QUYẾT ĐỊNH:` (với quyết định) – IN HOA, cỡ 13, đứng, đậm, dòng riêng, có `:`, canh giữa.

### 2. Trình bày nội dung

- **Chữ**: in thường
- **Cỡ**: 13–14
- **Kiểu**: đứng
- **Căn lề**: dàn đều hai lề
- **Thụt đầu dòng**: 1 cm đến 1,27 cm
- **Cách đoạn**: tối thiểu 6 pt
- **Giãn dòng**: từ đơn (single) đến tối đa 1,5 lines

- `Phần`, `Chương` + số thứ tự (**La Mã**): in thường, cỡ 13–14, đứng, đậm, dòng riêng, canh giữa. Tên phần/chương ở dưới: **IN HOA, cỡ 14**, đứng, đậm, canh giữa.
- `Mục`, `Tiểu mục` + số thứ tự (**Ả Rập**): in thường, cỡ 13–14, đứng, đậm, dòng riêng, canh giữa. Tên mục/tiểu mục ở dưới: IN HOA, cỡ 13–14, đứng, đậm, canh giữa.
- `Điều` + số thứ tự (Ả Rập, sau có dấu chấm) + tên điều: in thường, cỡ 13–14, đứng, đậm, cách lề trái 1–1,27 cm.
- Khoản: số Ả Rập + dấu chấm, cỡ 13–14, đứng. Khoản có tên: số và tên trên một dòng riêng, in thường, cỡ 13–14, đứng.
- Điểm: chữ cái tiếng Việt theo thứ tự bảng chữ cái + `)`, in thường, cỡ 13–14, đứng.

### 3. Phụ lục

- a) Văn bản có Phụ lục thì trong văn bản phải chỉ dẫn về Phụ lục. Từ hai Phụ lục trở lên: đánh số bằng **số La Mã**.
- b) `Phụ lục` + số thứ tự: dòng riêng, canh giữa, in thường, cỡ 13–14, đứng, đậm. Tên Phụ lục (nếu có): canh giữa, IN HOA, cỡ 13–14, đứng, đậm.
- c) Thông tin chỉ dẫn trên mỗi Phụ lục gồm: số, ký hiệu văn bản, thời gian ban hành và tên cơ quan ban hành. Canh giữa dưới tên Phụ lục, in thường, cỡ 13–14, **nghiêng**, cùng phông với nội dung.

---

## TÀI LIỆU KÈM THEO: `references/so-do-bo-tri.html`

Sơ đồ bố trí thành phần thể thức

# Sơ đồ bố trí các thành phần thể thức văn bản

Trên một trang giấy khổ A4 (210 mm × 297 mm). Nguồn: Phần IV Phụ lục thể thức, kỹ thuật trình bày văn bản QPPL – Nghị định 78/2025/NĐ-CP. Bản gốc là một hình vẽ; tài liệu này chuyển toàn bộ hình vẽ thành lời, bảng toạ độ và JSON để AI agent hiểu được mà không cần xem ảnh.

## 1. Chú giải ô số (giữ nguyên theo bản gốc)

| Ô số | Thành phần thể thức văn bản |
|---|---|
| 1 | Quốc hiệu và Tiêu ngữ |
| 2 | Tên cơ quan, tổ chức ban hành văn bản |
| 3 | Số, ký hiệu của văn bản |
| 4 | Địa danh và ngày, tháng, năm ban hành văn bản |
| 5 | Tên văn bản |
| 6 | Nội dung văn bản |
| 7a, 7b, 7c | Chức vụ (7a), họ và tên (7b) và chữ ký (7c) của người có thẩm quyền |
| 8 | Dấu của cơ quan, tổ chức |
| 9 | Nơi nhận |
| 10 | Dấu chỉ mức độ mật |
| 11 | Ký hiệu người đánh máy và số lượng bản phát hành |

## 2. Khung trang và lề

Trang A4 đặt **dọc**. Vùng trình bày (vùng có chữ) là một hình chữ nhật nằm bên trong trang, cách các mép giấy:

- **Mép trái: 30–35 mm** (lề rộng nhất, để đóng quyển). Trên hình có mũi tên ngang ở giữa chiều cao trang, ghi "30-35 mm".
- **Mép phải: 15–20 mm**. Trên hình có mũi tên ngang bên phải, chữ "15-20 mm" viết dọc.
- **Mép trên và mép dưới:** lời văn của Nghị định (Mục I.3) quy định **15–20 mm**.

**Chênh lệch cần biết:** trên hình vẽ gốc, mũi tên ở mép trên và mép dưới ghi **"20-25 mm"**, khác với lời văn (15–20 mm). Khi soạn văn bản QPPL theo NĐ 78/2025, **ưu tiên lời văn: 15–20 mm**. Nếu người dùng soạn công văn hành chính theo NĐ 30/2020, lề trên/dưới 20–25 mm là phổ biến — hãy hỏi lại nếu không rõ.

## 3. Mô tả sơ đồ bằng lời (đọc từ trên xuống dưới)

Hãy hình dung vùng trình bày chia làm **hai cột phần đầu** (trái và phải), một **thân văn bản rộng toàn bộ**, và **hai cột phần cuối** (nơi nhận bên trái, chữ ký bên phải). Cụ thể:

1. **Hàng 1 – sát mép trên vùng trình bày**:
  - Bên **trái**: **ô 2 – Tên cơ quan ban hành**. Ô bắt đầu sát lề trái, rộng khoảng 1/3 vùng trình bày.
  - Bên **phải**: **ô 1 – Quốc hiệu** (và Tiêu ngữ ngay dưới). Ô kết thúc sát lề phải, rộng khoảng 2/5 vùng trình bày.
  - Ô 2 và ô 1 nằm **ngang hàng nhau** (cùng dòng trên cùng). Khoảng giữa hai ô để trống.

2. **Hàng 2 – ngay dưới hàng 1**:
  - Bên trái, thẳng cột dưới ô 2: **ô 3 – Số, ký hiệu** (cùng độ rộng và cùng trục giữa với ô 2).
  - Bên phải, thẳng cột dưới ô 1: **ô 4 – Địa danh, ngày tháng năm** (cùng độ rộng và trục giữa với ô 1).
  - Ô 3 và ô 4 **cùng một dòng** — đúng quy tắc "địa danh, ngày tháng năm trình bày trên cùng một dòng với số, ký hiệu".

3. **Hàng 3**: **ô 5 – Tên văn bản**, nằm **giữa trang theo chiều ngang**, rộng khoảng 2/5 vùng trình bày, dưới hàng 2.
4. **Hàng 4**: **ô 10 – Dấu chỉ mức độ mật**, sát lề **trái**, nhỏ (khoảng 1/5 vùng trình bày), dưới ô 5 và trên thân văn bản. Ô này chỉ xuất hiện khi văn bản có độ mật.
5. **Khoảng trống** giữa ô 10 và thân văn bản: nơi trình bày căn cứ ban hành và các dòng như "QUYẾT ĐỊNH:" (thuộc phần mở đầu/nội dung).
6. **Thân văn bản – ô 6 – Nội dung**: một khối chữ nhật lớn **chiếm toàn bộ chiều rộng** vùng trình bày (từ lề trái đến lề phải), nằm khoảng giữa trang theo chiều dọc (trên hình chiếm khoảng 1/3 chiều cao). Trong thực tế ô 6 dài theo độ dài nội dung và có thể sang nhiều trang.
7. **Phần cuối – dưới ô 6**, chia hai bên:
  - **Bên trái – ô 9 – Nơi nhận**: khối sát lề trái, rộng khoảng 1/4 vùng trình bày. Đỉnh ô 9 **ngang hàng với ô 7a** (dòng "Nơi nhận:" ngang hàng dòng chức vụ người ký). Ô 9 có hình chữ L: góc **dưới bên phải** của nó bị khuyết để đặt **ô 11 – Ký hiệu người đánh máy, số lượng bản phát hành** (ô nhỏ nằm ở góc dưới phải khối nơi nhận).
  - **Bên phải – khối chữ ký**, từ khoảng giữa trang đến lề phải, xếp dọc từ trên xuống:
    1. **ô 7a – Quyền hạn, chức vụ người ký** (vd "TM. CHÍNH PHỦ / THỦ TƯỚNG"): ô rộng, trên cùng.
    2. **ô 7c – Chữ ký**: ô nhỏ ở giữa, hơi lệch phải, ngay dưới 7a.
    3. **ô 8 – Dấu**: hình **tròn** nằm bên trái ô 7c và **chồng lên phần bên trái của chữ ký 7c**.
    4. **ô 7b – Họ và tên người ký**: ô rộng ở dưới cùng, dưới chữ ký và dấu, cùng trục giữa với 7a.

8. Dưới khối chữ ký là khoảng trống tới lề dưới.

## 4. Hình minh hoạ dựng lại bằng HTML/CSS

Tỷ lệ dựng theo hình gốc, chỉ để minh hoạ vị trí tương đối – không phải kích thước in chính xác.

[Hình: Trang A4 dọc. Hàng trên: ô 2 bên trái, ô 1 bên phải. Hàng hai: ô 3 trái, ô 4 phải. Ô 5 giữa. Ô 10 trái. Ô 6 rộng toàn trang ở giữa. Dưới: ô 9 trái có ô 11 ở góc dưới phải; bên phải xếp dọc 7a, 7c có dấu tròn 8 chồng bên trái, rồi 7b.]

Biểu diễn ASCII tương đương (trái → phải là lề trái → lề phải):

```

+------------------------------------------------------------+
|        lề trên (15–20 mm theo lời văn; hình ghi 20–25)     |
|   +--------+                         +----------------+    |
|   |   2    |                         | 1. Quốc hiệu   |    |
|   +--------+                         +----------------+    |
|   |   3    |                         |       4        |    |
|   +--------+     +-------------+     +----------------+    |
|                  |      5      |                           |
|   +----+         +-------------+                           |
|30 | 10 |                                                15 |
|-  +----+                                                -  |
|35   (căn cứ ban hành, QUYẾT ĐỊNH: ...)                  20 |
|mm +---------------------------------------------------+ mm |
|   |                         6                         |    |
|   |                (nội dung văn bản)                 |    |
|   +---------------------------------------------------+    |
|   +-------+               +----------------------+         |
|   |   9   |               |          7a          |         |
|   |       |          ( 8 )+------+                         |
|   |   +---+          (dấu)|  7c  |                         |
|   |   |11 |               +------+                         |
|   +---+---+              +--------------------+            |
|                          |         7b         |            |
|                          +--------------------+            |
|        lề dưới (15–20 mm theo lời văn; hình ghi 20–25)     |
+------------------------------------------------------------+

```

## 5. Bảng toạ độ tương đối

Đơn vị: phần trăm của **vùng trình bày** (không tính lề). `x` tính từ lề trái, `y` tính từ lề trên. Số liệu đo trên hình gốc, sai số khoảng ±2%.

| Ô | x từ | x đến | y từ | y đến | Căn lề chữ trong ô | Neo / quan hệ |
|---|---|---|---|---|---|---|
| 2 | 0 | 32 | 0 | 4 | giữa | Ngang hàng ô 1 |
| 1 | 57 | 98 | 0 | 4 | giữa | Sát lề phải |
| 3 | 0 | 32 | 6 | 11 | giữa | Dưới ô 2, cùng trục giữa |
| 4 | 57 | 98 | 6 | 11 | giữa | Dưới ô 1, cùng dòng ô 3 |
| 5 | 36 | 74 | 13 | 17 | giữa | Giữa trang |
| 10 | 0 | 18 | 19 | 24 | trái | Dưới ô 5, sát lề trái |
| 6 | 0 | 100 | 34 | 66 | đều hai lề | Toàn chiều rộng; cao theo nội dung |
| 9 | 0 | 24 | 70 | 84 | trái | Đỉnh ngang hàng ô 7a |
| 11 | 16 | 24 | 79 | 84 | trái | Góc dưới phải của ô 9 |
| 7a | 49 | 98 | 69 | 74 | giữa | Dưới ô 6, bên phải |
| 7c | 71 | 88 | 78 | 83 | giữa | Dưới 7a |
| 8 | 59 | 75 | 75 | 86 | — | Hình tròn, chồng phần trái của 7c |
| 7b | 52 | 96 | 86 | 91 | giữa | Dưới 7c và 8, cùng trục giữa 7a |

## 6. Dữ liệu máy đọc (JSON)

Agent có thể dùng khối JSON sau để dựng bố cục (DOCX, PDF, HTML) một cách chương trình hoá.

```json

{
"page": { "size": "A4", "width_mm": 210, "height_mm": 297, "orientation": "portrait",
"orientation_appendix_tables": "landscape allowed" },
"margins_mm": { "left": [30, 35], "right": [15, 20], "top": [15, 20], "bottom": [15, 20],
"note": "Hinh goc ghi top/bottom 20-25 mm; loi van ND 78/2025 quy dinh 15-20 mm (uu tien loi van)." },
"font": { "family": "Times New Roman", "encoding": "Unicode TCVN 6909:2001", "color": "#000000" },
"page_number": { "position": "top-center", "size_pt": 13, "style": "regular", "hide_on_first_page": true },
"units": "percent of text area; x from left margin, y from top margin",
"blocks": [
{ "id": "2",  "name": "Ten co quan ban hanh",        "x": [0, 32],  "y": [0, 4],   "align": "center", "row": "header-1", "side": "left" },
{ "id": "1",  "name": "Quoc hieu va Tieu ngu",        "x": [57, 98], "y": [0, 4],   "align": "center", "row": "header-1", "side": "right" },
{ "id": "3",  "name": "So, ky hieu",                  "x": [0, 32],  "y": [6, 11],  "align": "center", "row": "header-2", "side": "left",  "below": "2" },
{ "id": "4",  "name": "Dia danh, ngay thang nam",     "x": [57, 98], "y": [6, 11],  "align": "center", "row": "header-2", "side": "right", "below": "1", "same_line_as": "3" },
{ "id": "5",  "name": "Ten van ban",                  "x": [36, 74], "y": [13, 17], "align": "center", "below": ["3", "4"] },
{ "id": "10", "name": "Dau chi muc do mat",           "x": [0, 18],  "y": [19, 24], "align": "left", "below": "5", "optional": true },
{ "id": "6",  "name": "Noi dung van ban",             "x": [0, 100], "y": [34, 66], "align": "justify", "height": "grows with content" },
{ "id": "9",  "name": "Noi nhan",                     "x": [0, 24],  "y": [70, 84], "align": "left", "top_aligned_with": "7a", "shape": "L, bottom-right corner cut out for 11" },
{ "id": "11", "name": "Ky hieu nguoi danh may, so luong ban", "x": [16, 24], "y": [79, 84], "align": "left", "inside_corner_of": "9" },
{ "id": "7a", "name": "Quyen han, chuc vu nguoi ky",  "x": [49, 98], "y": [69, 74], "align": "center", "below": "6", "side": "right" },
{ "id": "7c", "name": "Chu ky",                       "x": [71, 88], "y": [78, 83], "align": "center", "below": "7a" },
{ "id": "8",  "name": "Dau co quan",                  "x": [59, 75], "y": [75, 86], "shape": "circle", "overlaps": "left part of 7c" },
{ "id": "7b", "name": "Ho va ten nguoi ky",           "x": [52, 96], "y": [86, 91], "align": "center", "below": ["7c", "8"], "centered_with": "7a" }
],
"reading_order": ["2", "1", "3", "4", "5", "10", "6", "9", "11", "7a", "7c", "8", "7b"]
}

```

```

```

``

## 7. Cách áp dụng khi dựng văn bản thật

- **Phần đầu** (ô 1–4): dùng một bảng 2 cột không viền. Cột trái ~40% (ô 2 rồi ô 3), cột phải ~60% (ô 1, Tiêu ngữ, rồi ô 4). Mỗi ô canh giữa trong cột của nó. Hình gốc vẽ cột trái hẹp hơn, nhưng thực tế Quốc hiệu dài nên cột phải cần rộng hơn.
- **Ô 5**: các đoạn canh giữa toàn trang, sau bảng phần đầu.
- **Ô 6**: các đoạn thông thường, canh đều hai lề, thụt đầu dòng 1–1,27 cm.
- **Phần cuối** (ô 7–9, 11): bảng 2 cột không viền. Cột trái ~45% chứa "Nơi nhận:" và danh sách (cỡ 11–12) ở dòng đầu ngang hàng dòng chức vụ; cột phải ~55% chứa 7a (IN HOA đậm), khoảng trống cho chữ ký + dấu (~25–30 mm), rồi 7b (đậm), tất cả canh giữa trong cột.
- **Ô 10**: chỉ chèn khi văn bản có độ mật. **Ô 11**: tuỳ cơ quan, đặt ở cuối khối nơi nhận.

---

## TÀI LIỆU KÈM THEO: `assets/mau-cong-van.html`

(Tệp mẫu — sao chép nguyên văn khi tạo đầu ra.)

````html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mẫu công văn</title>
<!--
  MẪU CÔNG VĂN HÀNH CHÍNH – bố cục/định dạng theo NĐ 78/2025/NĐ-CP; các điểm riêng của công văn
  ("V/v", "Kính gửi", ký hiệu không có năm) theo thông lệ NĐ 30/2020/NĐ-CP – cần đối chiếu khi cần chính xác pháp lý.
  Cách dùng (cho agent):
    1. Sao chép tệp, thay mọi chỗ [ ... ] bằng dữ liệu thật; xoá khối không dùng.
    2. Giữ nguyên CSS. Mở bằng trình duyệt → In → Lưu PDF (khổ A4, lề "Mặc định"/"Không" vì lề đã đặt trong @page).
    3. Công văn không có tên loại văn bản (ô 5); trích yếu "V/v" nằm dưới số ký hiệu.
  Ánh xạ ô số trên sơ đồ: data-o="1".."11".
-->
<style>
  @page {
    size: A4 portrait;
    margin: 20mm 20mm 20mm 30mm;            /* trên phải dưới trái: 15–20 / 15–20 / 15–20 / 30–35 mm */
    @top-center { content: counter(page); font: 13pt "Times New Roman", serif; }
  }
  @page :first { @top-center { content: none; } }   /* không hiện số trang 1 */

  html { background: #e9ecef; }
  body {
    font-family: "Times New Roman", Times, serif; color: #000; background: #fff;
    font-size: 14pt; line-height: 1.3;
    width: 210mm; min-height: 297mm; margin: 0 auto; padding: 20mm 20mm 20mm 30mm; box-sizing: border-box;
  }
  @media print { html { background: none; } body { width: auto; min-height: 0; padding: 0; margin: 0; } }
  @media screen and (max-width: 820px) { body { width: 100%; padding: 16px; } }

  p { margin: 0; }
  .center { text-align: center; }
  .b { font-weight: bold; } .i { font-style: italic; } .up { text-transform: none; }
  .rule-full  { display: block; height: 0; border-top: 1px solid #000; margin: 2px auto 0; }
  .rule-third { display: block; height: 0; border-top: 1px solid #000; width: 40%; margin: 2px auto 0; } /* 1/3–1/2 dòng chữ */

  /* Phần đầu: bảng 2 cột không viền */
  table.head, table.sign { width: 100%; border-collapse: collapse; }
  table.head td, table.sign td { vertical-align: top; padding: 0; }
  .col-left  { width: 40%; text-align: center; }
  .col-right { width: 60%; text-align: center; }
  .co-quan   { font-size: 13pt; font-weight: bold; white-space: nowrap; }                 /* ô 2 */
  .quoc-hieu { font-size: 13pt; font-weight: bold; white-space: nowrap; }                 /* ô 1 */
  .tieu-ngu  { font-size: 14pt; font-weight: bold; display: inline-block; }               /* ô 1 */
  .tieu-ngu-rule { border-top: 1px solid #000; }                                          /* dài bằng dòng chữ */
  .so-ky-hieu { font-size: 13pt; margin-top: 6pt; }                                       /* ô 3 */
  .dia-danh   { font-size: 14pt; font-style: italic; margin-top: 6pt; }                   /* ô 4 */
  .mat        { font-size: 13pt; font-weight: bold; margin-top: 6pt; }                    /* ô 10 */

  .ten-loai   { font-size: 14pt; font-weight: bold; text-align: center; margin-top: 18pt; } /* ô 5 */
  .ten-goi    { font-size: 14pt; font-weight: bold; text-align: center; }
  .can-cu     { font-size: 14pt; font-style: italic; text-indent: 1.27cm; text-align: justify; margin-top: 6pt; }
  .tu-khoa    { font-size: 13pt; font-weight: bold; text-align: center; margin: 12pt 0 6pt; } /* QUYẾT NGHỊ: / QUYẾT ĐỊNH: */

  /* Ô 6 – nội dung */
  .noi-dung p { text-align: justify; text-indent: 1.27cm; margin-top: 6pt; line-height: 1.3; }
  .noi-dung p.chuong, .noi-dung p.ten-chuong { text-align: center; text-indent: 0; }
  .chuong     { font-weight: bold; text-align: center; margin-top: 12pt; }
  .ten-chuong { font-weight: bold; text-align: center; font-size: 14pt; }
  .noi-dung p.dieu { font-weight: bold; }

  /* Phần cuối: nơi nhận trái, chữ ký phải */
  table.sign { margin-top: 12pt; }
  .noi-nhan-col { width: 45%; text-align: left; }
  .ky-col { width: 55%; text-align: center; }
  .noi-nhan-tieu-de { font-size: 12pt; font-weight: bold; font-style: italic; }       /* ô 9 */
  .noi-nhan { font-size: 11pt; line-height: 1.2; }
  .chuc-vu { font-size: 13pt; font-weight: bold; }                                     /* ô 7a */
  .cho-ky  { height: 28mm; }                                                           /* ô 7c + ô 8 */
  .ho-ten  { font-size: 14pt; font-weight: bold; }                                     /* ô 7b */
  .danh-may { font-size: 11pt; }                                                       /* ô 11 */
  .trich-yeu { font-size: 12pt; margin-top: 2pt; }                                      /* trích yếu V/v */
  .kinh-gui  { font-size: 14pt; text-align: center; margin: 18pt 0 6pt; }
  .kinh-gui-list { display: inline-block; text-align: left; }
</style>
</head>
<body>

<!-- PHẦN ĐẦU: ô 2, 3 + trích yếu (trái) | ô 1, 4 (phải) -->
<table class="head">
  <tr>
    <td class="col-left">
      <p class="co-quan" style="font-weight:normal">[CƠ QUAN CHỦ QUẢN]</p>
      <p class="co-quan" data-o="2">[TÊN CƠ QUAN BAN HÀNH]</p>
      <span class="rule-third"></span>
      <p class="so-ky-hieu" data-o="3">Số: [123]/[CQ]-[ĐV]</p>
      <p class="trich-yeu">V/v [trích yếu nội dung công văn]</p>
      <!-- ô 10 (chỉ khi có độ mật): <p class="mat" data-o="10">[MẬT]</p> -->
    </td>
    <td class="col-right">
      <p class="quoc-hieu" data-o="1">CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</p>
      <p><span class="tieu-ngu">Độc lập - Tự do - Hạnh phúc<span class="rule-full tieu-ngu-rule"></span></span></p>
      <p class="dia-danh" data-o="4">[Hà Nội], ngày [05] tháng [02] năm [2025]</p>
    </td>
  </tr>
</table>

<!-- Kính gửi: một nơi thì cùng dòng; nhiều nơi thì liệt kê mỗi nơi một dòng có "-" -->
<p class="kinh-gui"><span class="kinh-gui-list">Kính gửi: [Tên cơ quan, tổ chức nhận].</span></p>
<!-- Nhiều nơi nhận:
<div class="kinh-gui"><div class="kinh-gui-list">
  <p>Kính gửi:</p>
  <p style="padding-left:2.5cm">- [Cơ quan A];</p>
  <p style="padding-left:2.5cm">- [Cơ quan B].</p>
</div></div> -->

<!-- Ô 6: nội dung -->
<div class="noi-dung" data-o="6">
  <p>[Mở đầu: nêu căn cứ/lý do, ví dụ "Thực hiện ..., [Cơ quan] đề nghị ..." ]</p>
  <p>1. [Nội dung thứ nhất ...]</p>
  <p>2. [Nội dung thứ hai ...]:</p>
  <p>a) [...];</p>
  <p>b) [...].</p>
  <p>[Kết: đề nghị, đầu mối liên hệ (họ tên, số điện thoại), lời cảm ơn nếu phù hợp].</p>
</div>

<!-- PHẦN CUỐI: ô 9, 11 (trái) | ô 7a, 7c, 8, 7b (phải) -->
<table class="sign">
  <tr>
    <td class="noi-nhan-col">
      <p class="noi-nhan-tieu-de" data-o="9">Nơi nhận:</p>
      <div class="noi-nhan">
        <p>- Như trên;</p>
        <p>- [Lãnh đạo cơ quan (để b/c)];</p>
        <p>- Lưu: VT, [đơn vị soạn thảo] ([số bản lưu]).</p>
      </div>
    </td>
    <td class="ky-col">
      <p class="chuc-vu" data-o="7a">KT. [GIÁM ĐỐC]</p>
      <p class="chuc-vu">[PHÓ GIÁM ĐỐC]</p>
      <div class="cho-ky" data-o="7c 8" aria-label="Chữ ký và dấu"></div>
      <p class="ho-ten" data-o="7b">[Họ và tên]</p>
    </td>
  </tr>
</table>

</body>
</html>
````

---

## TÀI LIỆU KÈM THEO: `assets/mau-van-ban-qppl.html`

(Tệp mẫu — sao chép nguyên văn khi tạo đầu ra.)

````html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mẫu văn bản QPPL</title>
<!--
  MẪU VĂN BẢN QUY PHẠM PHÁP LUẬT – theo NĐ 78/2025/NĐ-CP
  Cách dùng (cho agent):
    1. Sao chép tệp, thay mọi chỗ [ ... ] bằng dữ liệu thật; xoá khối không dùng.
    2. Giữ nguyên CSS. Mở bằng trình duyệt → In → Lưu PDF (khổ A4, lề "Mặc định"/"Không" vì lề đã đặt trong @page).
    3. Ví dụ dưới đây là một NGHỊ ĐỊNH; đổi tên loại, ký hiệu, khối ký cho loại văn bản khác (xem SKILL.md).
  Ánh xạ ô số trên sơ đồ: data-o="1".."11".
-->
<style>
  @page {
    size: A4 portrait;
    margin: 20mm 20mm 20mm 30mm;            /* trên phải dưới trái: 15–20 / 15–20 / 15–20 / 30–35 mm */
    @top-center { content: counter(page); font: 13pt "Times New Roman", serif; }
  }
  @page :first { @top-center { content: none; } }   /* không hiện số trang 1 */

  html { background: #e9ecef; }
  body {
    font-family: "Times New Roman", Times, serif; color: #000; background: #fff;
    font-size: 14pt; line-height: 1.3;
    width: 210mm; min-height: 297mm; margin: 0 auto; padding: 20mm 20mm 20mm 30mm; box-sizing: border-box;
  }
  @media print { html { background: none; } body { width: auto; min-height: 0; padding: 0; margin: 0; } }
  @media screen and (max-width: 820px) { body { width: 100%; padding: 16px; } }

  p { margin: 0; }
  .center { text-align: center; }
  .b { font-weight: bold; } .i { font-style: italic; } .up { text-transform: none; }
  .rule-full  { display: block; height: 0; border-top: 1px solid #000; margin: 2px auto 0; }
  .rule-third { display: block; height: 0; border-top: 1px solid #000; width: 40%; margin: 2px auto 0; } /* 1/3–1/2 dòng chữ */

  /* Phần đầu: bảng 2 cột không viền */
  table.head, table.sign { width: 100%; border-collapse: collapse; }
  table.head td, table.sign td { vertical-align: top; padding: 0; }
  .col-left  { width: 40%; text-align: center; }
  .col-right { width: 60%; text-align: center; }
  .co-quan   { font-size: 13pt; font-weight: bold; white-space: nowrap; }                 /* ô 2 */
  .quoc-hieu { font-size: 13pt; font-weight: bold; white-space: nowrap; }                 /* ô 1 */
  .tieu-ngu  { font-size: 14pt; font-weight: bold; display: inline-block; }               /* ô 1 */
  .tieu-ngu-rule { border-top: 1px solid #000; }                                          /* dài bằng dòng chữ */
  .so-ky-hieu { font-size: 13pt; margin-top: 6pt; }                                       /* ô 3 */
  .dia-danh   { font-size: 14pt; font-style: italic; margin-top: 6pt; }                   /* ô 4 */
  .mat        { font-size: 13pt; font-weight: bold; margin-top: 6pt; }                    /* ô 10 */

  .ten-loai   { font-size: 14pt; font-weight: bold; text-align: center; margin-top: 18pt; } /* ô 5 */
  .ten-goi    { font-size: 14pt; font-weight: bold; text-align: center; }
  .can-cu     { font-size: 14pt; font-style: italic; text-indent: 1.27cm; text-align: justify; margin-top: 6pt; }
  .tu-khoa    { font-size: 13pt; font-weight: bold; text-align: center; margin: 12pt 0 6pt; } /* QUYẾT NGHỊ: / QUYẾT ĐỊNH: */

  /* Ô 6 – nội dung */
  .noi-dung p { text-align: justify; text-indent: 1.27cm; margin-top: 6pt; line-height: 1.3; }
  .noi-dung p.chuong, .noi-dung p.ten-chuong { text-align: center; text-indent: 0; }
  .chuong     { font-weight: bold; text-align: center; margin-top: 12pt; }
  .ten-chuong { font-weight: bold; text-align: center; font-size: 14pt; }
  .noi-dung p.dieu { font-weight: bold; }

  /* Phần cuối: nơi nhận trái, chữ ký phải */
  table.sign { margin-top: 12pt; }
  .noi-nhan-col { width: 45%; text-align: left; }
  .ky-col { width: 55%; text-align: center; }
  .noi-nhan-tieu-de { font-size: 12pt; font-weight: bold; font-style: italic; }       /* ô 9 */
  .noi-nhan { font-size: 11pt; line-height: 1.2; }
  .chuc-vu { font-size: 13pt; font-weight: bold; }                                     /* ô 7a */
  .cho-ky  { height: 28mm; }                                                           /* ô 7c + ô 8 */
  .ho-ten  { font-size: 14pt; font-weight: bold; }                                     /* ô 7b */
  .danh-may { font-size: 11pt; }                                                       /* ô 11 */
</style>
</head>
<body>

<!-- PHẦN ĐẦU: ô 2, 3 (trái) | ô 1, 4 (phải) -->
<table class="head">
  <tr>
    <td class="col-left">
      <p class="co-quan" data-o="2">CHÍNH PHỦ</p>
      <span class="rule-third"></span>
      <p class="so-ky-hieu" data-o="3">Số: [01]/[2025]/NĐ-CP</p>
      <!-- ô 10 (chỉ khi văn bản có độ mật): <p class="mat" data-o="10">[MẬT]</p> -->
    </td>
    <td class="col-right">
      <p class="quoc-hieu" data-o="1">CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</p>
      <p><span class="tieu-ngu">Độc lập - Tự do - Hạnh phúc<span class="rule-full tieu-ngu-rule"></span></span></p>
      <p class="dia-danh" data-o="4">[Hà Nội], ngày [05] tháng [02] năm [2025]</p>
    </td>
  </tr>
</table>

<!-- Ô 5: tên văn bản -->
<p class="ten-loai" data-o="5">NGHỊ ĐỊNH</p>
<p class="ten-goi">[Quy định chi tiết một số điều của Luật ...]</p>
<span class="rule-third" style="width:30%"></span>

<!-- Căn cứ ban hành: nghiêng 14, mỗi căn cứ một dòng, kết thúc ";" -->
<p class="can-cu" style="margin-top:14pt">Căn cứ [Luật Tổ chức Chính phủ số .../.../QH...];</p>
<p class="can-cu">Căn cứ [Luật ...];</p>
<p class="can-cu">Theo đề nghị của [Bộ trưởng Bộ ...];</p>
<p class="can-cu">Chính phủ ban hành Nghị định [quy định chi tiết ...].</p>

<!-- Ô 6: nội dung -->
<div class="noi-dung" data-o="6">
  <p class="chuong" style="text-indent:0">Chương I</p>
  <p class="ten-chuong" style="text-indent:0">[QUY ĐỊNH CHUNG]</p>

  <p class="dieu">Điều 1. [Phạm vi điều chỉnh]</p>
  <p>[Nội dung điều 1 ...]</p>

  <p class="dieu">Điều 2. [Đối tượng áp dụng]</p>
  <p>1. [Khoản 1 ...]</p>
  <p>2. [Khoản 2 ...]:</p>
  <p>a) [Điểm a ...];</p>
  <p>b) [Điểm b ...];</p>
  <p>đ) [Lưu ý: thứ tự chữ cái tiếng Việt a, b, c, d, đ, e, g, h, i, k ...].</p>

  <p class="chuong" style="text-indent:0">Chương II</p>
  <p class="ten-chuong" style="text-indent:0">[ĐIỀU KHOẢN THI HÀNH]</p>
  <p class="dieu">Điều 3. Hiệu lực thi hành</p>
  <p>Nghị định này có hiệu lực thi hành từ ngày [...] tháng [...] năm [...].</p>
</div>

<!-- PHẦN CUỐI: ô 9, 11 (trái) | ô 7a, 7c, 8, 7b (phải). "Nơi nhận:" ngang hàng dòng chức vụ -->
<table class="sign">
  <tr>
    <td class="noi-nhan-col">
      <p class="noi-nhan-tieu-de" data-o="9">Nơi nhận:</p>
      <div class="noi-nhan">
        <p>- [Ban Bí thư Trung ương Đảng];</p>
        <p>- [Thủ tướng, các Phó Thủ tướng Chính phủ];</p>
        <p>- [Các bộ, cơ quan ngang bộ, cơ quan thuộc Chính phủ];</p>
        <p>- [Văn phòng Chính phủ: ..., Công báo];</p>
        <p>- Lưu: VT, [đơn vị soạn thảo] ([số bản lưu]).</p>
      </div>
      <!-- ô 11 (nếu cơ quan dùng): <p class="danh-may" data-o="11">[KH người đánh máy, số bản]</p> -->
    </td>
    <td class="ky-col">
      <p class="chuc-vu" data-o="7a">TM. CHÍNH PHỦ</p>
      <p class="chuc-vu">THỦ TƯỚNG</p>
      <div class="cho-ky" data-o="7c 8" aria-label="Chữ ký và dấu"></div>
      <p class="ho-ten" data-o="7b">[Họ và tên]</p>
    </td>
  </tr>
</table>

</body>
</html>
````
