---
name: mp-bieu-mau
description: >
  Biểu mẫu dùng ngay ở Minh Phúc (thư mục templates/, Markdown in được): phiếu kiểm đầu đơn cho tổ sóng – máy in – bế – dán – bồi, phiếu kiểm giấy cuộn nhập,
  phiếu kiểm xuất hàng AQL, NCR, báo cáo 8D, phiếu đếm "Lỗi khác", phiếu ghi tay khi mất kết nối MES, phiếu giao ca, khảo sát tem nhãn máy,
  sổ lý lịch máy, phiếu LOTO, đánh giá rủi ro máy, sổ quản lý anilox, hồ sơ quy cách mã hàng, phiếu yêu cầu khách hàng, ma trận kỹ năng, A3 cải tiến,
  SOP mẫu. Dùng khi cần một biểu mẫu để in, điền, hoặc làm khung cho quy trình ISO; khi soạn biểu mẫu mới theo cùng phong cách.
---

# mp-bieu-mau — biểu mẫu in được, điền được

Biểu mẫu trong repo là **bản đề xuất** dựng theo sổ tay và mã lỗi của xưởng; mã biểu mẫu chính thức đặt theo hệ thống ISO 9001 của công ty
(ví dụ biểu mẫu đang dùng: **SX-QT01-BM02/06** phiếu nhận dạng lô hàng — in từ MP MES).

## Danh mục

| Việc | Biểu mẫu | Skill liên quan |
|---|---|---|
| Kiểm tờ/tấm/thùng đầu đơn (sóng, in, bế, dán, bồi) | [kiem-tra-dau-don.md](../../templates/kiem-tra-dau-don.md) | `mp-kcs-chat-luong` |
| Kiểm giấy cuộn nhập kho | [phieu-kiem-tra-giay-cuon.md](../../templates/phieu-kiem-tra-giay-cuon.md) | `mp-giay-nguyen-lieu` |
| Kiểm xuất hàng theo lô (AQL, BCT…) | [phieu-kiem-tra-xuat-hang.md](../../templates/phieu-kiem-tra-xuat-hang.md) | `mp-kcs-chat-luong` |
| Sản phẩm không phù hợp | [phieu-ncr.md](../../templates/phieu-ncr.md) | `mp-kcs-chat-luong`, `mp-xu-ly-su-co` |
| Khiếu nại, lỗi lặp — 8D | [bao-cao-8d.md](../../templates/bao-cao-8d.md) | `mp-xu-ly-su-co` |
| Đếm "Lỗi khác" 1–2 tuần | [phieu-dem-loi-khac.md](../../templates/phieu-dem-loi-khac.md) | `mp-xu-ly-su-co` |
| Ghi tay khi MES mất kết nối | [phieu-ghi-tay-khi-mat-ket-noi.md](../../templates/phieu-ghi-tay-khi-mat-ket-noi.md) | `mp-mes-su-dung` |
| Giao ca tại máy | [phieu-giao-ca.md](../../templates/phieu-giao-ca.md) | mọi tổ |
| Khảo sát tem nhãn máy | [khao-sat-tem-nhan-may.md](../../templates/khao-sat-tem-nhan-may.md) | `mp-bao-tri` |
| Sổ lý lịch máy (bôi trơn, PM, phụ tùng, hỏng – sửa) | [so-ly-lich-may.md](../../templates/so-ly-lich-may.md) | `mp-bao-tri` |
| Khoá năng lượng – treo thẻ | [phieu-loto.md](../../templates/phieu-loto.md) | `mp-an-toan-lao-dong` |
| Đánh giá rủi ro máy | [danh-gia-rui-ro-may.md](../../templates/danh-gia-rui-ro-may.md) | `mp-an-toan-lao-dong` |
| Sổ anilox | [so-quan-ly-anilox.md](../../templates/so-quan-ly-anilox.md) | `mp-in-flexo` |
| Hồ sơ quy cách mã hàng | [ho-so-quy-cach-ma-hang.md](../../templates/ho-so-quy-cach-ma-hang.md) | `mp-ho-tro-kinh-doanh`, `mp-kcs-chat-luong` |
| Yêu cầu của khách (báo giá, mẫu) | [phieu-yeu-cau-khach-hang.md](../../templates/phieu-yeu-cau-khach-hang.md) | `mp-ho-tro-kinh-doanh` |
| Ma trận kỹ năng | [ma-tran-ky-nang.md](../../templates/ma-tran-ky-nang.md) | `mp-dao-tao` |
| A3 cải tiến | [a3-cai-tien.md](../../templates/a3-cai-tien.md) | `mp-cai-tien` |
| SOP mẫu | [sop-mau.md](../../templates/sop-mau.md) | `mp-cai-tien` |

## Cách dùng

- **In ra giấy**: mở file `.md` trong trình xem Markdown rồi in, hoặc xuất PDF bằng `python scripts/xuat_pdf.py templates/<file>.md`.
- **Điền cho một máy/đơn cụ thể**: nhờ Claude "điền phiếu kiểm đầu đơn cho máy In 2, mã hàng …" — Claude chép mẫu, điền phần biết được, để trống phần phải đo.
- **Soạn biểu mẫu mới**: giữ khung đầu (mã biểu mẫu, ngày, máy, số phiếu SX), dùng mã lỗi của xưởng, có ô ký người thật; đặt tên file chữ thường, gạch nối,
  không dấu; thêm một dòng vào bảng trên.
- Không đưa vào git: biểu mẫu đã điền có tên khách, số liệu thật của khách (lưu ở hệ thống tài liệu của công ty).
