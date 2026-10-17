# PHIẾU ĐẾM "LỖI KHÁC" (ghi trong 1–2 tuần)

Mục đích: biết "Lỗi khác" thật ra gồm những gì để chọn tên ô lỗi mới / nhóm nguyên nhân. Mã lỗi tra `data/ma-loi.csv` hoặc skill tổ máy
(TS- tổ sóng, FX- flexo, OF- offset, BO- bồi, BE- bế, DA- dán, CH- chung).

| Ngày | Máy | Số phiếu SX | Mã lỗi | Tên lỗi | Nhóm (1–7) | Số lượng | Ghi chú (đi đâu, vì sao) |
|---|---|---|---|---|---|---|---|
| 16/10/2026 | Máy In 2 | 359/10 | FX-04 | In nhoè, lem | 1 | 35 | Mực loãng sau giờ nghỉ trưa (dòng ví dụ) |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

Nhóm: **1** lỗi thật chưa có tên ô · **2** có ô nhưng nhập thiếu · **3** hao hụt kỹ thuật · **4** tồn trước máy · **5** chênh đếm · **6** chuyển đi (KCS lấy mẫu,
mượn tấm…) · **7** thất lạc / hư vận chuyển. "Hư thật" = 1 + 2 + 3 + 7.

Tổng hợp cuối kỳ: lưu thành CSV có cột `ma,so_luong` rồi chạy `python -m mptinh pareto --file phieu-dem.csv` (trong `tools/tinh-toan`).
File Excel gốc của xưởng có danh sách xổ chọn mã — **đừng mở bằng công cụ ghi lại tự động** (mất danh sách xổ).
