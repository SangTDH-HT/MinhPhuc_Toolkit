# Chọn kết cấu thùng theo tải và môi trường

Quy trình 6 bước. Bước 1–4 là ước lượng trên giấy; bước 5–6 mới là con số để chốt hợp đồng.

## Bước 1 — Hỏi đủ thông tin

| Thông tin | Vì sao cần |
|---|---|
| Khối lượng một thùng đã đóng hàng W (kg) | Tải lên thùng đáy |
| Kích thước lọt lòng (hoặc kích thước hàng + bao bì trong) | Chu vi Z cho McKee, phôi, pallet |
| Số tầng xếp chồng n (hoặc chiều cao pallet/kho) | (n − 1) × W |
| Hàng có tự đỡ tải không (chai lon, đồ điện tử có khoảng trống, hàng rời/thực phẩm) | Chọn hệ số an toàn S.F |
| Môi trường và thời gian: kho lạnh/mát, mùa mưa, lưu kho bao lâu, đi container đường biển | Độ ẩm và thời gian làm giảm BCT |
| In, thẩm mỹ, dựng thùng bằng máy hay tay | Chọn sóng mặt (B/E in đẹp), dung sai chặt cho máy dựng thùng |

## Bước 2 — Chọn sơ bộ theo ngành

Bảng quy cách thường dùng theo ngành: skill `mp-cong-ty` → `khach-hang-nganh-hang.md`.
Tham khảo thêm bảng IS 2771 (Ấn Độ, bảng 2) chọn tấm theo khối lượng hàng [Chuẩn: IS 2771-1]:

| Loại tấm | Khối lượng hàng tối đa (kg) | Tổng D+R+C tối đa (mm) | Độ bục tối thiểu (kPa) |
|---|---|---|---|
| 3 lớp | 5 | 635 | 600 |
| 3 lớp | 8 | 750 | 800 |
| 3 lớp | 10 | 1.025 | 900 |
| 5 lớp | 15 | 1.275 | 1.000 |
| 5 lớp | 20 | 1.525 | 1.200 |
| 5 lớp | 25 | 1.575 | 1.300 |
| 7 lớp | 30 – 75 | 1.650 – 2.150 | 1.400 – 2.900 |

Không cạnh nào vượt 50 % tổng D+R+C; khối lượng giảm 10 % thì tổng kích thước được tăng 5 %. Hàng trên 25 kg:
Minh Phúc không làm 7 lớp → **tính BCT cụ thể** thay vì tra bảng, cân nhắc 5 lớp BC giấy cao + vách ngăn chịu lực.

## Bước 3 — BCT yêu cầu [MP-Web]

```
BCT yêu cầu (kgf) = S.F × (n − 1) × W
```

| S.F | Mức hàng tự đỡ tải | Ví dụ |
|---|---|---|
| 3 | Tự đỡ tải (~100 %) | Chai thuỷ tinh, lon nhôm |
| 4 | Đỡ một phần (~50 %) | Quạt, đồ điện tử |
| 5 | Không đỡ tải | Thực phẩm, hàng rời |

Ví dụ: thực phẩm S.F 5, 8 tầng, 12 kg → 5 × 7 × 12 = **420 kgf**. Máy tính: `python -m mptinh bct-can --sf 5 --tang 8 --kg 12`.

Bù môi trường (định hướng): độ ẩm không khí tăng 10 điểm % → BCT giảm ~10 %; ở 80 % RH, BCT giảm 27–32 % so với 50 % RH
[Chuẩn: Georgia Tech]. Kho TP.HCM mùa mưa thường > 75 % RH, kho không điều hoà. **[KN ngành]**: xếp lệch mép pallet có thể
mất 20–30 % BCT, lưu kho vài tháng mất 30–40 %; xếp so le (interlock) yếu hơn xếp thẳng cột; lỗ thông hơi, lỗ tay cầm,
in phủ kín ép bẹp sóng đều làm giảm BCT. Máy tính độ ẩm: `python -m mptinh do-am`.

## Bước 4 — Từ BCT ra ECT, từ ECT ra giấy

McKee rút gọn [Chuẩn: Georgia Tech]:

```
BCT = 5,87 × ECT × √(t × Z)        ECT (N/m), t độ dày tấm (m), Z = 2 × (D + R) chu vi đáy (m)
⇒ ECT cần = BCT / (5,87 × √(t × Z))
```

Ví dụ ECT 5.000 N/m, t 4 mm, thùng 400 × 300 → Z 1,4 m → BCT ≈ 2.196 N ≈ **224 kgf**.

Maltenfort–Seth (sóng C) [Chuẩn: Georgia Tech]:

```
ECT ≈ 0,7 × (Σ SCT giấy mặt + 1,43 × SCT giấy sóng)       (SCT tính bằng kN/m)
```

Muốn tăng ECT thì tăng **SCT của giấy** (giấy tốt hơn, định lượng cao hơn), không chỉ tăng độ dày. Với 5 lớp cộng thêm
lớp mặt giữa và giấy sóng thứ hai (hệ số co của sóng đó). Máy tính: `python -m mptinh mckee`, `python -m mptinh ect`.

## Bước 5 — Làm mẫu

Mẫu kỹ thuật số (kết cấu, màu) → mẫu thật đúng giấy → khách đóng thử sản phẩm thật.

## Bước 6 — Đo và chốt

Đo BCT, ECT, bục, Cobb trên mẫu ở phòng QC (ổn định mẫu 23 °C / 50 % RH khi cần đối chiếu với khách). **Số đo bằng máy mới là số
chốt hợp đồng**; lưu vào hồ sơ quy cách mã hàng (`templates/ho-so-quy-cach-ma-hang.md`) để "lô sau giống lô trước".

## Bẫy hay gặp

- Chọn theo độ bục (Mullen) cho thùng xếp chồng: bục đo chống đâm thủng, **không** dự báo được BCT — dùng ECT.
- Tăng định lượng giấy mặt mà giữ giấy sóng yếu: ECT tăng ít; giấy sóng đóng góp lớn vào ECT (× hệ số co).
- Thùng quá cao, mảnh: BCT giảm; cân nhắc tỉ lệ kích thước, vách ngăn chịu lực.
- Hàng kho lạnh: chỉ tăng BCT chưa đủ — cần giấy mặt **Cobb thấp**; hàng ướp đá cần phủ chống ẩm theo đơn.
- Hàng điện tử: thông lệ chọn BCT dư **2–3 lần** tải xếp chồng; dùng 5 lớp thay 3 lớp khi xếp cao/đi container. [MP-Web]
