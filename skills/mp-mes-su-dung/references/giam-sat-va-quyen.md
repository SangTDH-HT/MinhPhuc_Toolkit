# Máy Giám sát, vai và quyền, Trợ lý

Nguồn: "Chức năng máy Giám sát xưởng" và "Tổng hợp chức năng các máy", MP MES bản 2.0, 10/2026 [MP-MES].

## 1. Vai và quyền

| Vai | Làm được |
|---|---|
| **Vận hành** (PIN) | Chọn đơn, chạy, dừng, khai lý do, ghi lỗi, lưu đơn, chuyển ngày, ngưng đơn, chuyển máy. Tổ sóng: thêm / sửa / đổi thứ tự / ghép đơn, xác nhận và sửa nhật ký sóng |
| **KCS** | Như Vận hành, thêm: **sửa nhật ký**, **thêm đơn gấp** |
| **Quản lý** | Sửa đơn, sửa / xoá nhật ký, máy Giám sát, bảng ca, tốc độ mục tiêu, Trợ lý. **Không chạy máy** (nút chạy mờ khi đăng nhập Quản lý) |
| **Kỹ thuật** | Mọi việc, cộng cấu hình kết nối, đổi máy của trạm, tài khoản |

Tài khoản: ai đăng nhập cũng đổi được mật khẩu của mình; Quản lý thêm được tài khoản Quản lý, KCS, Vận hành; Kỹ thuật thêm mọi vai; sửa/xoá tài khoản
chỉ Kỹ thuật. **Không chia sẻ PIN**; đổi người đứng máy thì Đăng xuất rồi người mới đăng nhập (tên người vận hành ghi theo tài khoản đang đăng nhập).

## 2. Máy Giám sát — xem cả xưởng, không ra lệnh cho máy

Máy Giám sát xem cả xưởng và **sửa dữ liệu trên máy chủ**, nhưng **không** chạy, dừng, chọn đơn, lưu đơn, không gõ ô lỗi, mực, chạy trước — những số đó
là của người đứng máy. Đăng nhập Quản lý hoặc Kỹ thuật.

**Toàn xưởng**: mỗi máy một thẻ — tình trạng, phiếu, người đứng máy, % đã làm, phút chạy / ngừng / chuẩn bị, khách, mã sản phẩm.
- Máy chạy: vạch tiến độ chạy sọc + chấm thở; máy đứng: đứng yên.
- **Mất tin**: quá 20 giây trạm không gửi số (số trên thẻ là số cũ). **Đã đóng phần mềm lúc …**: trạm tắt đàng hoàng. **Chưa mở ca hôm nay**.
- Thẻ tổ sóng: số của dao, tốc độ m/phút. Bấm thẻ để xem máy đó (Trang chủ giống trạm, nút lệnh mờ); về lại bằng nút Toàn xưởng.

**Đơn hàng** ở máy Giám sát:

| Nút | Làm gì | Ai |
|---|---|---|
| Thêm đơn | Đơn gấp chưa có trong kế hoạch, trạng thái Chờ, ghi chú "Thêm tại máy" | KCS trở lên |
| Sửa | Số lượng phải làm, số con, màu in, ghi chú (khách, tên hàng, mã hàng sửa trên ERP) | Quản lý trở lên |
| Chuyển máy | Đơn chưa chạy sang máy cùng loại (In 1 ↔ In 2, Dán 1 ↔ Dán 2, Bế 1 ↔ Bế 2) | đã đăng nhập |
| Lấy đơn ngày khác | Dời đơn chưa chạy từ ngày cũ về ngày đang xem | đã đăng nhập |
| Xuất Excel | Kế hoạch đang xem, có logo công ty | mọi người |

**Nhật ký**:

| Nút | Làm gì |
|---|---|
| Sửa bản ghi | Sửa số, giờ, ghi chú; số phụ thuộc tự tính lại — KCS trở lên |
| Xoá bản ghi | Xoá bản ghi sai — Quản lý trở lên |
| Thêm nhật ký | Ghi bù ca chạy lúc trạm mất điện, mất mạng hay thợ quên lưu — **chỉ ở máy Giám sát** |
| Hiệu suất | Đặt các máy cạnh nhau qua nhiều ngày: sẵn sàng × hiệu năng × chất lượng |
| Báo cáo ca – In | Tờ A4 tổng kết các bản ghi đang hiện, hoặc một bản ghi |
| So kế hoạch | Mỗi đơn kế hoạch so tổng mọi lượt đã làm: đủ, thiếu, thừa, đang dở, chưa chạy |

Tab Nhật ký xem theo **ngày** hoặc theo **phiếu** (phiếu = cộng mọi lượt của đơn — dùng khi đối chiếu).

**Dữ liệu** (Quản lý trở lên, chỉ đọc; Từ – Đến, Hôm nay / 7 / 30 ngày, Xuất Excel):
- **So kế hoạch** mọi máy trên một màn: số đơn đủ, thiếu, thừa, đang dở, chưa chạy; lọc chỉ đơn lệch.
- **Đơn cần xem lại**: bản ghi bị luật soát gắn cờ (có hàng mà không có giờ, tốc độ vô lý, giờ không khớp…) — Mở bản ghi, Hỏi Trợ lý, Đã xem.
- **Sức khoẻ dữ liệu**: điểm từng máy và các bản ghi cần sửa.

**Cài đặt → Báo cáo thao tác**: ai đã bấm gì, lúc nào, sửa gì từ số nào sang số nào; lọc theo ngày, xuất Excel.
Bảng ca và tốc độ mục tiêu sửa **ở trạm của máy** (Quản lý trở lên), máy Giám sát không có.

## 3. Trợ lý (nút tròn xanh góc phải)

Hỏi bằng tiếng Việt, ví dụ: "đơn nào thiếu so với kế hoạch hôm qua", "hôm qua MI1 có sự cố gì", "đối chiếu đơn 801/10".
Quản lý, Kỹ thuật nhờ Trợ lý thêm / sửa / xoá một dòng nhật ký: Trợ lý hiện **thẻ đề nghị**, bấm nút trên thẻ mới ghi. Trợ lý **không sửa kế hoạch**.

## 4. Báo cáo ca — ai ký

Cuối ca: NHẬT KÝ → Báo cáo ca → In ra giấy → **người vận hành, tổ trưởng, quản đốc** ký tên.
