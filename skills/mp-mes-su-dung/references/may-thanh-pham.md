# Máy thành phẩm (máy dán 1/2, máy bế 1/2, máy bồi) — chạy đơn trên MP MES

Nguồn: Hướng dẫn chạy máy MP MES bản 2.0, 10/2026 [MP-MES]. Ba loại máy dùng chung một Trang chủ thành phẩm; khác nhau ở đơn vị đếm và phiếu pallet.

| Máy | Một lần đếm | Lỗi gõ theo | Phiếu nhận dạng |
|---|---|---|---|
| Máy dán tự động 1, 2 | 1 thùng đã dán | thùng | **Có** (chừa tờ cuối) |
| Máy bế tự động 1, 2 | 1 nhịp dao (sản phẩm = nhịp × số con) | con | Không |
| Máy bồi | 1 tấm đã bồi | tấm | Không |

## 1. Đăng nhập, nhìn đèn

Như máy in: PIN 4 số; PLC xanh + số nhịp nhảy; Máy chủ xanh; góc phải đúng tên mình.

## 2. Chọn đơn

ĐƠN HÀNG → bấm **vòng tròn** trên thẻ đơn → trả lời **Có** ở câu "Chọn đơn … làm đơn đang chạy?". Đơn đang chạy trước tự về Chờ;
đơn đã xong bị gạch, không chọn được.
**Máy dán**: hộp **Phiếu nhận dạng** tự mở → kiểm tổng số thùng của lô và **số thùng một pallet** → **In … tờ đầu**. **Tờ cuối để dành** tới lúc Lưu đơn.

## 3. Chạy đơn

Canh khuôn, lên keo, chạy thử xong → TRANG CHỦ → **▶ Chạy đơn**. Máy dán **không có nút Start ngoài máy** — lệnh chạy chỉ từ phần mềm.
Nút mờ = chưa chọn đơn / hết đơn / đang đăng nhập Quản lý (chỉ xem).

## 4. Trong lúc chạy

| Khung | Nội dung |
|---|---|
| Tiến độ | % và số đã làm trên kế hoạch (đơn vị sản phẩm) |
| Tốc độ | Tốc độ (nhịp/phút), đã làm, còn lại, so với đơn đặt |
| Thời gian | Chạy máy, ngừng máy, **chuẩn bị** (canh khuôn, lên keo, chạy thử) |
| Chạy trước | Phần đã làm mà bộ đếm không có; chọn lại đơn đã ngưng / chuyển ngày thì **ô này tự cộng** |
| Ghi nhận lỗi | Sóng · In · Bế · Định hình · Khác — bấm + cho mỗi sản phẩm hỏng |
| Vật tư | Keo dán, keo bôi, kẽm đã dùng |

## 5. Dừng máy

**❚❚ Tạm dừng** → chọn lý do (4 loại như máy in; ngừng có kế hoạch và bảo trì phải gõ lý do). Dừng ngắn (kẹt thùng, chỉnh dao) cũng dùng nút này.

## 6. Lưu đơn

Tạm dừng cho máy đứng → **đếm lại thùng cuối, ghi lỗi cho đủ** → ✓ **Lưu đơn** (lưu ngay, báo "Đã lưu nhật ký phiếu …", xoá bộ đếm, đưa đơn kế lên).
Máy dán: **in tờ cuối** phiếu nhận dạng với số thùng thật (Phiếu nhận dạng → In tờ cuối).
- **Máy thành phẩm không tự lưu** — đủ số rồi vẫn phải bấm Lưu đơn.
- Đã lưu là đơn xong, kể cả thiếu số.

## 7. Nhường máy hoặc hết ca khi đơn chưa xong

**Ngưng đơn** (nhường máy cho đơn gấp, chờ giấy):
1. Chọn *Chạy tiếp trong hôm nay* — đơn về Chờ, giữ số đã làm; chọn lại là chạy tiếp; xong cả đơn chỉ ra **một bản ghi** (ghi chú "Chạy 2 lần: …").
   Hoặc *Mai mới chạy tiếp* — lưu phần đã làm, đơn lên đầu kế hoạch mai, **số kế hoạch giữ nguyên**.
2. Câu thứ hai: **từ giờ tới đơn kế máy làm gì** — chạy đơn khác ngay / máy nghỉ / máy hỏng (để quãng chờ vào đúng cột, không kéo tụt tốc độ đơn sau).

**Hết ca**: Tạm dừng → **Chuyển ngày** → *Chỉ đơn đang chạy* hoặc *Cả các đơn chưa xong*; mai chọn đơn là ô Chạy trước tự cộng phần đã làm.
**Sáng mở máy hỏi "Lưu bù"**: hôm qua còn phần chưa vào sổ — chọn đúng: chạy tiếp hôm nay / đơn đã xong / để sau.
Báo cáo ca: NHẬT KÝ → Báo cáo ca → In ra giấy, ký tên.

## 8. Phiếu nhận dạng lô hàng (máy dán) — luật chia pallet

- Biểu mẫu **SX-QT01-BM02/06**, A5 dọc, mỗi pallet một tờ; số thùng một pallet là **một số chung cả xưởng** (sửa ngay trên hộp thoại khi mặt hàng khác).
- In trước **N−1 tờ**, **luôn chừa tờ cuối** (kể cả chia chẵn) — Lưu đơn biết số thật mới in tờ cuối.
- Ô số pallet ghi **thứ tự / tổng** (3/12). Bốn ô ký (Người kiểm tra · QC sản phẩm · QC giấy tấm · Kiểm tra) để trống cho người thật ký.
- Chỉ **in ra giấy** mới tính là đã in (lưu PDF không đánh dấu).

## 9. Tình huống hay gặp

| Thấy gì | Làm gì |
|---|---|
| Máy hỏng, chạy đơn ở máy kia | ĐƠN HÀNG → chọn đơn (chưa chạy) → **Chuyển máy** (Dán 1 ↔ Dán 2, Bế 1 ↔ Bế 2) |
| Máy bế số đếm gấp đôi số tờ | Đếm đôi do cảm biến (BE-17) — không phải hàng hư; báo Kỹ thuật, ghi chú khi lưu |
| Lỡ chọn sai lý do dừng | Bấm khung Ngừng máy để đổi |
| Đèn đỏ, lưu lỗi | `canh-bao-va-su-co.md` |
