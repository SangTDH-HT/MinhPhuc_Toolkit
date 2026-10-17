# Tổ sóng — chạy đơn trên MP MES

Nguồn: Hướng dẫn chạy máy MP MES bản 2.0, 10/2026 [MP-MES]. Luật kế hoạch, ghép đơn, nhập lỗi: skill `mp-to-song` → `ke-hoach-va-ghi-so.md`.

## 1. Đăng nhập

Máy tính tổ sóng → tên mình → PIN 4 số; PLC xanh + số nhịp nhảy, Máy chủ xanh, góc phải đúng tên.
Đầu ngày bấm **Bắt đầu** trên **màn hình tại từng cụm sóng** — thẻ trạm viền vàng "chưa Bắt đầu" là trạm chưa đếm.

## 2. Kế hoạch, thêm đơn, ghép đơn

- ĐƠN HÀNG: kế hoạch hôm nay theo STT, máy chạy từ trên xuống.
- Đơn gấp chưa có: **Thêm đơn**. Sai số tấm, khổ: chọn đơn → **Sửa**. Đổi thứ tự: chọn đơn → **Lên / Xuống** (nhóm ghép đi nguyên khối).
- Phiếu dán pallet: **In phiếu** (in thẳng ra máy in của trạm).
- **Ghép đơn chạy chung cuộn giấy**: Trang chủ → **Ghép đơn** → tích các đơn **cùng giấy, cùng khổ** → **Ghép** → Đóng. Mỗi lần Ghép là một nhóm;
  trong nhóm, đơn trước đủ số thì tự lưu và chạy luôn đơn sau, **không cần bấm Start**.
- Góc màn báo "kế hoạch thay đổi": văn phòng vừa thêm, bớt, sửa đơn — đọc rồi tắt; Trang chủ tự đọc lại kế hoạch mỗi phút; nhóm ghép không rã.

## 3. Trang chủ — ba thẻ trạm

| # | Khung | Nội dung |
|---|---|---|
| 1 | **Dao chặt** (thẻ chính) | Đơn ở dao, số dao còn lại, đã chặt / kế hoạch |
| 2 | Nhân sự, **Dao bù**, tốc độ | Dao bù = tấm đã cắt từ trước (như "chạy trước") |
| 3 | Reset, Trước / Sau | Reset xoá số đếm trạm; Trước / Sau đưa trạm về đơn trước / sang đơn kế |
| 4 | **Sóng A/C/E** | Đơn, mét còn lại, nút Chạy; bấm dòng **mét lỗi** để nhập |
| 5 | **Sóng B** | Như trên |
| 6 | Ghi nhận lỗi | Lỗi của đơn đang ở dao |
| 7 | Đơn kế tiếp | Trạm nào đang ở đơn nào |
| 8 | Thời gian | Chạy, ngừng, chuẩn bị |

Chạy: bấm **Chạy** trên thẻ Sóng A/C/E và Sóng B (hoặc trên màn hình tại cụm) → **▶ Chạy dao** trên dải nút (hoặc nút Start ở dao); dao chạy thì nút
đổi thành **Dừng dao**. Dao chặt **đủ số dao** → phần mềm **tự lưu đơn** và đưa đơn kế vào dao; đơn ngoài nhóm ghép thì dao dừng chờ bấm Chạy.

## 4. Dừng dao, ghi lỗi, qua đơn bằng tay

- **❚❚ Dừng dao** → dao đứng tính **ngừng không kế hoạch**. Chờ giấy, hết việc, sửa máy: bấm **dòng lý do ngừng** ở khung Thời gian →
  *Dừng có kế hoạch* hoặc *Dừng bảo trì*, gõ lý do; xong bấm lại dòng đó → **Kết thúc**. (Tổ sóng không có nghỉ ca.)
- **Lỗi**: đổ rách, bong dộp, dập sóng, sáng biên, sai quy cách, sai kết cấu, lỗi khác — **gõ số khổ hỏng**; lúc lưu phần mềm nhân số tấm một khổ.
  Lỗi khác ghi mã **TS-xx** vào ghi chú.
- **Qua đơn khi chưa đủ** (hết giấy, khách bớt): **Lưu đơn ở dao** → *Lưu nhật ký rồi qua đơn*. *Qua đơn, không lưu* chỉ khi đơn chưa chặt tấm nào.

## 5. Tổ trưởng: xác nhận số tấm, phiếu, báo cáo

- Đơn đã lưu chờ **số tấm thực**: bấm **Nhập số lượng (n)** ở Trang chủ (n = số phiếu còn chờ), hoặc NHẬT KÝ → chọn bản ghi → **Xác nhận**.
- Sai giờ, nhân sự, số tấm: NHẬT KÝ → sửa trên khung Chi tiết → Lưu (**vận hành được sửa nhật ký tổ sóng**).
- **Phiếu nhận dạng**: Trang chủ → Phiếu nhận dạng → kiểm số tấm một pallet → In; in lại vài tờ: chỉnh Từ tờ / Đến tờ. Ô công đoạn tự tích theo kế hoạch.
- Cuối ca: NHẬT KÝ → Báo cáo ca → In ra giấy, ký tên.

## 6. Tình huống hay gặp

| Thấy gì | Làm gì |
|---|---|
| Thẻ trạm "Sắp hết đơn" (còi ở cụm kêu) | Chuẩn bị giấy cho đơn kế |
| Thẻ trạm viền vàng "chưa Bắt đầu" | Bấm Bắt đầu trên màn hình tại cụm |
| Lỡ chọn sai lý do dừng | Bấm dòng lý do ngừng ở khung Thời gian để đổi |
| Gõ nhầm mét lỗi ở màn cụm | Nhập số âm để trừ lại |
| Đơn chạy qua nửa đêm | Không cần làm gì: phần mềm đợi dao chặt xong đơn dở rồi mới sang kế hoạch ngày mới |
| Đèn đỏ, lưu lỗi | `canh-bao-va-su-co.md` |
