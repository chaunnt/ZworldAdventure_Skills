---
name: cach-viet-van-ban-skill-ai-da-nen-tang
description: Tạo mới hoặc chỉnh sửa một skill trong repo ZworldAdventure_Skills theo chuẩn Agent Skills (SKILL.md + references + assets) để dùng được trên Claude (claude.ai, Claude Code, API), ChatGPT (Custom GPT, Codex), Gemini (Gem, Gemini CLI) và các agent khác. Dùng khi người dùng muốn "viết skill", "tạo skill mới", "chuyển tài liệu/PDF/quy trình thành skill", "đóng gói skill cho ChatGPT/Gemini", hoặc rà soát một skill có đúng chuẩn không.
license: Xem LICENSE ở thư mục gốc repo
metadata:
  version: "1.1.0"
  language: vi
  category: cach-viet-van-ban
  summary: "Quy chuẩn tạo skill đa nền tảng (Claude, ChatGPT, Gemini), chuyển tài liệu/PDF thành skill và đóng gói."
  keywords: "agent skills, SKILL.md, viết skill, tạo skill, đóng gói skill, llms.txt"
---

# Viết skill chuẩn đa nền tảng

Một **skill** là một thư mục chứa hướng dẫn và tài nguyên để một AI agent làm tốt một loại việc.
Repo này dùng định dạng **Agent Skills** (chuẩn mở do Anthropic khởi xướng, được Claude, OpenAI Codex,
Gemini CLI, Cursor, GitHub Copilot... hỗ trợ). Với nền tảng chưa hỗ trợ trực tiếp (ChatGPT Custom GPT,
Gemini Gem), script `scripts/build_skills.py` tự chuyển skill thành **một tệp prompt duy nhất**.

Nguyên tắc vàng: **SKILL.md là nguồn sự thật duy nhất**. Không viết riêng bản cho từng model;
chỉ viết một lần cho đúng chuẩn, rồi build.

## Cấu trúc bắt buộc

```
skills/<ten-skill>/
├── SKILL.md            # bắt buộc: frontmatter YAML + hướng dẫn Markdown
├── references/         # tuỳ chọn: tài liệu tra cứu sâu (.html, .md) — agent đọc khi cần
├── assets/             # tuỳ chọn: mẫu, template, hình, dữ liệu dùng để tạo đầu ra
└── scripts/            # tuỳ chọn: mã chạy được (python/bash), chỉ dùng thư viện chuẩn nếu có thể
```

- `<ten-skill>` phải theo **Quy chuẩn đặt tên skill** ở mục dưới; trùng với `name` trong frontmatter.
- Đường dẫn trong SKILL.md luôn **tương đối** so với thư mục skill (vd references/quy-dinh.html), dùng `/`.

## Quy chuẩn đặt tên skill (bắt buộc)

Tên skill là thứ agent và người thấy đầu tiên khi lướt danh sách, nên phải **đọc tên là hiểu skill làm gì**,
và các skill cùng loại phải **nằm cạnh nhau** khi sắp xếp theo tên.

**Cấu trúc:**

```
<danh-muc>-<doi-tuong>[-<pham-vi>][-<can-cu>]
```

| Phần | Bắt buộc | Quy tắc | Ví dụ |
|---|---|---|---|
| `danh-muc` | Có | Đúng bằng slug danh mục trong `categories.json`. Dạng `cach-<dong-tu>-<doi-tuong-chung>`. | `cach-viet-van-ban`, `cach-tra-cuu-thong-tin`, `cach-tinh-phi` |
| `doi-tuong` | Có | Cụ thể: loại văn bản / nghiệp vụ / sản phẩm mà skill xử lý. Không dùng từ chung chung. | `quy-pham-phap-luat`, `skill-ai`, `hop-dong-bao-hiem` |
| `pham-vi` | Khi cần phân biệt | Giới hạn hoặc biến thể: đối tượng dùng, nền tảng, mức độ. | `da-nen-tang`, `ca-nhan`, `doanh-nghiep` |
| `can-cu` | Khi dựa trên văn bản pháp lý/tiêu chuẩn | Viết từ số ký hiệu: `<loai-co-quan><so>-<nam>`, bỏ dấu, viết liền phần chữ. | NĐ-CP 78/2025 → `ndcp78-2025`; TT 01/2025/TT-BTP → `ttbtp01-2025` |

**Ràng buộc kỹ thuật** (script build kiểm tra, sai là lỗi):
- Chỉ chữ thường a–z, số 0–9, gạch nối; **không dấu**, không chữ hoa (Claude và nhiều nền tảng từ chối chữ hoa), tối đa 64 ký tự.
- Phải bắt đầu bằng `<danh-muc>-` với `danh-muc` = `metadata.category`.

**Quy tắc nội dung:**
- Viết đầy đủ tiếng Việt không dấu, **không viết tắt** trừ ký hiệu văn bản pháp lý (`ndcp`, `tt`, `qh`) và từ phổ biến (`ai`, `pdf`).
- Cấm tên mơ hồ: `helper`, `tool`, `misc`, `chung`, `moi`, `test`, `v2`.
- Phiên bản của skill để trong `metadata.version`, **không** đưa vào tên. Chỉ đưa năm vào tên khi nó là một phần căn cứ (`-2025`).
- Hai skill cùng đối tượng nhưng khác căn cứ thì khác ở phần `can-cu`
  (vd `cach-viet-van-ban-quy-pham-phap-luat-ndcp78-2025` và một bản thay thế sau này `...-ndcp12-2027`).
- Cần danh mục mới: thêm vào `categories.json` trước (slug theo dạng `cach-<dong-tu>-<doi-tuong-chung>`, có `title`, `summary`).
- Đổi tên skill là thay đổi lớn (link, gói cài đặt đều đổi) — chỉ đổi khi tên hiện tại sai quy chuẩn.

**Ví dụ trong repo:**

| Tên | Đọc là |
|---|---|
| `cach-viet-van-ban-quy-pham-phap-luat-ndcp78-2025` | Cách viết văn bản / quy phạm pháp luật / theo NĐ-CP 78/2025 |
| `cach-viet-van-ban-skill-ai-da-nen-tang` | Cách viết văn bản / skill cho AI / dùng đa nền tảng |


## Frontmatter

```yaml
---
name: ten-skill                 # bắt buộc, = tên thư mục
description: >-                 # bắt buộc, ≤ 1024 ký tự, ngôi thứ ba
  [Skill làm gì]. Dùng khi [tình huống/từ khoá người dùng hay nói].
license: Xem LICENSE ở thư mục gốc repo
metadata:                       # chỉ dùng cặp khoá-giá trị chuỗi
  version: "1.0.0"
  language: vi
  category: cach-viet-van-ban   # bắt buộc: slug danh mục trong categories.json = tiền tố của name
  summary: "≤ 160 ký tự"        # bắt buộc: 1 câu ngắn, hiện trong llms.txt và danh sách
  keywords: "từ khoá 1, từ khoá 2"  # khuyến nghị: dùng cho SEO và tìm kiếm
  source: "[tài liệu gốc, nếu có]"
---
```

- Chỉ dùng các khoá `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.
  Khoá lạ có thể làm một số nền tảng từ chối upload.
- `summary` (≤ 160 ký tự) là dòng duy nhất agent thấy khi **lướt danh mục** (`llms.txt`) — viết sao cho chỉ đọc nó
  là biết có nên mở skill hay không. `description` dài hơn, dùng khi nền tảng tự chọn skill.
- `category` phải có trong `categories.json` ở gốc repo (thêm danh mục mới vào đó nếu cần).
- `description` là thứ agent đọc để **quyết định có dùng skill hay không** → phải nói rõ *làm gì* và *khi nào dùng*,
  liệt kê từ khoá thực tế người dùng sẽ gõ (cả tiếng Việt có dấu). Không dùng ký tự `<` `>` trong description.

## Thân SKILL.md

Viết bằng Markdown thuần (tiêu đề, danh sách, bảng, khối code) — mọi model đều đọc tốt. Bố cục khuyến nghị:

1. **Tiêu đề + 1–2 câu mục đích.**
2. **Tài liệu trong skill**: bảng `tệp → khi nào đọc`.
3. **Phạm vi và nguồn**: dựa trên tài liệu nào, điều gì nằm ngoài phạm vi, chỗ nào cần người dùng xác nhận.
4. **Quy trình làm việc**: các bước đánh số, mệnh lệnh ngắn.
5. **Bảng tra nhanh / quy tắc cốt lõi**: đủ để làm 80% việc mà không cần mở references.
6. **Checklist tự kiểm tra.**
7. **Định dạng đầu ra.**

Quy tắc viết:
- Giữ SKILL.md **dưới ~500 dòng**; chi tiết dài chuyển vào `references/` (agent chỉ tải khi cần — "progressive disclosure").
- Viết cho một agent thông minh nhưng **chưa biết gì về nghiệp vụ**: giải thích *vì sao*, không chỉ *làm gì*.
- Không phụ thuộc công cụ riêng của một nền tảng (không viết "dùng tool X của Claude"). Nếu cần, ghi
  "nếu môi trường có thể chạy Python thì chạy `scripts/...`; nếu không, làm thủ công theo bước ...".
- Không bịa dữ liệu; chỉ rõ chỗ cần người dùng cung cấp bằng `[...]`.
- Ghi rõ chênh lệch/mâu thuẫn trong tài liệu nguồn và lựa chọn ưu tiên.

## Chuyển tài liệu (PDF, ảnh, quy định) thành skill

1. Trích toàn bộ văn bản (vd `pdftotext -layout`), **xem trực tiếp các trang có hình** (render thành ảnh) — hình,
   sơ đồ, bảng thường không có trong văn bản trích xuất.
2. Loại bỏ phần thừa (menu web, quảng cáo, chữ lặp do trích xuất lỗi).
3. Viết lại nguyên văn có cấu trúc vào `references/<ten>.html` (HTML5 ngữ nghĩa: `section`, `h2/h3`, `ol/ul`, `table`, `dl`).
4. **Mọi hình/sơ đồ phải được mô tả bằng lời** để agent không nhìn ảnh vẫn hiểu:
   - mô tả tuần tự (trên→dưới, trái→phải), nêu quan hệ "ngang hàng", "dưới", "chồng lên", "canh giữa";
   - bảng toạ độ tương đối (% vùng nội dung) hoặc kích thước thật;
   - bản ASCII trong `<pre>`;
   - khối dữ liệu máy đọc `<script type="application/json">`;
   - (tuỳ chọn) dựng lại hình bằng HTML/CSS hoặc SVG có `aria-label`.
   Xem ví dụ chuẩn: `skills/cach-viet-van-ban-quy-pham-phap-luat-ndcp78-2025/references/so-do-bo-tri.html`.
5. Tóm tắt phần quan trọng nhất thành bảng tra nhanh + checklist trong SKILL.md.

Vì sao HTML5 cho references: một tệp vừa mở được bằng trình duyệt cho người đọc, vừa là văn bản có cấu trúc rõ ràng cho
model; nhúng được JSON, bảng, hình minh hoạ CSS/SVG mà không cần tệp ảnh. Yêu cầu: HTML5 tự chứa (CSS inline, không gọi
CDN), `lang="vi"`, `meta charset="utf-8"`, chạy được khi mở trực tiếp từ đĩa.

## Đóng gói và phân phối

Sau khi tạo/sửa skill, chạy ở thư mục gốc repo:

```bash
python3 scripts/build_skills.py          # kiểm tra + build tất cả skill vào dist/
python3 scripts/build_skills.py --check  # chỉ kiểm tra hợp lệ (dùng trong CI)
```

Script sẽ: kiểm tra frontmatter; tạo `dist/<ten>/<ten>.zip` (upload Claude), `dist/<ten>/<ten>.prompt.md`
(một tệp duy nhất cho ChatGPT/Gemini/model bất kỳ); sinh lại toàn bộ lớp điều hướng:
`llms.txt`, `skills.json`, `index.html`, `danh-muc/<slug>/` (có phân trang), `skills/<ten>/index.html`,
`sitemap.xml`, `robots.txt`, `.claude-plugin/marketplace.json`. **Không sửa tay các tệp sinh tự động.**
Chi tiết cách import từng nền tảng: `references/nen-tang.md`.

Lớp điều hướng cho AI (đọc từ nông đến sâu, dừng khi đủ):
`llms.txt` (1 dòng/skill) → `danh-muc/<slug>/llms.txt` (khi nhiều skill) → `skills/<ten>/SKILL.md` → `references/...`.

Mẫu khởi đầu: sao chép `assets/SKILL.template.md` thành `skills/<ten-skill>/SKILL.md`.

## Checklist skill hoàn chỉnh

- [ ] Tên đúng **Quy chuẩn đặt tên skill**: bắt đầu bằng slug danh mục, đủ chi tiết, không dấu, khớp tên thư mục và `name`.
- [ ] Có `metadata.category` (có trong `categories.json`) và `metadata.summary` ≤ 160 ký tự.
- [ ] `description` nói rõ làm gì + khi nào dùng, có từ khoá người dùng, ≤ 1024 ký tự.
- [ ] SKILL.md có: mục đích, bảng tài liệu, phạm vi/nguồn, quy trình, tra nhanh, checklist, đầu ra.
- [ ] Mọi hình/sơ đồ trong nguồn đã được mô tả bằng lời (+ toạ độ/JSON nếu là bố cục).
- [ ] Không phụ thuộc tool riêng của một model; đường dẫn tương đối.
- [ ] references HTML5 tự chứa, mở được offline.
- [ ] Đã chạy `python3 scripts/build_skills.py` không lỗi và commit toàn bộ tệp sinh ra.
