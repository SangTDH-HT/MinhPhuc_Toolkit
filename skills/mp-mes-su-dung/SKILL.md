---
name: mp-mes-su-dung
description: >
  Dùng phần mềm MP MES (bản 2.0, 10/2026) ở phía người dùng tại Minh Phúc — KHÔNG phải lập trình: đăng nhập PIN, đèn PLC/Máy chủ, chọn đơn,
  tờ phiếu Bắt đầu sản xuất, Chạy máy / Chạy đơn / Chạy dao, Tạm dừng có lý do (4 loại), ghi lỗi, mực, vật tư, Chạy trước, Lưu đơn, Chuyển ngày,
  Ngưng đơn, Lấy đơn ngày khác, Chuyển máy, In 2 mặt, đơn cán màng, ghép đơn tổ sóng, phiếu nhận dạng pallet, báo cáo ca, xác nhận số tấm,
  máy Giám sát (Toàn xưởng, Dữ liệu, Hiệu suất, Cảnh báo), 36 mã cảnh báo, vai Vận hành / KCS / Quản lý / Kỹ thuật, Trợ lý, xử lý sự cố khi mất
  kết nối. Dùng khi hướng dẫn thợ, tổ trưởng, KCS, quản lý thao tác trên MES hoặc giải thích một màn hình, một cảnh báo.
---

# mp-mes-su-dung — MP MES cho người đứng máy và người quản lý

Phạm vi: **cách dùng**. Không có trong repo: mã nguồn, cấu hình PLC, máy chủ, tài khoản, mật khẩu, địa chỉ mạng — những việc đó thuộc
người phụ trách phần mềm (vai Kỹ thuật). Luật tính giờ, đơn vị, OEE: skill `mp-ke-hoach-san-xuat`.

## Bảng tham chiếu

| Cần gì | Đọc |
|---|---|
| Thao tác ở máy in (In 1, In 2, Offset) — 7 bước, in 2 mặt, cán màng | [references/may-in.md](references/may-in.md) |
| Thao tác ở máy thành phẩm (dán 1/2, bế 1/2, bồi) — Ngưng đơn, phiếu nhận dạng | [references/may-thanh-pham.md](references/may-thanh-pham.md) |
| Thao tác ở tổ sóng — ba thẻ trạm, ghép đơn, dao tự chốt, xác nhận số tấm | [references/to-song.md](references/to-song.md) |
| Máy Giám sát, vai và quyền, Trợ lý, báo cáo | [references/giam-sat-va-quyen.md](references/giam-sat-va-quyen.md) |
| Đèn, cảnh báo (36 mã), mất kết nối — làm gì | [references/canh-bao-va-su-co.md](references/canh-bao-va-su-co.md) |

## Bảng chức năng tóm tắt (MES 2.0)

| Chức năng | Máy In 1, 2 | Offset | Dán 1, 2 | Bế 1, 2 | Bồi | Tổ sóng |
|---|---|---|---|---|---|---|
| Nút chạy | Chạy máy | Chạy máy | Chạy đơn | Chạy đơn | Chạy đơn | Chạy dao + Chạy từng trạm |
| Nút Start ngoài máy | có | — | — | — | — | ở dao |
| Thời gian chuẩn bị tính là | pha mực | pha mực | chuẩn bị* | chuẩn bị* | chuẩn bị* | chuẩn bị |
| Ô lỗi | Sóng, Thử máy, In lệch, Nhảy dao, Khác | như máy in | Sóng, In, Bế, Định hình, Khác | như máy dán | như máy dán | 7 ô: đổ rách … lỗi khác |
| Lỗi gõ theo | tờ in (không nhân số con) | tờ in | thùng | con | tấm | khổ (lúc lưu × tấm/khổ) |
| Trạm mực / vật tư | 6 trạm mực | 5 trạm mực | keo dán, keo bôi, kẽm | như dán | như dán | mét lỗi ở trạm sóng |
| Lưu đơn | hộp xác nhận | hộp xác nhận | lưu ngay | lưu ngay | lưu ngay | ở dao |
| Tự lưu khi đủ số | hộp đếm 90 s | hộp đếm 90 s | — | — | — | dao tự chốt |
| Ngưng đơn | — | — | ✓ | ✓ | ✓ | — |
| Chuyển ngày | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Chuyển máy | In 1 ↔ In 2 | — | Dán 1 ↔ Dán 2 | Bế 1 ↔ Bế 2 | — | — |
| Phiếu nhận dạng | — | — | chừa tờ cuối | — | — | in đủ lô |
| Sửa nhật ký | KCS trở lên | KCS | KCS | KCS | KCS | Vận hành |

\* Chuẩn bị ở máy thành phẩm hiện riêng trên Trang chủ, khi lưu cộng vào ngừng không kế hoạch.

## Ba lời dặn quan trọng nhất cho thợ

1. **Không tắt phần mềm** khi đèn PLC hay Máy chủ đỏ — số vẫn giữ; ghi tay số trên máy trong lúc chờ; quá 10 phút báo Kỹ thuật.
2. **Dừng máy thì bấm Tạm dừng và chọn đúng lý do**; bảo trì và ngừng có kế hoạch **phải gõ lý do** (bỏ trống = ngừng không kế hoạch).
3. **Đã lưu là đơn xong** — chạy tiếp ngày mai thì dùng **Chuyển ngày** (hoặc **Ngưng đơn** ở máy thành phẩm), đừng Lưu đơn.
