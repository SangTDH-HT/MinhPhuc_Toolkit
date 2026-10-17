# Tra theo triệu chứng

Khi chưa biết lỗi sinh ở đâu: tìm triệu chứng → máy nghi ngờ → mã lỗi → bảng tra sâu. [KN ngành] dựng từ các mã của xưởng và sổ tay tổ máy.

## 1. Triệu chứng khách báo

| Khách báo | Nghi ở đâu | Mã / kiểm gì |
|---|---|---|
| Thùng bẹp ở tầng dưới trong kho | Kết cấu không đủ BCT; ẩm kho; xếp lệch pallet; sóng bẹp khi in | Đo BCT mẫu lưu ở 23 °C/50 %; độ dày trước/sau in; skill `mp-san-pham-ket-cau` (chọn kết cấu) |
| Thùng mềm, nhũn ở kho lạnh | Giấy Cobb cao; ẩm; BCT không tính dư | Cobb giấy mặt; đơn có ghi kho lạnh không |
| Không mở được trên máy dựng thùng / dính chùm | Keo tràn, dính nắp; khe dán; đuôi cá; kích thước; cong tấm | DA-05, DA-12, DA-07, DA-08, TS-12 |
| Thùng xéo, không vuông khi dựng | Gấp không theo lằn; lằn lệch; cắt xéo | DA-09, TS-21, FX-19 |
| Mép dán bung khi đóng hàng | Keo; ép chưa đủ; vùng dán có mực/vecni | DA-04, DA-06 |
| Rách, nứt ở lằn khi gập nắp | Lằn sâu; giấy khô giòn; lằn ngược sóng | TS-18, BE-07, DA-11 |
| Màu khác lô trước | Mực khác lô; giấy kraft khác màu; độ nhớt | FX-07, OF-08; công thức mực lưu ở hồ sơ mã hàng |
| Sai chữ, sai mã vạch | Bản sai, lấy nhầm bản | FX-13, OF-15 (cấp 1 — nghiêm trọng) |
| Mã vạch không quét được | Ăn bông, bít chữ, in mờ | FX-10, FX-05 |
| Thiếu số lượng | Đếm, lẫn đơn, thất lạc | DA-15, CH-03, CH-05; phiếu nhận dạng pallet |
| Hộp offset phồng, bong lớp | Bồi | BO-04, BO-05 |
| Hộp offset cong | Bồi, ẩm | BO-09, OF-01 |

## 2. Triệu chứng tại xưởng

| Thấy | Ở máy | Gốc có thể ở | Mã |
|---|---|---|---|
| Tấm kẹt ở bàn nạp | In / bế / dán | Tấm cong từ tổ sóng | FX-01, FX-21, BE-14, DA-14 → TS-12 |
| Hằn sóng lên mặt in | In / bồi | Ván giặt ở máy sóng; ép quá tay | TS-16, BO-10 |
| Màu đậm nhạt từng vệt theo khổ | In | Trục không song song, anilox, dao gạt; tấm cong | FX-06, FX-09 |
| Đậm nhạt dần theo thời gian | In | Độ nhớt thay đổi (bay hơi, thêm nước) | FX-04, FX-05 |
| Khe dán thay đổi trong đơn | Dán | Lằn khâu trước; băng gấp | DA-08, FX-18 |
| Bế không đứt từng đoạn | Bế | Đệm/tấm cắt mòn, dao cùn, áp thiếu | BE-03 |
| Rác không rơi | Bế | Cao su đẩy, chốt tách rác | BE-09, BE-10 |
| Số máy đếm gấp đôi | Bế | Cảm biến thấy cả nhíp và tờ | BE-17 (chênh đếm, không phải lỗi) |
| Sóng giao khác số máy in nhận | Đối chiếu | Đơn vị đếm, tồn trước máy, mượn tấm | Nhóm 4, 5, 6 — `loi-khac-7-nhom.md` |
| Tấm mềm, bong khi xếp | Tổ sóng | Keo chưa chín, giấy ẩm | TS-11, TS-01 |
| Bọt khí dưới mặt giấy | Tổ sóng / bồi | Thiếu keo cục bộ, nhiệt | TS-14, BO-05 |

## 3. Sự cố không phải chất lượng

| Sự cố | Đi đâu |
|---|---|
| Máy hỏng, kêu, nóng, rò dầu, rung | `mp-bao-tri` |
| Tai nạn, suýt tai nạn, kẹt tay, bỏng | `mp-an-toan-lao-dong` |
| Phần mềm MES báo cảnh báo, số liệu đứng, không lưu được đơn | `mp-mes-su-dung` (phần cảnh báo) — báo Kỹ thuật, **ghi tay số liệu** trong lúc chờ |
| Đơn trễ, tắc kế hoạch | `mp-ke-hoach-san-xuat` |
