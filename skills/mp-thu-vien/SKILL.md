---
name: mp-thu-vien
description: >
  Thư viện tài liệu gốc phía sau repo và cách tra: bộ cào web minhphucpack.com (11 PDF theo phần, 80 bản chụp trang, hồ sơ năng lực 2025, chứng nhận ISO/FSC,
  video nhà máy), thư viện chuyên môn 132 PDF chia 9 mảng (FEFCO Code và Quality Catalogue, IS 2771/1397/7063, TCVN 6896, ISTA, NZQA 40317–40355,
  chuẩn năng lực Úc ICP, Sun Chemical, Harper, Lohmann, Cito, Intercol, Billerud, Korsnäs, APPM, FSC-STD-40-004, FSC-STD-50-001, 21 CFR 176, HSE PIS18),
  chữ trích Markdown để tra nhanh, danh sách nguồn và script tải lại, tài liệu nên mua. Dùng khi cần nguyên văn tiêu chuẩn, bảng gốc, hình vẽ FEFCO,
  hoặc khi thêm tài liệu mới vào kho.
---

# mp-thu-vien — biết tài liệu nằm đâu, tin tới mức nào

Repo chỉ chứa **kiến thức đã tổng hợp** (có ghi nguồn). Tài liệu gốc của bên thứ ba **không đưa lên git** (bản quyền) — nằm trên máy anh Sáng và tải lại được.

## Vị trí

| Kho | Đường dẫn (máy anh Sáng) | Nội dung |
|---|---|---|
| Web công ty | `C:\MinhPhuc\Website_MinhPhucPack\` | 11 PDF theo phần (00 tổng quan cho kỹ thuật … 09 định hướng), `Ban_chup_trang_web\` 80 PDF, `Tai_lieu_goc\` (hồ sơ năng lực 2025, chứng nhận ISO 9001, FSC CoC, bộ ký hiệu thùng SVG, video nhà máy), `_raw\text\*.md` chữ từng trang |
| Tài liệu chuyên môn | `C:\MinhPhuc\Tai_lieu_chuyen_mon\` | 132 PDF trong 01–09, mỗi mảng có `00_SO_TAY_*.pdf` (sổ tay tiếng Việt) + `_text\*.md` (chữ trích) + `_nguon.json` |
| Trong repo, tải lại được | `thu-vien/` (bị .gitignore) | `python scripts/tai_thu_vien.py` theo `sources/nguon.tsv` |

Danh mục đủ từng file: [../../sources/danh-muc-thu-vien.md](../../sources/danh-muc-thu-vien.md).

## Chín mảng chuyên môn

| Mảng | Tài liệu gốc chính | Skill dùng |
|---|---|---|
| 01 Sản phẩm, kết cấu | FEFCO Code bản 11 (2007), bản 12 (2022), NZQA 40318 | `mp-san-pham-ket-cau` |
| 02 Chất lượng, tiêu chuẩn | FEFCO Quality Catalogue 4.4, FEFCO Testing methods, IS 2771, IS 7063, IS 1060, IS 4006, IS 4261, TCVN 6896:2015, ISTA 3A, Georgia Tech (ẩm – BCT) | `mp-kcs-chat-luong` |
| 03 Giấy | IS 1397, IS 1763, Billerud, Korsnäs, APPM | `mp-giay-nguyen-lieu` |
| 04 Dây chuyền sóng | NZQA (máy sóng, keo, máy dán đôi, dao, cong tấm), ICPCBF (một mặt, hai mặt), FEFCO, AOPack, Valmet | `mp-to-song` |
| 05 In flexo | Sun Chemical (16 + 11 lỗi), Harper anilox, Lohmann, Converter, Luminite, NZQA in, ICPPRN | `mp-in-flexo` |
| 06 Bế – dán – thành phẩm | NZQA bế, dán, gỡ lề, đóng kiện; ICPCBF; Cito; Intercol; Heidelberg | `mp-be-dan` |
| 07 Offset – bồi – cán màng | Sun Chemical offset (21 lỗi), ICPCBF xén, cán – bồi | `mp-xuong-offset` |
| 08 FSC – ATTP – an toàn | FSC-STD-40-004 V3-1, FSC-STD-50-001 V2-1, 21 CFR 176.170/176.180, HSE PIS18 | `mp-fsc-iso-attp`, `mp-an-toan-lao-dong` |
| 09 Khung năng lực | NZQA kiến thức ngành, chương trình chứng chỉ III Úc | `mp-dao-tao` |

## Cách tra nhanh

1. Tìm trong skill trước (đã dịch, đã ghi nguồn).
2. Cần nguyên văn: tìm chữ trong `_text\*.md` của mảng (grep theo từ khoá tiếng Anh), rồi mở PDF đúng trang.
3. Hình vẽ kiểu hộp FEFCO: mở PDF FEFCO Code (bản vẽ nhìn từ mặt trong hộp).

## Độ tin của nguồn (dùng khi hai nguồn nói khác nhau)

1. **[MP]** — đã xác nhận tại xưởng (anh Sáng, tổ trưởng, KCS) hoặc dữ liệu/luật MP MES đã chốt.
2. **[MP-Web] / [MP-HSNL]** — công ty công bố (web, hồ sơ năng lực, chứng nhận).
3. **[Chuẩn]** — tiêu chuẩn, tài liệu nghề có tên (FEFCO, ISO, IS, NZQA, ICP, hãng máy, hãng mực).
4. **[KN ngành]** — kinh nghiệm chung của nghề, chưa kiểm tại Minh Phúc.

## Thêm tài liệu mới

1. Thêm dòng vào `sources/nguon.tsv` (thư mục mảng, tên file, URL, ghi chú) → `python scripts/tai_thu_vien.py --chi <mảng>`.
2. Đọc, tóm phần dùng được vào `references/` của skill đúng mảng, ghi nguồn `[Tên tài liệu, trang]`.
3. Sách máy (sau khảo sát tem nhãn): lưu `thu-vien/may-moc/<máy>/`, tóm thông số, lịch bảo trì, mã lỗi hãng vào skill tổ máy, gắn **[Sách hãng]**.
4. Cập nhật `sources/danh-muc-thu-vien.md` và `CHANGELOG.md`.

## Tài liệu nên mua (trả phí, chưa có)

TAPPI Corrugating Defect/Remedy Manual (7th), TIP 0304-32, Corrugated Adhesives Preparation (5th), The Anilox Roll (2nd), TIP 0306-17,
"Troubleshooting the Die Cutting / Folding Section"; ISO 3037, 12048, 2759, 535, 536, 9895, 2233, 2859-1; GB/T 6543-2025, GB/T 6544, JIS Z 1506,
DIN 55468-1; ISTA 1A/2A/3A; ISO 12647-2, G7/GRACoL; FTA FIRST; ECMA Code (hộp giấy gấp).
