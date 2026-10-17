# Vật tư phụ: keo, mực, màng, bản, khuôn, dây đai

Mỗi vật tư một dòng: dùng ở đâu, chỉ tiêu nhận hàng, bảo quản, lỗi khi vật tư kém. Thông số vận hành chi tiết nằm ở skill của từng tổ.

| Vật tư | Dùng ở | Nhận hàng / chỉ tiêu | Bảo quản | Lỗi khi kém (mã MP) |
|---|---|---|---|---|
| **Tinh bột** (bắp/sắn) | Bếp keo tổ sóng | Loại, độ ẩm, COA; mỗi lô thử nấu một mẻ đo độ nhớt, điểm gel | Khô, kê cao, FIFO | Bong lớp, keo chưa chín (TS-09, TS-11) |
| **Xút (NaOH)** | Bếp keo | Nồng độ, loại vảy/dung dịch | Kín, khu hoá chất, có SDS; **ăn da** — găng, kính, nước rửa mắt | Điểm gel sai → bong keo |
| **Borax** | Bếp keo (chất tạo liên kết, tăng độ dính) | Loại, COA | Khô, kín | Keo kém dính |
| **Mực gốc nước** | Máy In 1, 2 | Màu so mẫu chuẩn, độ nhớt, pH (8,5–9,5); SDS | Kín nắp, tránh nắng và đông; quay vòng lô cũ trước | Sai màu, nhoè, mờ, chấm mực (FX-04…09); "mực kém, khác lô" thuộc nhóm NVL |
| **Mực offset** | Máy In Offset | Màu, lô | Kín, tránh nắng | Đậm nhạt, sai màu (OF-07, OF-08) |
| **Dung dịch máng nước, bột chống dính** | Máy In Offset | pH, độ dẫn điện theo hãng | Kín | Bẩn nền, dính mặt sau (OF-06, OF-09) |
| **Keo dán thùng** (keo nước PVA hoặc keo nhiệt) | Máy dán 1, 2 | Loại keo, độ nhớt, thời gian khô | Không để đông lạnh / quá nóng; kín | Bung mép dán, keo khô nhanh (DA-04, DA-06) |
| **Keo bồi** | Máy bồi | Loại, độ nhớt | Kín, FIFO | Bong bồi, phồng rộp, cong vênh (BO-04, BO-05, BO-09) |
| **Màng cán OPP/PE** (bóng, mờ) | Máy cán màng | Độ dày, loại, độ bám (corona) | Tránh nắng, bụi | Bong màng, nhăn, bọt (OF-16) |
| **Bản flexo photopolymer + băng dán bản** | Máy In 1, 2 | Độ dày, độ cứng, kích thước; băng xốp 1,1–2,6 mm | Treo/đặt phẳng, tránh nắng, hoá chất mạnh (bản trương nở) | Mất nét, bong bản, ăn bông (FX-10…12) |
| **Bản kẽm offset** | Máy In Offset | Kích thước, độ phơi | Kệ riêng kho bản kẽm (mã BK…) | Bản mòn, trầy (OF-14) |
| **Khuôn bế + cao su đẩy** | Máy bế 1, 2, bế tròn | Kiểm khi nhận và khi trả về kho (mã KB…) | Kệ khuôn đúng vị trí | Bế không đứt, rác kẹt, dao gãy, cao su bung (BE-03, BE-10…12) |
| **Dây đai, băng keo** | Máy dán (bó), đóng kiện | Lực kéo đứt, độ rộng | Khô | Bó lỏng, bung khi vận chuyển (DA-16) |
| **Màng quấn pallet** | Kho thành phẩm | Độ dày, độ giãn | | Ngã pallet (CH-01) |

Ghi chú:
- Keo tinh bột kiểu **Stein-Hall** gồm tinh bột sống, phần tinh bột đã hồ hoá (chất mang), xút và borax trong nước. Kiểm mỗi mẻ: độ nhớt,
  điểm gel, độ dính, nhiệt độ, thử iốt. [Chuẩn: NZQA 40340] Chi tiết: skill `mp-to-song`.
- Mực nước: pH 8,5–9,5, độ nhớt 20–25 giây cốc Ford số 4; pha nước xong đo lại pH. [Converter] Chi tiết: skill `mp-in-flexo`.
- Hoá chất (xút, mực, dung môi rửa, keo) phải có **SDS** tiếng Việt tại nơi dùng (skill `mp-an-toan-lao-dong`).
- Đơn hộp tiếp xúc thực phẩm: mực, keo, màng phải có xác nhận phù hợp tiếp xúc thực phẩm (skill `mp-fsc-iso-attp`).
- Danh sách nhà cung cấp mực, bản, keo, màng, khuôn của Minh Phúc **chưa có trong repo** — bổ sung vào `data/nha-cung-cap.csv`.
