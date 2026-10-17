# Trợ lý trong MP MES (Quản lý, Kỹ thuật)

Nguồn: "Hướng dẫn Trợ lý — MP MES" (bản 1.8, 07/10/2026) [MP-MES]. Phần dưới là cách **dùng**; cài đặt máy chủ là việc của vai Kỹ thuật.

## 1. Trợ lý làm được gì

Cửa sổ hỏi – đáp trong MP MES: gõ câu hỏi như hỏi người trong xưởng, trợ lý tự tra nhật ký máy, kế hoạch, log và nhật ký thao tác của các trạm rồi trả lời
kèm con số, số phiếu, tên máy và giờ. **Trợ lý chỉ đọc**; riêng thêm/sửa/xoá **một dòng nhật ký** thì nó hiện **thẻ đề nghị**, người bấm nút trên thẻ mới ghi.

| | Cơ bản | Claude |
|---|---|---|
| Hỏi thế nào | Theo các kiểu câu có sẵn (bảng mục 2); gõ không dấu cũng được | Hỏi tự do, hỏi nối tiếp, hỏi "vì sao", so hai máy |
| Tốc độ | Dưới 3 giây | 20–40 giây một câu |
| Cần gì | Không cần Internet | Tài khoản MES vai **Kỹ thuật**, Internet, gói Claude đăng nhập ngay trong cửa sổ Trợ lý |
| Tên khách | Hiện tên thật, không gì rời khỏi máy | Tên khách, tên hàng đổi thành mã (KH-…, HG-…) trước khi gửi đi; màn hình tự đổi lại tên thật |

Ai thấy: **Quản lý** (chỉ Cơ bản) và **Kỹ thuật** (Cơ bản + Claude). Vận hành, KCS không có trợ lý.
Trợ lý **không có**: doanh thu, giá, lương, tồn kho giấy, ngày giao hàng ("Phần mềm chưa có số này"); không xếp lịch thay người; không sửa mạng, PLC, máy chủ.

## 2. Các kiểu câu Cơ bản hiểu

| Muốn biết | Hỏi ví dụ |
|---|---|
| Các trạm lúc này | "Hôm nay các trạm thế nào?" |
| Sản lượng, lỗi, giờ chạy | "Máy in 1 hôm qua chạy được bao nhiêu?" · "Máy dán 1 từ 01/09 đến 05/10 làm được bao nhiêu, lỗi bao nhiêu?" |
| Kế hoạch | "Kế hoạch hôm nay của máy dán 1" · "Kế hoạch 05/10 có bao nhiêu đơn?" |
| Sự cố | "Hôm qua MI1 có sự cố gì?" · "MI1 mất kết nối những lúc nào từ 24/09 đến 05/10?" |
| Log một khung giờ | "Lúc 11:05–11:12 ngày 04/10 MI1 log ghi gì?" |
| Đơn bất thường | "Soát đơn bất thường tuần này" |
| Một đơn cụ thể | "Đối chiếu đơn 765/9" |
| Ai làm gì | "Ai bấm gì ở MI1 hôm qua?" |
| Dữ liệu đủ không | "Dữ liệu tháng này có chỗ nào thiếu?" |

Ngày viết kiểu nào cũng nhận (hôm nay, hôm qua, tuần này, tháng 9, 04/10, "từ 01/10 đến 05/10"); máy gọi bằng mã (MI1, DT1) hoặc tên ("máy in 1",
"dán 2", "tổ sóng"); câu sau "còn MI2 thì sao" giữ ngày của câu trước. Thêm **"rồi xuất Excel"** cuối câu để ra file .xlsx (nút Mở thư mục báo cáo).

## 3. Đọc câu trả lời

Thứ tự: câu kết luận → **Đáng để ý** (việc nặng lên trước) → bảng số → **Sổ tay lỗi** (nghĩa là gì, thường do đâu, kiểm gì trước). Cột **Đã tra** ghi trợ lý
đã lấy số gì, máy nào, ngày nào, bao nhiêu dòng.

| Gặp chữ | Nghĩa là |
|---|---|
| **Chắc sai** | Bản ghi vi phạm luật không thể đúng (vd có 150 tờ mà phút chạy máy = 0) — cần sửa |
| **Nghi** | Bản ghi lạ nhưng có thể có lý do (vd hai đơn chồng giờ nhau) — cần người xem lại |
| không có tin | Trạm không gửi số về máy chủ (tắt hoặc mất mạng) — số trong dòng là số cũ |
| PLC giả lập | Số do phần mềm tự sinh khi thử, không phải số máy thật |
| **Không cộng các số này** | Máy in đếm tờ, máy dán đếm thùng, máy bế đếm nhịp × số con, tổ sóng đếm tấm và mét — trợ lý đưa từng số riêng |

## 4. Thêm, sửa, xoá một dòng nhật ký (Quản lý, Kỹ thuật)

| Việc | Gõ ví dụ | Phải có trong câu |
|---|---|---|
| Thêm | "thêm nhật ký phiếu 765/9 ngày 05/10 máy in 1 từ 7:30 đến 10:15 số nhịp 3000" | Phiếu, ngày, máy, sản lượng (máy in: số nhịp · thành phẩm: số lượng). Tổ sóng chưa thêm được |
| Sửa | "sửa nhật ký 694/9 ngày 04/10 máy in 1 số nhịp 3100" | Phiếu và ô cần đổi (sản lượng, giờ, ghi chú) |
| Xoá | "xoá nhật ký 765/9 ngày 05/10 máy in 1" | Phiếu và ngày |
| Khôi phục | "khôi phục nhật ký 765/9 ngày 05/10 máy in 1" | Phiếu — lấy lại dòng đã xoá trong 30 ngày, trên máy đã xoá |

- Đọc **thẻ đề nghị**: bản ghi sẽ bị đụng, ô nào đổi (đang ghi → sẽ ghi), dòng "tự tính", dòng "Lưu ý" màu cam. Bấm nút chính mới ghi; gõ "ok" **không** ghi gì.
- **Hoàn tác** = thẻ ngược lại, vẫn phải bấm.
- Giới hạn do phần mềm chặn: mỗi lần **một dòng**; trong **10 ngày** (cũ hơn chỉ Kỹ thuật); xoá tối đa **10 bản ghi/ngày/tài khoản**; thẻ hết hạn **2 phút**;
  ở trạm sản xuất chỉ với máy của trạm đó; không đụng kế hoạch.
- Trước mỗi lần sửa/xoá, phần mềm **sao lưu nguyên dòng** (ai, lúc nào, câu đã gõ) và ghi vào Báo cáo thao tác.
- KCS sửa nhật ký bằng tay ở tab Nhật ký như trước.

## 5. Lịch sử hỏi

Mỗi cuộc hỏi lưu theo tài khoản MES (đi theo tài khoản sang máy khác khi có máy chủ). Tìm (Ctrl+F), đổi tên (F2), xoá (Delete), "Xoá lịch sử…" theo
mốc 30/90 ngày. Trạm sản xuất dùng chung người dùng Windows thì ai mở được thư mục cũng đọc được → **hỏi ở máy văn phòng**.
