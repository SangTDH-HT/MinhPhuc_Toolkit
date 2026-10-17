---
name: mp-bao-tri
description: >
  Bảo trì máy ở Minh Phúc (phần cơ khí – vận hành, không phải lập trình): bảo trì phòng ngừa theo từng máy (dây chuyền sóng, máy in flexo,
  máy in offset, máy bồi, cán màng, máy bế phẳng/bế tròn, máy dán, máy xén, bếp keo, hệ hơi), bảo trì tự quản của thợ (vệ sinh – bôi trơn – kiểm tra –
  siết chặt), bôi trơn, ổ bi, xích, dây đai, khí nén, bẫy hơi, chi tiết hao mòn (dao, trục sóng, anilox, dao gạt, cao su, đệm bế, khuôn),
  quy trình xử lý máy hỏng, ghi lý do bảo trì trên MES, MTBF/MTTR, sổ lý lịch máy, khảo sát tem nhãn để tìm sách hãng, phụ tùng dự phòng.
  Dùng khi lập kế hoạch bảo trì, xử lý máy hỏng, tìm nguyên nhân dừng máy lặp lại, chuẩn bị phụ tùng.
---

# mp-bao-tri — máy chạy ổn là nền của mọi chỉ số

Trong sơ đồ tổ chức Minh Phúc, **Bảo trì** là một bộ phận của khối Sản xuất (cùng Dợn sóng, In, Thành phẩm). [MP-HSNL]
Mã lỗi xưởng chỉ rõ nhiều lỗi chất lượng có gốc **máy móc – khuôn bản** (trục sóng mòn, dao cùn, anilox, dao gạt, cao su, khuôn) — bảo trì tốt là
giảm lỗi, không chỉ giảm dừng máy.

## Bảng tham chiếu

| Cần gì | Đọc |
|---|---|
| Danh mục bảo trì phòng ngừa từng máy (ngày / tuần / tháng / quý) | [references/bao-tri-phong-ngua-theo-may.md](references/bao-tri-phong-ngua-theo-may.md) |
| Bôi trơn, ổ bi, xích, đai, khí nén, hơi; chi tiết hao mòn; dấu hiệu sắp hỏng; bảo trì tự quản | [references/boi-tron-va-hao-mon.md](references/boi-tron-va-hao-mon.md) |
| Máy hỏng: trình tự xử lý, ghi MES, MTBF/MTTR, phụ tùng | [references/xu-ly-may-hong.md](references/xu-ly-may-hong.md) |
| Sổ lý lịch máy, khảo sát tem nhãn, tìm sách hãng, hồ sơ cần có | [references/so-may-va-tai-lieu-may.md](references/so-may-va-tai-lieu-may.md) |
| An toàn khi bảo trì (LOTO, hơi, dao) | skill `mp-an-toan-lao-dong` |

## Năm nguyên tắc

1. **Khoá năng lượng (LOTO)** trước mọi việc trong vùng nguy hiểm — điện, khí nén, hơi, thuỷ lực, trọng lực (bàn ép, dao).
2. **Ghi lý do bảo trì trên MES** khi dừng sửa máy — không ghi lý do thì phút đó tính ngừng không kế hoạch; bấm chạy lại là hết bảo trì.
3. Dừng vặt lặp lại (cảnh báo **SX-22**) là tín hiệu bảo trì — tìm gốc, đừng chỉ sửa tạm.
4. Mỗi lần sửa ghi **sổ lý lịch máy**: hiện tượng, nguyên nhân, đã làm gì, phụ tùng, thời gian dừng.
5. Sách hãng và tem nhãn là nguồn đúng nhất — số trong repo là **[KN ngành]**, sách máy thật thắng.

## Hiện trạng tài liệu (10/2026)

Chưa có tem nhãn, sách hướng dẫn, sơ đồ của hầu hết máy (chỉ biết Mitsubishi offset, YB-1300E, 115SC). Việc đầu tiên của bảo trì: khảo sát tem nhãn
toàn bộ máy theo `templates/khao-sat-tem-nhan-may.md` và lập sổ lý lịch máy (`templates/so-ly-lich-may.md`).
