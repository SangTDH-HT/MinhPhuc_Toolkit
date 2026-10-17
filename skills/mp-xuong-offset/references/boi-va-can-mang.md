# Bồi sóng và cán màng

## 1. Bồi sóng (flute lamination, litho-lamination)

- Tờ in offset được bồi lên tấm sóng (thường sóng E) vì mặt tấm sóng gợn không in offset trực tiếp đẹp được. [MP-Web]
- Chuẩn năng lực Úc cho máy bồi/cán: thiết lập cấp tờ, dẫn tờ; chỉnh **hệ bôi keo, áp lực ép, hệ sấy**; chạy mẫu, kiểm, chỉnh;
  trong sản xuất theo dõi **khớp vị trí tờ in – tấm**, áp lực và độ bám, **theo dõi keo suốt ca**. [Chuẩn: ICPCBF3810, ICPCBF3820]
- Giấy tráng phủ cường độ cao giúp **giảm ván giặt** khi bồi. [Korsnäs]
- Máy bồi Minh Phúc: **YB-1300E**, ≥ 56.000 sản phẩm/8 giờ [MP-HSNL]; trên MES đếm 1 lần cảm biến = 1 tấm.

### Lỗi bồi — nguyên nhân và hướng xử lý [KN ngành]

| Lỗi | Nguyên nhân thường gặp | Hướng xử lý |
|---|---|---|
| Cong tấm sau bồi | Ẩm tờ in và tấm sóng chênh; keo nhiều nước | Cân ẩm hai vật liệu, giảm lượng keo, **ép chồng khi chờ khô** |
| Phồng, bong mảng | Thiếu keo hoặc keo không đều; áp ép thấp; mặt sau tờ in có vecni/mực dày | Tăng keo đều, tăng áp, kiểm mặt sau tờ in |
| Ván giặt (hằn sóng lên mặt in) | Keo nhiều, giấy mặt mỏng, áp ép lớn | Giảm keo, giấy dày/cứng hơn, giảm áp |
| Lệch tờ in – tấm | Canh lề sai, tờ cong | Chỉnh canh lề, xử lý tờ cong trước khi bồi |
| Keo thấm lên mặt in | Keo loãng, giấy mỏng hút mạnh | Tăng độ nhớt keo, giảm lượng |

## 2. 14 mã lỗi máy bồi của Minh Phúc (BO-01 … BO-14)

Nguồn: file mổ xẻ "Lỗi khác" [MP]; ô MES máy bồi: **Sóng · In · Bế · Định hình · Khác**. ★n = thứ hạng "6 lỗi hay gặp" (chưa có số đếm thật).

| Mã | Tên lỗi | Nhận biết | Nguyên nhân thường gặp | Khâu | Xử lý | Ô MES đang ghi | Phòng ngừa | Nhóm |
|---|---|---|---|---|---|---|---|---|
| | **Vào (khâu trước)** | | | | | | | |
| BO-01 | Tấm sóng lỗi | Tấm cong, bong, sai khổ | Lỗi tổ sóng | Khâu trước | Loại bỏ | Sóng | KCS kiểm tấm trước khi bồi | 2 |
| BO-02 | Tờ in lỗi | Lệch màu, bẩn, sai màu | Lỗi máy in | Khâu trước | Loại bỏ | In | Chọn tờ trước khi bồi | 2 |
| | **Bồi** | | | | | | | |
| BO-03 | Lệch bồi ★1 | Tờ in lệch so với tấm sóng | Canh mép; tốc độ | Tại máy | Loại bỏ | Khác | Canh mép tờ đầu | 1 |
| BO-04 | Bong bồi, không dính ★2 | Tờ in tách khỏi tấm | Thiếu keo; keo kém | Tại máy | Loại bỏ | Khác | Kiểm lượng keo, độ nhớt | 1 |
| BO-05 | Phồng rộp, bọt khí ★3 | Bọt khí dưới tờ in | Keo không đều; ép yếu | Tại máy | Loại bỏ | Khác | Chỉnh trục ép | 1 |
| BO-06 | Nhăn tờ in ★6 | Nếp nhăn trên mặt in | Tờ in cong; lực kéo | Tại máy | Loại bỏ | Khác | Ủ tờ in; chỉnh dẫn hướng | 1 |
| | **Keo** | | | | | | | |
| BO-07 | Keo tràn mép / mặt in ★4 | Vết keo trên mặt in, mép | Lượng keo nhiều | Tại máy | Chọn lại | Khác | Giảm keo; vệ sinh trục | 1 |
| BO-08 | Thiếu keo mép, hở mép | Mép tờ in vểnh lên | Trục keo không đều | Tại máy | Loại bỏ | Khác | Kiểm trục keo hai mép | 1 |
| | **Sau bồi** | | | | | | | |
| BO-09 | Cong vênh sau bồi ★5 | Tấm cong khi khô | Keo ẩm; chênh ẩm hai mặt | Tại máy | Ép phẳng hoặc loại | Khác | Ép chồng khi còn ẩm | 1 |
| BO-10 | Dập sóng do ép | Sóng xẹp, tấm yếu | Ép quá tay | Tại máy | Loại bỏ | Khác | Chỉnh áp ép theo loại sóng | 1 |
| BO-11 | Dính tấm khi xếp chồng | Tấm dính nhau | Keo chưa khô | Tại máy | Loại bỏ | Khác | Chờ khô; xếp so le | 1 |
| | **Thao tác** | | | | | | | |
| BO-12 | Bồi ngược mặt / ngược chiều | Hình in quay sai hướng | Đặt tờ sai | Tại máy | Loại bỏ | Khác | Đánh dấu chiều tờ | 1 |
| | **Ngoại quan** | | | | | | | |
| BO-13 | Trầy, bẩn mặt in | Vết xước, dấu tay | Xếp, vận chuyển trong máy | Tại máy | Chọn lại | Khác | Găng tay; lót bàn | 1 |
| | **Chuẩn bị** | | | | | | | |
| BO-14 | Tấm canh máy | Tấm chạy thử đầu đơn | Canh mép, canh keo | Tại máy | Hao hụt kỹ thuật | Khác | Ghi riêng là hao hụt | 3 |

Tổng 14 lỗi, 12 lỗi đang rơi vào "Khác". BO-14 (tấm canh máy) là hao hụt kỹ thuật, ghi riêng.

## 3. Cán màng nhiệt (OPP/PE)

- Lỗi cán ghép (tài liệu đào tạo Comexi): cong, phồng ống (tunnelling), mờ sương, vỏ cam, vân đá, bọt khí, cuộn lệch, nhăn cuộn, mực lem,
  **bám yếu**, keo còn dính.
- Lực căng màng sai → cong, cúp, bọt khí; chạy cùng loại màng hai mặt thì đặt lực căng hai bên như nhau; quá nhiệt làm màng gợn sóng;
  chạy chậm = truyền nhiệt nhiều hơn → cân **nhiệt – tốc độ**; cặn keo bám trục gây điểm nóng không đều. [hướng dẫn máy cán]
- **[KN ngành]** Bám yếu trên tờ in offset thường do **mực chưa khô** hoặc còn nhiều **bột chống dính** — chờ mực khô đủ (24–48 giờ) trước khi cán.
- Mã MP: **OF-16** "Bong màng, nhăn màng, bọt" (nhiệt, keo màng → chỉnh nhiệt, áp cán).

## 4. Đơn có cán màng ở xưởng flexo

Đơn cán màng của máy in flexo đi vòng: in → cán màng → quay lại máy in cắt rãnh (skill `mp-in-flexo`, mục đơn cán màng hai lượt).
