# Làm mẫu, duyệt mẫu, chuyển đơn vào sản xuất

## 1. Sáu bước từ yêu cầu tới giao hàng [MP-Web]

1. Gửi yêu cầu (form báo giá hoặc Zalo OA) kèm 5 thông tin.
2. Nhận tư vấn và báo giá trong 4 giờ làm việc.
3. **Làm mẫu** để khách kiểm kích thước và bản in.
4. **Duyệt mẫu**: khách cho hàng thật vào thử — độ vừa, độ cứng, màu in; cần chỉnh thì chỉnh ở bước này.
5. Sản xuất và kiểm tra chất lượng (QC đo độ nén, độ bục…).
6. Giao hàng theo lịch.

Sai lầm: đặt sát ngày cần hàng, **không còn thời gian duyệt mẫu**.

## 2. Mẫu in kỹ thuật số [MP-Web]

- **Không khuôn, không bản**: đổi thiết kế chỉ là đổi file → sửa mẫu nhanh, rẻ; in được nhiều phương án trong một lần (dữ liệu biến đổi).
- **Đúng vật liệu thật**: cùng loại giấy mặt và sóng dự kiến cho hàng loạt.
- Kiểm: kích thước và dung sai (đặt sản phẩm vào, nắp gài, lằn gấp, xếp phẳng), màu dưới ánh sáng thật (logo, font, vùng phủ), cảm nhận chất liệu và gia công
  (cán màng, ép kim, UV).
- Máy in KTS: ≥ 2.000 m²/8 giờ [MP-HSNL].

## 3. Chuyển đơn mới vào sản xuất — danh sách bàn giao

| Mục | Ai | Ghi ở đâu |
|---|---|---|
| Quy cách đã duyệt (kiểu hộp, lọt lòng, sóng, giấy từng lớp, hướng sóng, mối nối) | Kinh doanh + Thiết kế | Hồ sơ quy cách mã hàng (`templates/ho-so-quy-cach-ma-hang.md`) |
| Mẫu duyệt có chữ ký (kết cấu + màu) | Kinh doanh | Lưu tại KCS / phòng mẫu |
| File in đã duyệt, số màu, Pantone | Thiết kế | Bản in BI/BK; nhãn FSC đã duyệt nếu có |
| Bản vẽ khuôn bế | Thiết kế | Khuôn KB…; kiểm khuôn khi nhận |
| Yêu cầu chất lượng đặc biệt (BCT mục tiêu, Cobb, dung sai chặt cho máy dựng thùng, kết quả theo lô) | Kinh doanh | Lệnh SX + kế hoạch kiểm |
| FSC (loại tuyên bố) / tiếp xúc thực phẩm | Kinh doanh | Lệnh SX |
| Đóng gói: số thùng/pallet, kiểu pallet, nhãn | Kinh doanh + Kho | Phiếu nhận dạng, lệnh SX |
| Ghi chú "**mới**" trên kế hoạch | Kế hoạch | Để xưởng biết chạy mẫu trước (MES tự nhận "hàng mới") |

Đơn **lặp lại**: kiểm hồ sơ mã hàng, khuôn và bản còn tốt, giấy còn đúng loại — "lô sau giống lô trước".

## 4. Khách khiếu nại — phía kinh doanh

1. Ghi nhận đủ: mã hàng, ngày giao/số lô, số lượng lỗi, **ảnh**, mẫu lỗi, điều kiện dùng (kho lạnh? xếp mấy tầng? máy dựng thùng?).
2. Chuyển KCS truy ngược (phiếu → MES → QC → lô giấy) — skill `mp-kcs-chat-luong`.
3. Trả lời khách trong thời hạn đã cam kết: ngăn chặn tạm thời (đổi hàng, chọn lại) → nguyên nhân → khắc phục (8D).
4. Cập nhật hồ sơ quy cách mã hàng để lỗi không lặp.
