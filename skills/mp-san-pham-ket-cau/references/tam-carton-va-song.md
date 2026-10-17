# Tấm carton và các loại sóng

## 1. Cấu tạo tấm

| Tên | Cấu tạo | Ghi chú |
|---|---|---|
| Tấm một mặt (single face) | 1 giấy sóng + 1 giấy mặt | Bán thành phẩm sau máy sóng một mặt |
| Tấm sóng đơn — **3 lớp** | 2 giấy mặt + 1 giấy sóng | Sóng A, B, C hoặc E |
| Tấm sóng đôi — **5 lớp** | 3 giấy mặt + 2 giấy sóng | BC, BE, BA |
| Tấm sóng ba — 7 lớp | 4 giấy mặt + 3 giấy sóng | **Minh Phúc không làm** |

[Chuẩn: IS 2771-1 mục 4.1][MP-Web]

Tên lớp trên kế hoạch tổ sóng Minh Phúc: **Mặt** (giấy mặt ngoài) · **B** (giấy sóng B) · **Giữa** (giấy mặt giữa của tấm 5 lớp) ·
**E** · **A** · **C** (giấy sóng tương ứng) · **Đáy** (giấy mặt trong). Dây chuyền có trạm sóng A/C/E (một máy, đổi A, C hoặc E
theo đơn) và trạm sóng B; sóng đôi BC = trạm B + trạm C. [MP-MES]

## 2. Đặc tính các loại sóng

| Sóng | Cao (mm) theo web MP | Thế mạnh | Dùng cho |
|---|---|---|---|
| A | 4,5 – 5,0 | Đệm, giảm chấn tốt nhất; chịu xếp chồng | Hàng nặng, dễ vỡ |
| C | 3,5 – 4,0 | Cân bằng nén và đệm — phổ biến nhất | Thùng vận chuyển tiêu chuẩn |
| B | 2,5 – 3,2 | Chống đè bẹp, mặt phẳng in đẹp, gấp dễ, bền ở lằn | Hộp bán lẻ, hàng lon, chai |
| E | 1,5 – 1,6 | Mặt mịn, in offset rất nét, dễ gấp nhất | Hộp nhỏ, mỹ phẩm, quà tặng; bồi offset |
| BC (5 lớp) | 6 – 7 | B chống bẹp + C chịu nén | Hàng nặng, xuất khẩu |
| BE (5 lớp) | 4 – 4,5 | Mặt ngoài in đẹp, trong vẫn cứng | Vừa bền vừa đẹp |

[MP-Web; Chuẩn: IS 2771-1 mục 4.2.1]. Trong thùng, sóng thường **đứng** để chịu xếp chồng tốt nhất.

## 3. Phân loại sóng theo chiều cao và bước sóng [Chuẩn: FEFCO Quality Catalogue, bảng 3]

| Sóng | Chiều cao h (mm) | Bước sóng (mm) |
|---|---|---|
| G | < 0,6 | ≤ 1,8 |
| F | 0,6 – < 1,0 | 1,8 – < 2,6 |
| E | 1,0 – < 1,9 | 2,6 – 3,5 |
| D | 1,9 – < 2,2 | 3,5 – 4,8 |
| B | 2,2 – < 3,1 | 4,8 – 6,5 |
| C | 3,1 – < 4,0 | 6,5 – 7,9 |
| A | 4,0 – < 5,0 | 7,9 – 10,0 |
| K | ≥ 5,0 | > 10,0 |

IS 2771 ghi số sóng trên 30 cm: **A 32–38 · B 50–56 · C 36–43 · E 90–96** (cao A 4,2–4,6; B 2,2–2,8; C 3,5–3,7; E 1,2–1,6 mm).
Cách nhận sóng tại xưởng: cắt ngang tấm ở vùng không in, đếm số đỉnh sóng trên 30 cm, so bảng trên.
Độ dày tấm **không** dùng để xác định loại sóng (sóng bị ép bẹp khi in vẫn là sóng cũ).

## 4. Độ dày tấm dùng để tính toán [KN ngành]

Giá trị gần đúng để tính lằn, phôi, McKee khi chưa đo (đo thật bằng thước đo độ dày theo ISO 3034):

| Sóng | Độ dày t gần đúng (mm) |
|---|---|
| E | 1,5 |
| B | 3,0 |
| C | 4,0 |
| A | 5,0 |
| BE | 4,5 |
| BC | 7,0 |

## 5. Hệ số co sóng (take-up factor) [KN ngành]

Chiều dài giấy sóng cần cho 1 m tấm (phép đo FEFCO R 102). Dùng để tính định lượng tấm và lượng giấy sóng tiêu hao.

| Sóng | Hệ số co gần đúng |
|---|---|
| A | 1,50 – 1,55 |
| C | 1,42 – 1,48 (Georgia Tech dùng 1,43) |
| B | 1,32 – 1,38 |
| E | 1,22 – 1,30 |

Hệ số thật phụ thuộc trục sóng của máy — hỏi nhà sản xuất trục hoặc đo: cắt 1 tấm dài L, tách giấy sóng, kéo phẳng đo L'
→ hệ số = L'/L.

**Định lượng tấm (g/m²)** ≈ Σ giấy mặt + Σ (giấy sóng × hệ số co) + keo khô (~8–15 g/m² mỗi lớp keo [KN ngành]).
Ví dụ 3 lớp sóng C: mặt 150 + sóng 120 × 1,45 + đáy 150 ≈ 474 g/m² chưa kể keo. Máy tính: `python -m mptinh dinh-luong`.

## 6. Giấy cho carton [Chuẩn: FEFCO QC; NZQA 40318]

- **Giấy mặt (liner)**: kraftliner (xơ nguyên sinh, nâu hoặc mặt trắng), testliner (tái chế, nâu hoặc trắng), schrenz,
  giấy mặt trắng (white top).
- **Giấy sóng (medium/fluting)**: giấy sóng tái chế (RF, "wellenstoff"), giấy sóng bán hoá (SC — semi-chemical).
- Tấm đặc biệt: định lượng cao/thấp, tấm một mặt, cáctông đặc (solid fibre).
- Xưởng offset: giấy mặt Couche / Ivory / Duplex in offset rồi bồi lên tấm sóng (thường sóng E).

Chỉ tiêu giấy và cách nhận giấy: skill `mp-giay-nguyen-lieu`.
