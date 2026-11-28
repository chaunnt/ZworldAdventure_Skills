# SKILL: cach-to-chuc-cong-viec-clone-push-repo-github-nong-an-toan

> Tệp này gộp toàn bộ skill thành một tài liệu duy nhất để dùng với ChatGPT, Gemini hoặc model bất kỳ.
> Hãy làm theo phần HƯỚNG DẪN CHÍNH; các phần TÀI LIỆU KÈM THEO là tài liệu tra cứu được nhắc tới trong hướng dẫn.
> Nguồn: https://github.com/chaunnt/ZworldAdventure_Skills/tree/main/skills/cach-to-chuc-cong-viec-clone-push-repo-github-nong-an-toan

**Mô tả / khi nào dùng:** Clone repo GitHub nông (depth 3), kiểm tra repo public hay private trước khi ghi data, commit và push an toàn từ bản clone nông. Dùng khi cần lấy repo về để làm việc, khi push bị lỗi 413/429, hoặc trước khi lưu dữ liệu nhạy cảm lên một repo.

---

## HƯỚNG DẪN CHÍNH (SKILL.md)

# Clone và push repo GitHub nông, an toàn

## Các bước

1. **Clone nông** (người dùng yêu cầu chỉ lấy depth 3, không lấy toàn bộ history):
   ```bash
   git clone --depth 3 https://github.com/<owner>/<repo> <thu-muc>
   ```
   Repo lớn có thể mất vài phút. Đặt timeout dài và đừng ngắt giữa chừng: nếu bị ngắt, `index-pack` sẽ để lại một bản clone hỏng.
2. **Kiểm tra quyền xem** trước khi ghi data:
   ```bash
   gh api repos/<owner>/<repo> --jq '.visibility'   # public | private
   ```
   Repo `public` thì tuyệt đối không ghi data khách hàng hay bí mật vào.
3. **Đọc hướng dẫn của repo** (`CLAUDE.md`, `AGENTS.md`, `README.md`) trước khi sửa. Repo có thể có quy chuẩn riêng và có file sinh tự động không được sửa tay.
4. **Commit** có ghi đồng tác giả nếu môi trường yêu cầu.
5. **Push** từ bản clone nông:
   ```bash
   git -c push.negotiate=true push origin main
   ```
   Nếu thấy cảnh báo `push negotiation failed` thì chưa chắc push đã hỏng, hãy xem dòng `main -> main`. Bị từ chối vì gói quá lớn (413) thì chạy `git fetch --depth=50 origin main` rồi rebase lên.

## Lỗi hay gặp

| Lỗi | Cách xử lý |
|---|---|
| HTTP 429 "too many concurrent transfers" | Đây là giới hạn số kết nối đồng thời, không phải rate limit. Chờ 5 giây rồi thử lại **một lần**, và không clone song song nhiều repo. |
| Thư mục đích đã tồn tại | Đừng xoá ngay. Chạy `git -C <dir> rev-parse HEAD`, nếu lệnh chạy được thì bản clone đã dùng được. |
| Lệnh không tìm được nhánh | Không phải repo nào cũng dùng `main`. Xem `default_branch` qua `gh api`. |
