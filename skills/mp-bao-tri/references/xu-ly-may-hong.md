# Xử lý máy hỏng

## 1. Trình tự (mọi máy)

| Bước | Ai | Việc |
|---|---|---|
| 1 | Thợ đứng máy | Dừng máy an toàn; trên MES bấm **Tạm dừng → Bảo trì, gõ lý do** (tổ sóng: dòng ngừng → Dừng bảo trì) |
| 2 | Thợ | Báo bảo trì: máy, hiện tượng, lúc nào, đã thấy gì (ảnh, tiếng, mùi); nút **Chép cho Kỹ thuật** nếu là cảnh báo phần mềm |
| 3 | Bảo trì | **Khoá năng lượng (LOTO)**: điện, khí, hơi, thuỷ lực, trọng lực — treo thẻ tên người (skill `mp-an-toan-lao-dong`) |
| 4 | Bảo trì | Chẩn đoán: hỏi thợ, xem sổ máy (đã hỏng kiểu này chưa), kiểm theo thứ tự đơn giản → phức tạp |
| 5 | Bảo trì | Sửa; thay phụ tùng; ghi phụ tùng dùng |
| 6 | Bảo trì + thợ | Gỡ khoá, chạy thử, kiểm **sản phẩm đầu tiên** sau sửa (sửa máy có thể đổi lằn, áp, màu) |
| 7 | Thợ | Bấm chạy lại trên MES (**bấm chạy là hết bảo trì**) |
| 8 | Bảo trì | Ghi **sổ lý lịch máy**: hiện tượng, nguyên nhân gốc, việc đã làm, phụ tùng, thời gian dừng, người sửa |

Máy hỏng lâu mà đơn gấp: chuyển đơn **chưa chạy** sang máy cùng loại (In 1 ↔ In 2, Dán 1 ↔ Dán 2, Bế 1 ↔ Bế 2).

## 2. Ghi đúng trên MES

- Có lý do → cột **Bảo trì** (không trừ hiệu suất tổ máy). Không lý do → **ngừng không kế hoạch** (trừ hiệu suất).
- Dừng ngắn sửa vặt (kẹt giấy, chỉnh) → ngừng không kế hoạch — đúng bản chất; nếu lặp nhiều sẽ bật **SX-22 máy dừng vặt liên tục**.
- Lỗi sản phẩm do máy hỏng → ghi đúng ô lỗi, nhóm nguyên nhân **Máy móc – khuôn bản**.

## 3. Chỉ số bảo trì [KN ngành]

| Chỉ số | Công thức | Dùng để |
|---|---|---|
| MTBF | Tổng thời gian chạy ÷ số lần hỏng | Máy nào hay hỏng |
| MTTR | Tổng thời gian sửa ÷ số lần hỏng | Sửa nhanh hay chậm (thiếu phụ tùng? thiếu tài liệu?) |
| Tỷ lệ bảo trì kế hoạch | Giờ bảo trì kế hoạch ÷ tổng giờ bảo trì | Mục tiêu tăng dần (phòng ngừa thay cho chữa cháy) |
| Thời gian dừng do bảo trì / tháng | Từ cột Bảo trì trên MES | Theo máy, theo bộ phận |

Nguồn dữ liệu: cột Bảo trì + lý do trên nhật ký MES, sổ lý lịch máy.

## 4. Khi cần hãng / dịch vụ ngoài

Chuẩn bị: ảnh tem nhãn (hãng, model, số máy, năm), ảnh/video hiện tượng, mã lỗi trên màn hình máy (nếu có), lịch sử sửa. Lò hơi, bình áp lực, xe nâng,
thang nâng: kiểm định bởi đơn vị có chứng chỉ theo quy định an toàn.
