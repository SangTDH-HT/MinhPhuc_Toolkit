# Mã kiểu hộp FEFCO và ký hiệu bản vẽ

Bộ mã do FEFCO (châu Âu) và ESBO soạn, được ICCA (hiệp hội nhà sản xuất thùng carton quốc tế) công nhận; dùng ký hiệu
thay mô tả dài khi đặt hàng và ghi quy cách. [Chuẩn: FEFCO Code bản 11 (2007), bản 12 (2022)] — bản PDF trong thư viện
`01_San_pham_Ket_cau_hop` (chủ yếu là hình vẽ).

## 1. Các nhóm mã và sản phẩm Minh Phúc tương ứng

| Nhóm | Tên | Mô tả | Sản phẩm Minh Phúc |
|---|---|---|---|
| 01 | Cuộn, tấm thương mại | Tấm phẳng, cuộn một mặt | **Giấy tấm carton** |
| 02 | Hộp kiểu xẻ rãnh (slotted) | Một mảnh, có mối nối (dán, ghim, băng), nắp trên và đáy; giao phẳng, khách tự gập nắp | **0201 thùng nắp gài (RSC)** — sản phẩm chủ lực; **0200** thùng không nắp trên (HSC); **0203** nắp ngoài chồng toàn phần (FOL) |
| 03 | Hộp kiểu telescope | Nhiều mảnh; nắp và/hoặc đáy chụp lồng lên thân | **Thùng nắp rời, hộp âm dương** (ví dụ 0320 ghép từ hai nửa hộp) |
| 04 | Hộp gấp, khay | Thường một mảnh, đáy gập lên làm vách và nắp; có tai khoá, quai, mặt trưng bày | **Hộp bế định hình, khay**, hộp nắp cài gửi hàng (ví dụ 0427) |
| 05 | Hộp trượt | Nhiều mảnh lồng trượt; gồm cả vỏ bọc | — |
| 06 | Hộp cứng | Hai đầu rời và thân, cần ghim | — |
| 07 | Hộp dán sẵn | Một mảnh giao phẳng, dựng là dùng (đáy khoá, đáy tự bung) | Hộp đáy khoá (nếu có đơn) |
| 09 | Chi tiết lót trong | Lót, đệm, vách ngăn, tấm chia | **Vách ngăn, vỉ lót** — 0982 … 0999 theo số tấm ghép (2 tấm → 0982 … 19 tấm → 0999) |

[Chuẩn: FEFCO Code bản 11 tr. 7–8; MP-Web bài "Phân biệt các kiểu hộp carton"]

Gợi ý chọn kiểu theo nhu cầu (web Minh Phúc):

| Nhu cầu chính | Kiểu | Mã |
|---|---|---|
| Vận chuyển phổ thông, tối ưu chi phí | RSC nắp gài | 0201 |
| Mở/đóng nhiều lần, thành hộp chắc | Nắp rời / telescope | 03xx |
| Quà tặng, cao cấp, cảm giác mở hộp | Hộp âm dương (nắp dương chụp ngoài, đáy âm trong) | 03xx |
| Bày kệ, gửi hàng thương mại điện tử, khay | Hộp bế định hình | 04xx |
| Chai, lọ, linh kiện cần chia ô | Vách ngăn | 09xx |

Hộp âm dương: chất lượng nằm ở **dung sai bế** giữa hai mảnh (lỏng thì rơi nắp, chật thì khó đậy) → thường chạy **máy bế phẳng**
(góc sắc, lằn đều, dung sai chặt hơn bế tròn). [MP-Web]

## 2. Cách viết mã [Chuẩn: FEFCO]

- Mã đầy đủ `XXXX-XXXX`: bốn số đầu là kiểu chuẩn, phần sau là phiên bản riêng của nhà sản xuất (ví dụ `0201-2`).
- Kiểu kết hợp: nắp trên theo 0204, nắp đáy theo 0215 → viết **0204/0215** (trên/đáy).
- Ký hiệu dựng thùng: **M** dựng tay · **A** dựng máy · **M/A** cả hai · **M+A** cần cả hai.
- Bản vẽ trong bộ mã luôn **nhìn từ mặt trong** của hộp.
- Kiểu NZQA yêu cầu thợ nhận diện: khay bốn góc, hộp đáy khoá (crash-lock), hộp sáu góc, phôi bế, RSC, HSC;
  chi tiết lót: lót đan, tấm lớp, vách ngăn. [Chuẩn: NZQA 40318]

## 3. Ký hiệu trên bản vẽ (dieline) [Chuẩn: FEFCO Code bản 11 tr. 5]

| Mã | Ý nghĩa |
|---|---|
| CL | Đường bao hộp dựng / đường cắt phôi |
| SC | Đường xẻ rãnh |
| CI / CO | Lằn gấp vào trong / ra ngoài |
| SI / SO | Lằn có rạch, gấp vào / ra |
| DS | Lằn đôi |
| PL | Đường răng cưa |
| SE | Đường cắt mép mềm |
| TP | Răng cưa xé mở |
| SJ / TJ / GJ | Mối nối ghim / băng / dán keo |
| PC / UC / NC | Lỗ tay cầm đục bỏ / không đục bỏ |
| FD | Ký hiệu hướng sóng |

## 4. Đóng thùng

Bốn cách, dùng riêng hoặc kết hợp: dán keo (nguội hoặc nóng), dán băng, cài khoá, ghim. [Chuẩn: FEFCO Code tr. 8]
Kế hoạch ERP của Minh Phúc có cờ công đoạn **Đóng kim** (đóng ghim) — đơn thùng lớn có thể đi ghim thay dán. [MP-MES]
