# "Lỗi khác" gồm những gì — mổ xẻ theo 7 nguồn

Nguồn: file mổ xẻ "Lỗi khác" của xưởng (10/2026) [MP].

> "Lỗi khác" hiện là **phần dư để cho khớp số**, không phải một loại lỗi. Chỉ nhóm **1, 2, 3, 7** là hàng hư thật; nhóm **4, 5, 6 không mất gì**.

## 1. Bảy nguồn

| Nhóm | Nguồn | Ví dụ thực tế | Hư thật? | Cách tách / xử lý | Ai lo |
|---|---|---|---|---|---|
| 1 | Lỗi thật chưa có tên ô | Cong vênh, nhoè mực, bế không đứt, bung mép dán… | Có | Thợ ghi theo mã lỗi; lỗi nhiều nhất thành ô riêng trên MES | Thợ máy, KCS |
| 2 | Lỗi đã có ô nhưng nhập thiếu / không nhập | Tấm sóng hư bị loại trước khi in mà không ghi ô "Sóng"; tờ in lệch không đếm vào "In lệch" | Có (ghi sai chỗ) | So "Lỗi khác" với các ô đã có; nhắc thợ nhập đúng ô | Thợ máy, KCS |
| 3 | Hao hụt kỹ thuật không ghi | Tờ thử máy, canh màu, tấm đầu đơn, đoạn chuyển đơn / ghép đơn | Có (có chủ đích) | Ghi vào "Thử máy" / hao hụt kỹ thuật, không tính là lỗi | Thợ máy |
| 4 | Hàng chưa chạy, còn tồn trước máy | Sóng giao hôm nay, mai mới in; đơn chạy dở, Chuyển ngày, Ngưng đơn | Không | Tính chênh theo **PHIẾU** khi đơn đã xong, không theo ngày; MES có cột "Tồn trước máy" ở màn Đối chiếu công đoạn | Phần mềm |
| 5 | Chênh do cách đếm | Sóng đếm theo dao × tấm/khổ, máy in đếm nhịp; máy bế đếm đôi; cảm biến sót; số con; làm tròn | Không | Soát bộ đếm và số con của đơn; máy bế bật cảm biến nhíp chống đếm đôi | Kỹ thuật |
| 6 | Hàng chuyển đi chỗ khác | KCS lấy mẫu; mượn tấm sang đơn khác; chạy bù; trả lại tổ sóng; lẫn đơn | Không | Ghi rõ số lượng và chuyển đi đâu (ghi chú bản ghi) | KCS, Quản lý |
| 7 | Thất lạc / hư khi vận chuyển | Hư khi vận chuyển, ngã pallet, ướt kho, mất | Có (cần truy) | Là phần còn lại sau khi trừ nhóm 1–6; lớn bất thường thì truy theo phiếu | Quản lý |

## 2. Công thức đang dùng

- **ERP** (máy in, cột NgoaiQuan): `Lỗi khác = Số tấm sóng chuyển qua (sóng OK) − Tổng số lượng in (bên In nhận)`.
- **MES** (máy in, cột "SP lệch"): `Sóng vào − Số tờ in − Tổng các ô lỗi` — số sóng vào đọc lại từ nhật ký tổ sóng mỗi lần xem.
- Khác nhau: MES **có trừ** các lỗi thợ đã nhập, ERP thì không → cùng một tấm hư có thể bị **đếm hai lần** ở ERP (ở ô lỗi và ở "Lỗi khác").
- "Lỗi khác" có thể **ÂM** (in nhiều hơn sóng giao): dùng tấm tồn từ trước hoặc sóng đếm thiếu — thuộc nhóm 4 hoặc 5, không phải lỗi.

## 3. Làm sao giảm "Lỗi khác" (lộ trình của xưởng)

1. **Đếm thật 1–2 tuần** bằng phiếu đếm (`templates/phieu-dem-loi-khac.md`): mỗi lần có hàng rơi vào "Lỗi khác" ghi mã + số lượng.
2. **Tổng hợp** theo máy × nhóm và theo mã (Pareto) → "hư thật" = nhóm 1 + 2 + 3 + 7.
3. **Chọn ô mới**: các mã nhiều nhất của nhóm 1 thành ô riêng trên MES (hoặc dùng 6 ô theo nguyên nhân — `sau-nhom-nguyen-nhan.md`).
4. **Sửa cách ghi**: nhóm 2 → nhắc nhập đúng ô; nhóm 3 → ô Thử máy / hao hụt; nhóm 6 → ghi chú chuyển đi.
5. **Sửa cách đếm**: nhóm 5 → cảm biến nhíp máy bế, quy cùng đơn vị (tấm/nhịp/con/thùng) trước khi so.
6. **Tính theo phiếu khi đơn xong** thay vì theo ngày (nhóm 4).
7. Phần còn lại lớn bất thường → **truy theo phiếu** (nhóm 7).

## 4. Đối chiếu công đoạn — đọc số cho đúng

| Đọc | Lưu ý |
|---|---|
| So tấm sóng giao với tấm máy in nhận | Cùng **đơn vị tấm** (sóng = dao × tấm/khổ; in = nhịp × số con) |
| So máy in với thành phẩm | Thành phẩm có thể ra **con** (bế) hoặc **thùng** (dán) — quy đổi theo số con |
| Đơn chưa xong | Đừng kết luận chênh; còn tồn trước máy |
| Đơn ngưng, chuyển ngày, chạy 2 lần | Cộng mọi bản ghi của phiếu |
