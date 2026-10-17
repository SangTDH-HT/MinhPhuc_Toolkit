---
name: mp-kcs-chat-luong
description: >
  KCS / QC của Minh Phúc theo chuẩn: điều kiện thử 23 °C/50 % RH, phép thử giấy – tấm – thùng và số hiệu ISO/TAPPI/FEFCO/TCVN
  (BCT ISO 12048, ECT ISO 3037, RCT ISO 12192/TCVN 6896, bục ISO 2759, Cobb ISO 535, định lượng ISO 536…), thiết bị phòng QC,
  phân loại lỗi FEFCO (1, 2A, 2B, 3), lấy mẫu AQL theo ISO 2859-1, dung sai kích thước, khe dán, đuôi cá, chồng màu, mối dán ≥ 80 % xơ,
  IS 2771, kiểm đầu đơn, kiểm công đoạn, kiểm xuất hàng, hồ sơ BCT/ECT theo lô, xử lý hàng không phù hợp, khiếu nại khách, ISTA,
  quan hệ số đo QC ↔ chỉnh máy. Dùng khi lập kế hoạch kiểm, kiểm lô, viết phiếu kết quả, trả lời khách về tiêu chuẩn, xử lý khiếu nại.
---

# mp-kcs-chat-luong — đo bằng máy, không chỉ bằng cảm quan

Minh Phúc tự nhận "kiểm soát chất lượng bằng máy đo, không chỉ bằng cảm quan"; phòng QC có máy nén thùng, nén cạnh, nén vòng, máy bục,
dụng cụ Cobb, cân định lượng, máy kéo; QC lấy mẫu **từng lô**, khách KCN nhận **hồ sơ BCT/ECT theo lô**. ISO 9001:2015 (SGS). [MP-Web]

## Ba câu hỏi QC phải trả lời

1. **Đúng quy cách không?** Kích thước, kiểu hộp, sóng, hướng sóng, giấy, in — so lệnh sản xuất và mẫu duyệt.
2. **Đủ bền không?** BCT, ECT, bục, bám keo, Cobb — đo bằng máy, theo chuẩn.
3. **Đẹp và chạy được trên máy của khách không?** Lỗi in, chồng màu, mép cắt, khe dán, độ phẳng — nhất là khi khách dựng thùng bằng máy.

## Bảng tham chiếu

| Cần gì | Đọc |
|---|---|
| Phép thử nào, chuẩn nào, khí hậu chuẩn, thiết bị | [references/phep-thu-va-tieu-chuan.md](references/phep-thu-va-tieu-chuan.md) |
| Phân loại lỗi, bảng AQL, dung sai gia công và vật liệu, IS 2771 | [references/dung-sai-aql-phan-loai-loi.md](references/dung-sai-aql-phan-loai-loi.md) |
| Kế hoạch kiểm tại Minh Phúc: nhập giấy, đầu ra sóng, in, bế – dán, xuất hàng; hồ sơ lô; NCR; khiếu nại | [references/ke-hoach-kiem-tra.md](references/ke-hoach-kiem-tra.md) |
| Số QC thấp thì chỉnh máy nào (ECT, BCT, bục, Cobb, bám keo) | [references/doc-so-qc-de-chinh-may.md](references/doc-so-qc-de-chinh-may.md) |
| Tính AQL, McKee, BCT yêu cầu, độ ẩm | skill `mp-tinh-toan` |
| Biểu mẫu: kiểm đầu đơn, kiểm xuất hàng, NCR, 8D | skill `mp-bieu-mau` |

## Nguyên tắc

- Một hộp nhiều lỗi chỉ tính **lỗi nặng nhất**; hộp hỏng do vận chuyển không tính. [FEFCO]
- Có tranh chấp với khách → **thử lại ở 23 °C / 50 % RH** sau khi ổn định mẫu (TP.HCM mùa mưa > 75 % RH, kho không điều hoà, kết quả lệch).
- Phiếu kết quả ghi **số hiệu chuẩn cụ thể** (ISO/TAPPI) — chưa có TCVN riêng cho ECT và cho thùng carton sóng thành phẩm.
- Kết quả ghi theo **số phiếu sản xuất** để nối với MP MES (máy, ca, tốc độ, dừng máy) → truy được tới máy và ca khi khách khiếu nại.
- KCS là người **sửa nhật ký máy in và thành phẩm** trên MES; KCS lấy mẫu thì **ghi rõ số mẫu** vào ghi chú (không để thành "Lỗi khác" — mã CH-06).
- Bốn ô ký trên phiếu nhận dạng pallet (Người kiểm tra · QC sản phẩm · QC giấy tấm · Kiểm tra) là chữ ký người thật — không ký thay.
