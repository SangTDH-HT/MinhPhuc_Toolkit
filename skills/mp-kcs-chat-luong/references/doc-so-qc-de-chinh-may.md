# Đọc số QC để chỉnh máy

Số QC chỉ có giá trị khi dẫn tới **chỉnh đúng chỗ**. Bảng dưới là cây suy luận [KN ngành] dựng từ các sổ tay tổ máy; luôn **kiểm phép thử trước**
(mẫu ổn định chưa, dao cắt mẫu sắc chưa, máy thử hiệu chuẩn chưa) rồi mới đổ cho máy.

## 1. Công thức nối giấy → tấm → thùng

```
ECT ≈ 0,7 × (Σ SCT giấy mặt + hệ số co × SCT giấy sóng)        (Maltenfort–Seth; sóng C hệ số co ≈ 1,43)
BCT = 5,87 × ECT × √(t × Z)                                     (McKee rút gọn; t độ dày tấm, Z chu vi đáy)
```

- BCT tỷ lệ **bậc một** với ECT nhưng chỉ tỷ lệ **căn bậc hai** với độ dày → mất 20 % độ dày (sóng bị ép) mất khoảng 10 % BCT, cộng thêm phần ECT giảm.
- Muốn tăng ECT: tăng **SCT của giấy** (giấy tốt hơn/định lượng cao hơn), không chỉ tăng độ dày.
- Độ ẩm +10 điểm % → ECT, BCT −~10 %.

## 2. Số thấp → nghi ở đâu

| Hiện tượng QC | Kiểm phép thử trước | Nguyên nhân hay gặp | Chỉnh ở đâu |
|---|---|---|---|
| **ECT thấp** | Dao cắt mẫu, ổn định mẫu | Giấy SCT/RCT thấp (so COA, đo lại giấy); sóng bẹp (độ dày giảm); bám keo kém; tấm ẩm/"xanh" | Giấy: kho/mua hàng. Sóng bẹp: áp máy dán đôi (tổ sóng), khe lô kéo máy in. Keo: bếp keo, nhiệt |
| **BCT thấp, ECT đạt** | Cố định nắp hay không (TAPPI vs FEFCO), ổn định mẫu | Độ dày giảm sau in (in ép bẹp); lằn quá sâu/nứt; sai **hướng sóng**; thùng cao mảnh; lỗ thông hơi, tay cầm; mối dán yếu; cong tấm | Máy in (khe lô kéo), cán lằn (sóng/in/bế), thiết kế kết cấu |
| **BCT dao động trong lô** | | Ẩm không đều, giấy khác lô, ép bẹp không đều theo khổ | Đo ẩm, đối chiếu lô giấy theo phiếu |
| **Độ bục thấp** | Chuẩn ISO 2758 hay 2759 | Giấy mặt yếu (định lượng, cấp kraft), bám keo kém | Giấy; keo |
| **Cobb cao** (hút nước nhiều) | Đo đúng mặt (mặt in khác mặt sau) | Giấy kém chống thấm; nhầm mặt giấy khi lắp cuộn | Mua giấy Cobb thấp; lắp đúng mặt; phủ chống ẩm theo đơn |
| **Bám keo kém** (xé không thấy xơ) | | Keo chưa chín (nhiệt thấp, chạy nhanh, điểm gel cao); keo ít; keo "khoá kéo" do nhiệt quá cao; giấy Cobb quá thấp keo không thấm | Bếp keo (độ nhớt, điểm gel), khe keo, nhiệt – tốc độ |
| **Độ dày tấm thấp** | Thước đo đúng áp | Biên dạng trục sóng mòn, căng giấy sóng, ngón giữ/chân không, thiếu nhiệt, keo nhiều | Tổ sóng (bảng "tấm mỏng" trong `mp-to-song`) |
| **Cong tấm** | Đo theo FEFCO | Ẩm hai mặt lệch, lực căng lệch, bẫy hơi | Tổ sóng — TS-12, TS-13 |
| **Kích thước lằn/khe sai** | Đo tâm lằn | Dao cắt dọc – cán lằn (tổ sóng), slotter (máy in), khuôn (bế) | Đúng máy tạo ra lằn đó |
| **Khe dán sai, đuôi cá** | Đo ở 3 điểm | Lằn khâu trước lệch; băng gấp lệch tốc; gấp mồi | Kiểm khâu trước rồi mới chỉnh máy dán |
| **Chồng màu, sai màu** | Nguồn sáng so màu | Canh bản; độ nhớt, pH; anilox | Máy in |

## 3. Vòng lặp cải tiến

Ghi số QC theo **số phiếu sản xuất** → nối dữ liệu MP MES (máy, ca, tốc độ, dừng máy) → mỗi tháng xem:
ECT/BCT theo **công thức tấm** (giấy nào ghép với giấy nào), theo **nhà cung cấp giấy**, theo **máy in** (ép bẹp) — để làm "bảng chuẩn tấm" của
riêng Minh Phúc (đang thiếu; xem `docs/LO-TRINH.md`).
