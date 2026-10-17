# Hệ mã lỗi của xưởng (127 mã)

Nguồn: file "Mổ xẻ Lỗi khác — MP MES" của xưởng (16–17/10/2026) [MP]. Dữ liệu máy đọc được: `data/ma-loi.csv`
(cột: ma, may, nhom_loi, ten, nhan_biet, nguyen_nhan, khau, xu_ly, o_mes, phong_ngua, nhom_loi_khac, top6).

## 1. Cấu trúc mã

| Tiền tố | Máy | Số mã | Ô lỗi MES đang có | Bảng chi tiết |
|---|---|---|---|---|
| TS | Tổ sóng (máy sóng + dao chặt) | 26 | Đổ rách · Bong dộp · Dập sóng · Sáng biên · Sai quy cách · Sai kết cấu · Lỗi khác | `mp-to-song` → `loi-tam-va-xu-ly.md` |
| FX | Máy In 1, Máy In 2 (flexo) | 24 | Sóng · Thử máy · In lệch · Nhảy dao · Khác | `mp-in-flexo` → `loi-in-va-xu-ly.md` |
| OF | Máy In Offset | 18 | Sóng · Thử máy · In lệch · Nhảy dao · Khác | `mp-xuong-offset` → `in-offset.md` |
| BO | Máy bồi | 14 | Sóng · In · Bế · Định hình · Khác | `mp-xuong-offset` → `boi-va-can-mang.md` |
| BE | Máy bế 1, Máy bế 2 | 18 | Sóng · In · Bế · Định hình · Khác | `mp-be-dan` → `be-va-khuon.md` |
| DA | Máy dán 1, Máy dán 2 | 17 | Sóng · In · Bế · Định hình · Khác | `mp-be-dan` → `dan-va-dong-kien.md` |
| CH | Chung mọi máy (gồm cả phần **không phải lỗi**) | 10 | thường rơi vào Khác / Lỗi khác | bảng dưới |

Mỗi mã có: tên · nhận biết (nhìn thấy gì) · nguyên nhân thường gặp · khâu gây ra (Nguyên liệu / Tại máy / Khâu trước / Quản lý / Vận chuyển – kho) ·
xử lý (Loại bỏ / Chọn lại / Ép phẳng / Hao hụt kỹ thuật / Không phải lỗi…) · ô MES đang ghi · phòng ngừa · nhóm "Lỗi khác" (1–7).

## 2. Sáu lỗi hay gặp nhất mỗi máy (đang rơi vào "Khác")

Xếp theo lỗi thường gặp của ngành, **chưa có số đếm thật**: soát lại, đếm thử 1–2 tuần bằng phiếu đếm rồi mới chốt tên ô mới với Giám đốc.

| # | Tổ sóng | Máy in flexo | Máy in offset | Máy bồi | Máy bế | Máy dán |
|---|---|---|---|---|---|---|
| 1 | TS-12 Cong lên/xuống | FX-05 In mờ, thiếu mực | OF-07 Đậm nhạt không đều | BO-03 Lệch bồi | BE-09 Tách rác không sạch | DA-04 Bung mép dán |
| 2 | TS-14 Phồng rộp | FX-04 In nhoè, lem | OF-09 Dính mặt sau | BO-04 Bong bồi | BE-10 Lỗ không rơi rác | DA-05 Keo tràn |
| 3 | TS-15 Nhăn mặt giấy | FX-10 Ăn bông, bít chữ | OF-10 Đốm bụi (hickey) | BO-05 Phồng rộp, bọt khí | BE-14 Kẹt tấm, gãy góc | DA-12 Dính thùng vào nhau |
| 4 | TS-11 Keo chưa chín / tấm ướt | FX-07 Sai màu so mẫu | OF-06 Thiếu nước: bẩn nền | BO-07 Keo tràn mép/mặt in | BE-16 Dập, hằn mặt in | DA-13 Móp góc, trầy |
| 5 | TS-04 Mối nối lọt vào tấm | FX-18 Rãnh lệch, sai kích thước | OF-17 Kẹt giấy, nạp đôi | BO-09 Cong vênh sau bồi | BE-11 Khuôn hỏng, dao gãy | DA-14 Kẹt phôi, nạp đôi |
| 6 | TS-21 Cắt xéo, không vuông | FX-21 Kẹt tấm, móp, gãy góc | OF-01 Giấy cong, nhăn, gấp góc | BO-06 Nhăn tờ in | BE-15 Nạp đôi tấm | DA-11 Gãy, nứt lằn khi gấp |

**Không phải lỗi — đừng ghi vào "Lỗi khác"**: tờ thử, tấm canh máy · tấm chuyển đơn, đầu cuộn · hàng còn tồn trước máy · chênh do cách đếm
(máy bế đếm đôi, tấm / nhịp / con) · KCS lấy mẫu · mượn tấm sang đơn khác.

## 3. Mã chung mọi máy (CH-01 … CH-10)

| Mã | Tên lỗi | Nhận biết | Nguyên nhân thường gặp | Khâu | Xử lý | Ô MES đang ghi | Phòng ngừa | Nhóm |
|---|---|---|---|---|---|---|---|---|
| | **Vận chuyển, kho** | | | | | | | |
| CH-01 | Móp, ngã pallet | Hàng móp, gãy khi chuyển | Xe nâng; xếp chồng cao | Vận chuyển - kho | Loại bỏ | Khác | Quấn màng; giới hạn chồng | 7 |
| CH-02 | Ướt mưa, ẩm kho | Hàng mềm, loang | Kho dột; để ngoài trời | Vận chuyển - kho | Loại bỏ | Khác | Che chắn; kê cao | 7 |
| CH-03 | Mất, thất lạc | Thiếu số lượng không rõ lý do | Không có phiếu giao nhận | Vận chuyển - kho | Truy theo phiếu | Khác | Ký giao nhận giữa các khâu | 7 |
| | **Ngoại quan** | | | | | | | |
| CH-04 | Bẩn dầu mỡ, dấu tay | Vết bẩn trên sản phẩm | Tay bẩn; máy rò dầu | Tại máy | Chọn lại | Khác | Găng tay; vệ sinh máy | 1 |
| | **Quản lý** | | | | | | | |
| CH-05 | Lẫn đơn, dán nhầm phiếu | Hàng nằm ở đơn khác | Phiếu nhận dạng sai; xếp chung | Quản lý | Chuyển về đúng đơn | Khác | In phiếu nhận dạng cho từng pallet | 6 |
| CH-06 | KCS lấy mẫu kiểm | Mẫu lấy ra không trả về | Kiểm chất lượng | Quản lý | Không phải lỗi | Khác | Ghi số mẫu vào ghi chú | 6 |
| CH-07 | Mượn tấm / phôi sang đơn khác | Đơn này thiếu, đơn kia dư | Bù cho đơn gấp | Quản lý | Không phải lỗi | Khác | Ghi rõ mượn sang đơn nào | 6 |
| CH-08 | Trả lại khâu trước | Tấm trả về tổ sóng / máy in | Không dùng hết; sai quy cách | Quản lý | Không phải lỗi | Khác | Ghi số trả về | 6 |
| | **Số liệu** | | | | | | | |
| CH-09 | Hàng chưa chạy, tồn trước máy | Khâu trước giao, máy này chưa chạy hết | Đơn chạy dở; Chuyển ngày; Ngưng đơn | Quản lý | Không phải lỗi | Khác | Tính chênh theo phiếu khi đơn xong | 4 |
| CH-10 | Chênh do đơn vị đếm | Số hai khâu lệch nhau dù không mất | Tấm / nhịp / con / thùng; làm tròn | Quản lý | Không phải lỗi | Khác | Quy về cùng đơn vị trước khi so | 5 |

## 4. Ghi lỗi trên MES — bốn luật

1. Lỗi đã có ô → **ghi đúng ô** (nhóm 2 "nhập thiếu ô" là lỗi ghi sai chỗ, ví dụ tấm sóng hư bị loại trước khi in mà không ghi ô Sóng).
2. Lỗi chưa có ô → ô Khác / Lỗi khác **kèm mã** (ví dụ "FX-04 ×35") trong ghi chú.
3. Hao hụt kỹ thuật (tờ thử, canh máy, chuyển đơn) → ô **Thử máy** (máy in) hoặc ghi riêng là hao hụt — không tính lỗi.
4. Không phải hàng hư (tồn trước máy, chênh đếm, KCS lấy mẫu, mượn tấm) → **không ghi lỗi**; ghi rõ số lượng và đi đâu trong ghi chú.

Tổ sóng nhập lỗi **theo dao** (lưu × số tấm/khổ); máy in nhập theo tấm (số đã nhân số con); thành phẩm theo sản phẩm của máy.

## 5. Phiếu đếm "Lỗi khác"

Mẫu phiếu: `templates/phieu-dem-loi-khac.md` — ghi Ngày · Máy · Số phiếu · Mã lỗi · Số lượng · Ghi chú; tổng hợp theo máy × nhóm và theo từng mã
(xếp hạng) để chọn tên ô lỗi mới. File gốc của xưởng (Excel, có danh sách xổ chọn mã) — **không mở bằng thư viện ghi lại** vì mất danh sách xổ.
