# Phân loại lỗi, lấy mẫu AQL, dung sai

Nguồn: FEFCO/VDW Quality Catalogue 4.4 (2014) — "chuẩn mực thực hành tốt" ở châu Âu để khách kiểm nhận lô thùng, hộp, phôi carton;
IS 2771-1 (Ấn Độ) để tham khảo yêu cầu thùng hoàn chỉnh.

## 1. Ba loại lỗi, bốn cấp

| Loại | Ý nghĩa | Cấp | Mức ảnh hưởng | AQL |
|---|---|---|---|---|
| Nghiêm trọng (CD) | Gây hại người, vi phạm pháp luật, hỏng hàng bên trong, **làm đứng máy đóng gói** | 1 | Bao bì không dùng được | Không cho phép — có thể trả cả lô |
| Nặng (MJD) | Kém tác dụng, bị khiếu nại, giảm năng suất đóng gói | 2A | Nghiêm trọng | 0,65 hoặc 1,0 |
| Nặng (MJD) | | 2B | Ít hơn | 1,5 hoặc 4,0 |
| Nhẹ (MND) | Giảm chất lượng chung, không hậu quả đáng kể | 3 | Không đáng kể | 6,5 |

Một hộp nhiều lỗi chỉ tính lỗi **nặng nhất**. Lấy mẫu ngẫu nhiên rải đều đầu, giữa, cuối lô. Hộp hỏng do vận chuyển không tính.

## 2. Bảng lấy mẫu (theo ISO 2859-1)

Số trong ô là **số hộp lỗi tối đa được chấp nhận** (c) trong mẫu.

| Cỡ lô N (cái) | Cỡ mẫu n | AQL 0,65 | AQL 1,0 | AQL 1,5 | AQL 2,5 | AQL 4,0 | AQL 6,5 |
|---|---|---|---|---|---|---|---|
| đến 500 | N hoặc 10 | 0 | 0 | 0 | 1 | 1 | 2 |
| 501 – 1.200 | 20 | 0 | 1 | 1 | 1 | 2 | 3 |
| 1.201 – 3.200 | 32 | 1 | 1 | 1 | 2 | 3 | 4 |
| 3.201 – 10.000 | 50 | 1 | 1 | 2 | 3 | 4 | 6 |
| 10.001 – 35.000 | 80 | 1 | 2 | 3 | 4 | 6 | 8 |
| 35.001 – 150.000 | 125 | 2 | 3 | 4 | 6 | 8 | 12 |

Ví dụ lô 20.000 hộp → lấy 80: cấp 1 không được lỗi nào; 2A cho phép 1 (AQL 0,65) hoặc 2 (AQL 1,0); 2B cho 3 (AQL 1,5); cấp 3 cho 8 (AQL 6,5).
Đơn rất lớn nên chia lô (mỗi pallet hoặc mỗi chuyến xe một lô). Máy tính: `python -m mptinh aql --lo 20000 --aql 1.5`.

## 3. Chỉ tiêu vật liệu [FEFCO QC]

| # | Chỉ tiêu | Cách kiểm | Cấp | AQL |
|---|---|---|---|---|
| 1 | Loại giấy mặt (màu, cấp) | Nhìn, so đơn hàng | 2A | 0,65 |
| 2 | Tình trạng giấy mặt (nhăn, phồng, hư) | Nhìn | 2B | 4,0 |
| 3 | **Loại sóng và hướng sóng** | Cắt ngang sóng ở vùng không in | **1** | — |
| 4 | Cấu trúc sóng | Cắt sóng ở vùng nắp | 2B | 1,5 |
| 5 | Độ bám keo | Xé thử, phải thấy xơ giấy rách | 2B | — |
| 6 | Sóng và giấy mặt thẳng hàng | Nhìn | 3 | 6,5 |
| 7 | Độ phẳng (cong tấm) | Theo quy cách | 2B | 1,5 |

Mặc định **hướng sóng song song khe xẻ** nếu không thoả thuận khác. Độ dày tấm không dùng để xác định loại sóng. Đo cong: tấm đặt lên mặt phẳng,
chiều cong úp lên, độ cao lớn nhất ÷ khoảng cách hai mép tựa × 100 %.

## 4. Chỉ tiêu gia công (ở 23 °C / 50 % RH) [FEFCO QC]

| # | Chỉ tiêu | Dung sai / cách kiểm | Cấp | AQL |
|---|---|---|---|---|
| 1 | Kết cấu đúng bản vẽ | Có / không | 1 | — |
| 2 | **Kích thước** (tâm lằn – tâm lằn hoặc tâm lằn – mép) | ≤ 300 mm **±3**; 300–700 mm **±4**; 700–1.200 mm **±0,6 %**; > 1.200 mm thoả thuận | 2A | 0,65 |
| 3 | Dung sai phôi bế | ±0,5 %, tối thiểu ±1 mm | 2B | 4,0 (bế tròn) / 1,5 (bế phẳng) |
| 4 | Vị trí lằn gấp | Gấp đúng chỗ | 2A | 0,65 |
| 5 | Lằn gấp nứt | Nứt lớp ngoài 2B / 1,5 — nứt lớp trong 3 / 6,5 | | |
| 6 | Vị trí khe xẻ | Lệch tâm lằn dọc ±2 mm | 2A | 1,0 |
| 7 | Độ sâu khe xẻ | ±5 mm so tâm lằn | 2A | 1,0 |
| 8 | Mép cắt, khe xẻ | Không xơ, không sót giấy | 2B | 4,0 |
| 9 | **Khe hở mối dán** | Chuẩn 6–8 mm; sóng đơn −4/+4; sóng đôi −4/+6 mm | 2B | 4,0 / 1,5 |
| 10 | **Bền mối dán** | Xé tay: đạt nếu **≥ 80 %** diện tích keo còn xơ giấy | 2A | 0,65 |
| 11 | Lệch mép ở mối dán (đuôi cá) | ≤ 0,5 % chiều cao phôi, tối thiểu 3 mm | 2B | 1,5 |
| 12 | Dính nắp (keo trong/ngoài) | Có / không | 2A | 1,0 |
| 13 | Dán băng | Đúng loại, đúng vị trí | 2A | 1,0 |
| 14 | Ghim | Đúng vị trí, khoảng cách | 2A | 1,0 |
| 15 | In đúng nội dung | So mẫu in | 1 | — |
| 16 | In đầy đủ (nhoè, mờ, thiếu) | So mẫu | 2B | 1,5 |
| 17 | Màu | So mẫu chuẩn | 2B | 1,5 |
| 18 | **Chồng màu** | ±2 mm | 2B (flexo in sau) / 2A (in trước) | 1,5 / 1,0 |
| 19 | Vị trí hình in | So mẫu | 2B | 1,5 |

Ví dụ: sóng B (t ≈ 3 mm), lọt lòng 650 × 400 × 250 → lằn 653 × 403 × 256; đo 653 ± 4 × 403 ± 4 × 256 ± 3 là đạt.

## 5. Gán mã lỗi Minh Phúc vào cấp FEFCO (gợi ý để KCS duyệt) [KN ngành]

| Cấp | Mã MP tiêu biểu |
|---|---|
| 1 | FX-13 / OF-15 sai nội dung bản; BE-13 lắp sai khuôn; TS-03 sai loại giấy (sai kết cấu); sai hướng sóng |
| 2A | TS-17, TS-20 sai lằn/sai kích thước; FX-18 rãnh lệch; DA-04 bung mép dán; DA-12 dính thùng; FX-14, FX-15 lệch hình/chồng màu (in trước) |
| 2B | FX-04…07 nhoè, mờ, đậm nhạt, sai màu; DA-07 đuôi cá; DA-08 khe dán; TS-12 cong; TS-22 mép xơ; BE-06 bavia |
| 3 | Trầy nhẹ (FX-22, DA-13 mức nhẹ), bẩn nhẹ (TS-24, CH-04) |

## 6. IS 2771-1 (Ấn Độ) — các yêu cầu đáng tham khảo

- Dung sai kích thước thùng: **±3 mm (3 lớp), ±5 mm (5 lớp), ±7 mm (7 lớp)**; máy dựng thùng tự động có thể thoả thuận chặt hơn (không chặt hơn ±1 mm).
- Mối nối: chồng mép ≥ 30 mm; ghim ≤ 60 mm, ghim đầu/cuối ≤ 25 mm từ mép; dán kín toàn diện tích; nối giáp mép băng ≥ 50 mm.
- **Cobb 30 phút** mặt ngoài ≤ **155 g/m²** (vùng in trừ 5 %).
- Gập nắp 90° vào rồi 90° ra (sửa đổi 1997: 180°) không nứt.
- Bền mối nối: kéo tay, phải rách ở tấm chứ không bung keo/ghim.
- Không dùng keo silicat natri hay keo kiềm mạnh.
- Lấy mẫu: bục 3 thùng × 2 mẫu × 10 lần; độ dày 3 thùng; Cobb 3 thùng; gập nắp 3 thùng. Lô đạt khi mọi thùng đạt, hoặc một thùng trượt và thử lại
  gấp đôi không thêm thùng trượt.
- Bảng chọn tấm theo khối lượng hàng: skill `mp-san-pham-ket-cau` → `chon-ket-cau.md`.
