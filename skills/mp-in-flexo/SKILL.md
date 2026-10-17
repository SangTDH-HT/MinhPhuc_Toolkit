---
name: mp-in-flexo
description: >
  Tổ in flexo của Minh Phúc (Máy In 1, Máy In 2 — in thẳng lên tấm carton kèm cán lằn, xẻ rãnh; máy flexo process theo HSNL):
  cấu tạo trạm in, lên bản, canh tâm, canh chồng màu, tờ đầu, mực gốc nước (pH 8,5–9,5, độ nhớt 20–25 s cốc Ford 4, bọt),
  trục anilox (BCM, vệ sinh, 10 điều giữ tuổi thọ), bản photopolymer và băng dán, áp in "vừa chạm", in ép bẹp sóng,
  24 mã lỗi FX-01…FX-24 của xưởng và bảng tra lỗi Sun Chemical (nhoè, mờ, bít chữ, viền quầng, sọc, chồng mực kém…),
  đơn in 2 mặt, đơn cán màng hai lượt, mã bảng in BI + mã sản phẩm, đếm nhịp × số con. Dùng khi chạy máy in, xử lý lỗi in,
  duyệt màu, đào tạo thợ in, đọc số liệu tổ in.
---

# mp-in-flexo — in đẹp mà không làm yếu thùng

Hai máy in flexo (HSNL: 5 màu, 150 nhịp/phút; MES khai **6 trạm mực** — cần xác nhận) in thẳng lên tấm sóng, đi liền **cán lằn + xẻ rãnh**
(printer-slotter). HSNL còn nêu một máy flexo 5 màu in process 250 sp/phút (chưa có trên MES). [MP-HSNL][MP-MES]

## Việc thường gặp

| Việc | Đọc |
|---|---|
| Cấu tạo trạm in, chuẩn bị đơn (lên bản, canh tâm, chồng màu, tờ đầu), xẻ rãnh, đếm nhịp | [references/may-in-va-chuan-bi.md](references/may-in-va-chuan-bi.md) |
| Mực nước, anilox, bản và băng dán, quản lý màu | [references/muc-anilox-ban.md](references/muc-anilox-ban.md) |
| Lỗi in: 24 mã FX + bảng tra Sun Chemical + in ép bẹp sóng | [references/loi-in-va-xu-ly.md](references/loi-in-va-xu-ly.md) |
| Đơn in 2 mặt, đơn cán màng hai lượt, chuyển máy, lưu đơn | [references/may-in-va-chuan-bi.md](references/may-in-va-chuan-bi.md) mục 5–6 |

## Ba con số của mực — phải thuộc

| Chỉ tiêu | Giá trị | Ghi chú |
|---|---|---|
| pH | **8,5 – 9,5** | pH thấp → mực khô nhanh, đông gel trong buồng dao gạt; pha nước xong **đo lại pH** |
| Độ nhớt | **20 – 25 giây** cốc Ford số 4 | Đổ mực vào cốc, bấm giờ tới lúc dòng chảy đứt lần đầu |
| Bọt | **không có** | Phá bọt quá liều gây lỗ kim, mắt cá |

[Converter] Kiểm độ nhớt mực **đầu đơn và sau giờ nghỉ** (ví dụ thật: FX-04 "mực loãng sau giờ nghỉ trưa"). [MP]

## Khi in lỗi — hỏi theo thứ tự

1. **Tấm vào có lỗi không?** (cong, bong, sai khổ → ghi ô **Sóng**, báo tổ sóng — FX-01…03).
2. **Mực**: độ nhớt, pH, bọt, nhiễm bẩn, lô mực.
3. **Anilox – dao gạt**: bẩn, mòn, nghẹt, dao gạt cong.
4. **Bản**: bẩn, mòn, dán lỏng, phồng do hoá chất.
5. **Áp in**: áp bản, áp anilox – bản (phải "vừa chạm"); khe lô kéo (ép bẹp sóng).
6. **Máy**: song song trục, bánh răng, ổ bi (sọc, đậm nhạt hai bên).

Sửa một biến một lần; ghi lại anilox, độ nhớt, pH của lần chạy **đạt màu** để lần sau chạy lại nhanh.

## Ghi lỗi đúng ô MES

Ô máy in: **Sóng · Thử máy · In lệch · Nhảy dao · Khác** (ERP gọi ô cuối là "Ngoại quan"). Tờ thử, canh màu → **Thử máy** (FX-23),
không ghi vào Khác. Đếm dư/thiếu do cảm biến (FX-24) là chênh đếm, không phải hàng hư. Lỗi khác ghi **mã FX-xx** vào ghi chú.
