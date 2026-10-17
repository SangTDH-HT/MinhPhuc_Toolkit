---
name: mp-be-dan
description: >
  Tổ thành phẩm của Minh Phúc: máy bế tự động 1 và 2 (bế phẳng), máy bế tròn, khuôn bế (dao cắt 23,8 mm, dao lằn, ma trận lằn,
  cao su đẩy, khấc), gỡ lề, máy dán tự động 1 và 2 (folder-gluer: cấp tờ, gấp mồi, keo, gấp cuối, ép), keo dán và độ nhớt,
  khe dán, đuôi cá, đóng kim, xếp – đóng kiện – đai, phiếu nhận dạng lô hàng SX-QT01-BM02/06 và luật chia pallet, đếm nhịp × số con
  và đếm đôi ở máy bế, 18 mã lỗi BE-01…BE-18 và 17 mã DA-01…DA-17, an toàn máy bế. Dùng khi lên khuôn, chỉnh máy dán,
  xử lý lỗi bế/dán, in phiếu pallet, đào tạo thợ thành phẩm.
---

# mp-be-dan — bế đúng, dán thẳng, kiện chắc

Máy theo HSNL: **2 máy bế tự động** (3.500 và 5.500 nhịp/giờ, ≥ 58.000 tờ/ngày), **máy bế tròn** (150 nhịp/phút), **máy dán** (150 m/phút)
ở xưởng flexo; máy bế phẳng + máy dán ở xưởng offset. Trên MES: **Máy bế tự động 1, 2** · **Máy dán tự động 1, 2** · **Máy bồi** — chung một
Trang chủ tổ thành phẩm. [MP-HSNL][MP-MES]

## Việc thường gặp

| Việc | Đọc |
|---|---|
| Bế tròn, bế phẳng, khuôn bế, gỡ lề, mã BE-xx, đếm ở máy bế | [references/be-va-khuon.md](references/be-va-khuon.md) |
| Máy dán: make-ready, keo, khe dán, đuôi cá, mã DA-xx; đóng kiện, phiếu pallet | [references/dan-va-dong-kien.md](references/dan-va-dong-kien.md) |
| An toàn máy bế (kẹp giữa bàn ép), LOTO khi lên khuôn, gỡ kẹt | [references/be-va-khuon.md](references/be-va-khuon.md) mục 6, skill `mp-an-toan-lao-dong` |

## Quy tắc vàng

1. **Soát mã khuôn với phiếu** trước khi lên máy: khuôn = **KB + mã sản phẩm** (đơn mượn khuôn ghi đè trên kế hoạch) — lắp sai khuôn là BE-13.
2. **Kiểm khuôn khi nhận và khi trả** về kho (dao gãy, cao su bung) — BE-11, BE-12.
3. **Canh tờ đầu theo hình in** (bế lẹm, lệch bế — BE-04, BE-05); **canh dẫn hướng, đo khe dán ở thùng đầu** (DA-07, DA-08).
4. Khe dán sai, đuôi cá thường **bắt nguồn từ lằn, khe ở máy in/máy bế** — kiểm khâu trước trước khi chỉnh máy dán.
5. Máy bế đếm **nhịp**; sản lượng = **nhịp × số con**. Máy dán đếm **thùng**. Máy bế có thể **đếm đôi** (cảm biến thấy cả nhíp và tờ) — chênh
   đếm, không phải hàng hư (BE-17).
6. **Cắt điện, khoá, treo thẻ** khi lên khuôn, lót bù, gỡ kẹt — kể cả máy bế tự động.

## Ghi lỗi đúng ô MES

Ô thành phẩm: **Sóng · In · Bế · Định hình · Khác**. Phôi lỗi từ khâu trước ghi đúng ô Sóng / In / Bế; tấm canh khuôn, phôi canh máy là **hao hụt**
(BE-18, DA-17); đếm sai số trong bó (DA-15) là chênh đếm. Lỗi khác ghi mã BE-xx / DA-xx trong ghi chú.
