# Máy in (Máy In 1, Máy In 2, Máy In Offset) — chạy đơn trên MP MES

Nguồn: Hướng dẫn chạy máy MP MES bản 2.0, 10/2026 [MP-MES].

## 1. Đăng nhập, nhìn đèn

Mở MP MES trên máy tính của máy, bấm tên mình, gõ **mã PIN 4 số** (sai 5 lần liền khoá 5 phút). Nhìn thanh trên cùng:
- **PLC xanh**, số nhịp nhảy liên tục → phần mềm đang đọc được máy.
- **Máy chủ xanh** → lưu được đơn. Đèn giữa: Máy chạy / Máy dừng.
- Góc phải đúng tên mình (sai thì Đăng xuất ở thanh trái rồi vào lại). Đèn vàng/đỏ → `canh-bao-va-su-co.md`.

## 2. Chọn đơn

ĐƠN HÀNG (thanh trái) → danh sách kế hoạch hôm nay, đơn đầu tiên ở trên → bấm **vòng tròn** trên thẻ đơn → tờ phiếu **Bắt đầu sản xuất** hiện ra:
đọc kỹ số lượng, màu mực, **mã bảng in và chỗ cất** → **Chạy đơn này** (đơn đang chạy trước tự về Chờ).
Trên tờ phiếu còn: ô VỊ TRÍ để khai chỗ cất bảng in (chữ đỏ CHƯA KHAI); tích **gộp các phiếu giống hệt** (thẻ có nhãn GỘP ĐƯỢC) để chạy liền;
tích **In 2 mặt**; xem layout.

## 3. Chạy máy

Pha mực, canh màu, chạy thử xong → TRANG CHỦ → **▶ Chạy máy**. Từ lúc bấm, máy đứng là **ngừng**; trước lúc bấm là **pha mực**.
Nút Start ngoài máy cũng chạy được và **không xoá số đếm** (Máy In Offset không có nút ngoài máy).
Nút Chạy máy mờ = chưa chọn đơn / kế hoạch hết đơn / đang đăng nhập tài khoản Quản lý (chỉ xem).

## 4. Trong lúc chạy

| Khung | Làm gì |
|---|---|
| Tiến độ | Đã chạy bao nhiêu nhịp (tờ in) trên kế hoạch |
| Tốc độ | Tốc độ, số còn lại, giờ dự kiến xong |
| Thời gian | Chạy máy, ngừng máy, pha mực — **bấm khung ngừng máy để đổi lý do dừng** |
| Chạy trước | Chỉ gõ khi đơn đã chạy một phần mà bộ đếm không có (vd lượt trước). **Gõ bằng nhịp** |
| Ghi nhận lỗi | Bấm + cho mỗi tờ hỏng. **Thử máy** = tờ chạy thử trước khi bấm Chạy máy. Gõ theo **tờ in**, không nhân số con |
| Trạm mực | 6 trạm (offset 5): gõ kg mực và độ nhớt (giây) từng màu |
| Nhân sự | Số người đứng máy |

Lỗi không có ô → ô **Khác** và ghi **mã FX-xx / OF-xx** vào ghi chú (skill `mp-xu-ly-su-co`).

## 5. Dừng máy — bấm Tạm dừng, chọn lý do

| Chọn | Khi nào |
|---|---|
| Ngừng không kế hoạch | Kẹt giấy, chỉnh máy, chờ người, hư nhỏ — mọi lần dừng không lường trước |
| Ngừng có kế hoạch | Chờ giấy, chờ khách duyệt mẫu, hết việc — **phải gõ lý do** |
| Nghỉ ca | Nghỉ trưa, nghỉ chiều — chỉ tính trong giờ nghỉ của bảng ca; ngoài giờ nghỉ chọn mục này vẫn tính ngừng |
| Bảo trì | Sửa máy, thay chi tiết — **phải gõ lý do**, bỏ trống là ngừng không kế hoạch |

Bấm **Thôi, máy chạy tiếp** (hoặc Esc) là không dừng. Chạy lại: ▶ Chạy máy (bấm chạy lại là hết bảo trì).

## 6. Lưu đơn

✓ **Lưu đơn** → hộp Lưu nhật ký hiện sản lượng, lỗi, giờ chạy, giờ ngừng — xem lại cho đúng. Đơn **cán màng**: tích ô cán màng, chọn **lượt in**
(hàng còn đi cán màng, đơn chưa xong) hay **lượt cắt rãnh** (đơn xong hẳn). Bấm **Lưu nhật ký** → phần mềm ghi sổ xong mới dừng máy, xoá bộ đếm,
đưa đơn kế lên → hộp tốc độ bình quân → **Đã xem**.
- **Đã lưu là đơn xong**, kể cả thiếu số.
- Đủ số mà máy đứng yên: hộp đếm ngược **90 giây** rồi tự lưu.

## 7. Hết ca, đơn chưa xong

**Tạm dừng** trước, rồi **Chuyển ngày**: *Chỉ đơn đang chạy* (lưu phần đã chạy, đơn lên đầu kế hoạch mai) hoặc *Cả các đơn chưa xong* (dời cả loạt,
giữ thứ tự). Cuối ca: NHẬT KÝ → **Báo cáo ca** → In ra giấy → người vận hành, tổ trưởng, quản đốc ký.

## 8. In 2 mặt

Tích **In 2 mặt** ở tờ phiếu (ghi chú có "in 2 mặt"/"hai mặt" thì tự tích sẵn). In hết mặt 1 → hộp **Xong mặt 1** đếm 90 giây rồi tự sang mặt 2
(phần mềm dừng máy, số về 0, "nhịp mặt 2") → lật chồng, thay bản, mực → Chạy máy → mặt 2 đủ số → lưu **một bản ghi**. Quên tích: nút **In 2 mặt**
trên dải nút hoặc **In tiếp mặt 2** trong hộp "Đơn đã chạy đủ". Sang nhầm: **Về mặt 1**.

## 9. Tình huống hay gặp

| Thấy gì | Làm gì |
|---|---|
| Lỡ chọn sai lý do dừng | Bấm khung Ngừng máy (cột thời gian bên phải Trang chủ) để đổi |
| Đơn nằm ở ngày hôm qua | Hôm qua quên Chuyển ngày: ĐƠN HÀNG → **Lấy đơn ngày khác** → chọn ngày → tích đơn |
| Máy hỏng, cần chạy đơn ở máy kia | ĐƠN HÀNG → chọn đơn (chưa chạy) → **Chuyển máy** sang Máy In 2 (chỉ giữa In 1 ↔ In 2) |
| Lưu đơn báo lỗi | Số liệu còn nguyên; có mạng lại bấm Lưu đơn lần nữa |
| Máy tính bỏ túi | Nút ở thanh icon trái; số kiểu Việt Nam (dấu phẩy thập phân), Enter = bằng, Esc = xoá, `%` = chia 100 |
