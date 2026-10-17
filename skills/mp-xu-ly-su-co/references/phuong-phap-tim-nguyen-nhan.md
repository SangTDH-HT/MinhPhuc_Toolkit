# Phương pháp tìm nguyên nhân gốc

Các công cụ dưới đây là phương pháp chất lượng chuẩn (ISO 9001 mục 10.2, 8D) [KN ngành], áp vào dữ liệu và mã lỗi của Minh Phúc.

## 1. Mô tả vấn đề — 5W2H (làm trước, mất 5 phút)

| Câu | Ví dụ |
|---|---|
| What — lỗi gì (mã lỗi) | FX-04 in nhoè, lem chữ |
| Where — máy nào, chỗ nào trên tấm | Máy In 2, trạm màu 2, mép trái |
| When — từ lúc nào | Sau giờ nghỉ trưa, đơn 359/10 |
| Who — ca, người vận hành | Ca hành chính |
| Which — đơn, mã hàng, lô giấy, lô mực | Phiếu 359/10, mực đỏ lô mới |
| How many — bao nhiêu (tấm, %) | 35 tấm / 1.200 |
| How — phát hiện thế nào | KCS kiểm định kỳ |

Kèm ảnh, mẫu lỗi và **mẫu đạt** để so.

## 2. Pareto — sửa cái lớn trước

Gom số lỗi theo mã (phiếu đếm, nhật ký MES) trong 1–2 tuần → xếp giảm dần → 20 % mã thường chiếm ~80 % số hư.
Chỉ làm dự án cải tiến cho 2–3 mã đầu. Máy tính: `python -m mptinh pareto --file phieu-dem.csv`.

## 3. Xương cá theo 6 nhóm Minh Phúc

Đầu cá = mã lỗi. Sáu xương = **NVL · Máy móc – khuôn bản · Vận hành · Khâu trước · Kỹ thuật – kế hoạch · Kho – vận chuyển**.
Điền giả thuyết từ cột "nguyên nhân thường gặp" của mã lỗi và bảng tra sâu của tổ máy; gạch bỏ dần bằng **kiểm chứng** (đổi cuộn, đo, thử).

## 4. 5 Why — hỏi "vì sao" tới khi gặp thứ sửa được

Ví dụ 1 — **DA-04 bung mép dán** (máy dán):
1. Vì sao bung? → Keo không bám vào tai dán.
2. Vì sao không bám? → Keo khô trước khi ép (bề mặt keo đã đóng màng).
3. Vì sao khô sớm? → Độ nhớt keo cao, ống keo nóng (đường ống đi dưới mái tôn, chiều nắng), thợ tăng áp bù.
4. Vì sao không phát hiện? → Không có bước đo độ nhớt keo đầu ca/giữa ca; thùng đầu đơn không xé thử.
5. Vì sao? → SOP máy dán chưa có điểm kiểm keo.
→ Nguyên nhân gốc: **Kỹ thuật – kế hoạch** (thiếu chuẩn) + Máy móc (ống keo nóng). Hành động: đo độ nhớt đầu ca, che/đi lại ống keo, thêm xé thử vào
phiếu kiểm đầu đơn, áp lực keo theo tốc độ.

Ví dụ 2 — **TS-12 tấm cong lên** (tổ sóng):
1. Vì sao cong? → Mặt trên co nhiều hơn mặt dưới (mặt trên khô hơn).
2. Vì sao lệch ẩm? → Cuộn giấy mặt trên mới nhập, ẩm thấp hơn cuộn đáy ~2 %.
3. Vì sao không chỉnh nhiệt bù? → Thợ không đo ẩm cuộn trước khi lắp.
4. Vì sao? → Không có máy đo ẩm cầm tay tại giá cuộn / không có quy định.
→ Gốc: Vận hành + Kỹ thuật (quy trình). Hành động: đo ẩm hai cuộn mặt trước khi ghép, bảng chỉnh góc bao theo chênh ẩm.

Ví dụ 3 — **FX-04 in nhoè sau giờ nghỉ trưa** (máy in):
1. Vì sao nhoè? → Mực loãng.
2. Vì sao loãng? → Trước nghỉ trưa mực đặc lại (nước bay hơi), thợ thêm nước; sau nghỉ mực khuấy lại thành loãng.
3. Vì sao thêm nước không đo? → Không có cốc Ford ở máy / không có thói quen đo.
→ Gốc: Vận hành. Hành động: đo độ nhớt sau mỗi lần nghỉ, ghi vào phiếu; mức 20–25 s cốc Ford 4.

## 5. Kiểm chứng — đừng tin nguyên nhân chưa kiểm

| Cách | Khi nào |
|---|---|
| Đổi một biến, giữ biến khác | Nghi giấy: đổi cuộn; nghi mực: thay mực mới |
| Đo trước – sau | Độ dày tấm trước/sau máy in; nhiệt hai đầu trục |
| Tái hiện | Chạy lại đúng điều kiện cũ có ra lỗi không |
| Đối chiếu dữ liệu | MES: lỗi tăng sau mốc nào (đổi ca, đổi đơn, sửa máy) |

## 6. 8D — khi khách khiếu nại hoặc lỗi lớn

D1 lập nhóm · D2 mô tả (5W2H) · D3 ngăn chặn tạm thời (chọn lại lô, khoanh hàng tồn, báo khách) · D4 nguyên nhân gốc (sinh ra **và** lọt qua kiểm) ·
D5 chọn hành động khắc phục · D6 thực hiện và kiểm chứng · D7 phòng ngừa lặp lại (SOP, phiếu kiểm đầu đơn, đào tạo, FMEA) · D8 ghi nhận nhóm.
Mẫu: `templates/bao-cao-8d.md`.

## 7. Sai lầm hay gặp

- Sửa nhiều biến cùng lúc → không biết cái nào có tác dụng.
- Đổ lỗi máy sau khi chưa kiểm phép thử / chưa kiểm khâu trước.
- Ghi "Lỗi khác" không mã → mất dữ liệu cho Pareto.
- Dừng ở "do thợ" — hỏi tiếp vì sao thợ làm sai (thiếu chuẩn? thiếu dụng cụ? thiếu đào tạo?).
