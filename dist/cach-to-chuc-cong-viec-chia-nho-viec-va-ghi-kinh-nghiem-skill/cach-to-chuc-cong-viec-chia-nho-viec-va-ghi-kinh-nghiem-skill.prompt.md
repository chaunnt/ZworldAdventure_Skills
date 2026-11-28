# SKILL: cach-to-chuc-cong-viec-chia-nho-viec-va-ghi-kinh-nghiem-skill

> Tệp này gộp toàn bộ skill thành một tài liệu duy nhất để dùng với ChatGPT, Gemini hoặc model bất kỳ.
> Hãy làm theo phần HƯỚNG DẪN CHÍNH; các phần TÀI LIỆU KÈM THEO là tài liệu tra cứu được nhắc tới trong hướng dẫn.
> Nguồn: https://github.com/chaunnt/ZworldAdventure_Skills/tree/main/skills/cach-to-chuc-cong-viec-chia-nho-viec-va-ghi-kinh-nghiem-skill

**Mô tả / khi nào dùng:** Quy trình gốc cho mọi việc của agent với Z-World. Trước khi làm thì tra repo skill xem đã có cách làm chưa. Việc phức tạp thì chia thành các việc nhỏ, mỗi việc nhỏ một skill đơn lẻ, và có một skill quy trình ghép chúng lại. Làm xong thì ghi kinh nghiệm vào repo ZworldAdventure_Skills. Dùng khi bắt đầu một việc mới, khi gặp việc nhiều bước, khi người dùng nói "lưu kinh nghiệm", "tạo skill", "đừng tìm hiểu lại từ đầu", "tối ưu công việc".

---

## HƯỚNG DẪN CHÍNH (SKILL.md)

# Chia nhỏ việc phức tạp và ghi kinh nghiệm thành skill

Mục tiêu: **không việc nào phải tìm hiểu lại từ đầu**. Mỗi lần làm xong, cách làm được ghi thành skill. Lần sau chỉ cần đọc lại skill đó.

## Hai loại skill

| Loại | `metadata.level` | Tiền tố summary | Nội dung |
|---|---|---|---|
| Skill đơn lẻ | `don-le` | `[Đơn lẻ]` | Một thao tác cụ thể: đầu vào, các bước, lệnh, lỗi hay gặp. Không gọi skill khác. |
| Skill quy trình | `quy-trinh` | `[Quy trình]` | Việc phức tạp: dùng skill đơn lẻ nào, thứ tự ra sao, điểm cần quyết định. Khai báo danh sách trong `metadata.uses`. |

Tiền tố summary hiện ngay trong `llms.txt`, nhờ vậy chỉ cần lướt danh sách là biết skill nào là quy trình.

## Quy trình bắt đầu mọi việc

1. Clone repo skill nông (xem `cach-to-chuc-cong-viec-clone-push-repo-github-nong-an-toan`), đọc `llms.txt`. Việc cần viết code thì đọc thêm `index.json` của Vault. **Không mở lần lượt từng SKILL.md.**
2. Có skill quy trình khớp việc → làm theo nó. Chỉ có skill đơn lẻ khớp một phần → dùng các skill đó, phần còn thiếu thì tự làm.
3. Chưa có gì → làm việc như bình thường, nhưng ghi chép lại: các bước, lệnh chạy được, lỗi đã gặp và cách sửa.

## Quy trình kết thúc việc (ghi kinh nghiệm)

1. Tách việc vừa làm thành các thao tác nhỏ dùng lại được. Mỗi thao tác là một skill đơn lẻ, cái nào có sẵn thì cập nhật cái đó.
2. Nếu việc có từ 2 thao tác trở lên → viết thêm skill quy trình, liệt kê skill đơn lẻ trong `metadata.uses` và mô tả thứ tự gọi.
3. Đặt tên theo quy chuẩn trong `cach-viet-van-ban-skill-ai-da-nen-tang`. Tên phải **cụ thể, đọc là hiểu**, dài 5-15 từ cũng được, tối đa 64 ký tự. Tránh các từ bị cấm: `moi`, `chung`, `test`, `misc`, `tool`, `helper`.
4. Ghi vào skill những gì **chỉ có được sau khi làm thật**: lỗi gặp phải, giới hạn môi trường, cách đã chạy được. Đừng chép lại kiến thức phổ thông.
5. **Tool tự viết** (py, node, bash...) dùng lại được → lưu vào repo **private** `chaunnt/ZWorldAdventure_Vault`: tổng quát hoá, thêm header `@mo-ta/@cach-dung`, đặt tên file cụ thể, build `index.json` (xem `CLAUDE.md` của Vault). Trong skill chỉ ghi đường dẫn tool trong Vault, không chép lại code. Trước khi viết script mới, đọc `index.json` của Vault xem đã có tool chưa.
6. Chạy `python3 scripts/build_skills.py`, sau đó commit và push.

## Ranh giới quan trọng: không làm lộ thông tin cá nhân

Repo skill là **public**. Skill chỉ ghi **cách làm**, không ghi **dữ liệu của một người hay doanh nghiệp cụ thể**.

- **Cấm** ghi vào skill: họ tên người thật, tên doanh nghiệp thật đang là khách hàng, MST, CCCD, SĐT, email, địa chỉ cụ thể, biển số xe, số tài khoản, token, mật khẩu, nội dung email/tin nhắn của khách.
- Ví dụ dùng dữ liệu **giả rõ ràng**: `CÔNG TY ABC`, `0301234567 (ví dụ giả)`, `nguyen.van.a@example.com`, `phuong-x`.
- Khi rút kinh nghiệm từ một file thật, ghi lại **đặc điểm cấu trúc** của file (dòng tiêu đề, kiểu cột, lỗi hay gặp), không chép giá trị trong đó.
- Data thật để trong kho data private (danh mục `cach-quan-ly-du-lieu`). Skill chỉ ghi tên repo và đường dẫn, không ghi nội dung.
- `scripts/build_skills.py` tự quét skill tìm email, SĐT, dãy số giống MST/CCCD và báo lỗi. Có cảnh báo thì phải sửa, đừng tìm cách lách.

## Checklist

- [ ] Đã tra `llms.txt` trước khi bắt đầu.
- [ ] Mỗi thao tác dùng lại được đều có skill đơn lẻ; việc nhiều bước có skill quy trình kèm `uses`.
- [ ] Tên skill cụ thể, summary có tiền tố `[Đơn lẻ]`/`[Quy trình]`.
- [ ] Không có thông tin cá nhân hay data thật của khách hàng cụ thể nào; ví dụ đều là dữ liệu giả.
- [ ] Đã build, commit, push.
