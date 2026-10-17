# In offset tờ rời: thông số, mã lỗi, bảng tra

Offset in gián tiếp: mực từ bản sang **cao su (blanket)** rồi sang giấy; hình sắc nét, màu chuẩn CMYK/Pantone; hợp số lượng trung bình tới lớn. [MP-Web]

## 1. Con số vận hành máy offset tờ rời [Sun Chemical]

| Thông số | Giá trị khuyến nghị | Ghi chú |
|---|---|---|
| Nhiệt độ lô chà mực (form rollers) | **22 – 26 °C** | Nóng: mực loãng, giảm độ dính → văng mực, bẩn nền. Lạnh: mực đặc, truyền kém |
| Máng mực | **≥ 21 °C** | Lạnh quá mực "lùi", không theo lô máng |
| Máng nước (fountain pan) | **~18 °C** | Nước nóng gây bẩn nền, tăng tầng |
| Dung dịch làm ẩm | Theo hãng: pH, độ dẫn điện, Brix, nhiệt độ | Nước nguồn không ổn định → cân nhắc lọc RO |
| pH giấy | **6,0 – 8,0** | Ngoài khoảng này mực khô chậm |
| Mực oxy hoá khô hẳn | **24 – 48 giờ** | Chồng tờ cao, phun bột sai → khô chậm, dính mặt sau |
| Cân bằng mực – nước | **Lượng mực và nước tối thiểu** | Nhiều nước → mực nhũ hoá, mất màu, loang |
| Tẩy cặn canxi trên lô | Nước nóng + giấm trắng 2:1 | Sau khi rửa bình thường |

Sách hướng dẫn máy Mitsubishi của xưởng (khi có) thắng các số này.

## 2. 18 mã lỗi máy in offset của Minh Phúc (OF-01 … OF-18)

Nguồn: file mổ xẻ "Lỗi khác" [MP]; ô MES: **Sóng · Thử máy · In lệch · Nhảy dao · Khác**. ★n = thứ hạng "6 lỗi hay gặp" (chưa có số đếm thật).

| Mã | Tên lỗi | Nhận biết | Nguyên nhân thường gặp | Khâu | Xử lý | Ô MES đang ghi | Phòng ngừa | Nhóm |
|---|---|---|---|---|---|---|---|---|
| | **Giấy vào** | | | | | | | |
| OF-01 | Giấy cong, nhăn, gấp góc ★6 | Tờ không phẳng | Độ ẩm giấy; bảo quản | Nguyên liệu | Loại bỏ | Khác | Ủ giấy trong xưởng trước khi in | 1 |
| OF-02 | Giấy co giãn | Lệch màu tăng dần theo chồng | Giấy hút ẩm | Nguyên liệu | Loại bỏ | Khác | Giữ ẩm xưởng ổn định | 1 |
| | **Vị trí in** | | | | | | | |
| OF-03 | Chồng màu lệch | Các màu không trùng nhau | Lệch bản; giấy co giãn | Tại máy | Loại bỏ | In lệch | Canh chồng màu tờ đầu | 2 |
| OF-04 | Lệch nhíp, lệch tay kê | Hình lệch so với mép giấy | Chỉnh nhíp, tay kê sai | Tại máy | Loại bỏ | In lệch | Kiểm nhíp, tay kê | 2 |
| | **Mực, nước** | | | | | | | |
| OF-05 | Dư nước: nhạt, lem | Màu nhạt, loang | Cân bằng mực – nước sai | Tại máy | Loại bỏ | Khác | Chỉnh nước theo tờ duyệt | 1 |
| OF-06 | Thiếu nước: bẩn nền ★4 | Nền trắng bị mực bám | Nước ít; bản bẩn | Tại máy | Loại bỏ | Khác | Kiểm hệ thống nước | 1 |
| OF-07 | Đậm nhạt không đều ★1 | Màu khác nhau giữa các tờ | Mực không đều | Tại máy | Chọn lại | Khác | Đo mật độ màu định kỳ | 1 |
| OF-08 | Sai màu so tờ duyệt | Màu khác tờ duyệt | Pha mực; mực khác lô | Tại máy | Loại bỏ | Khác | So màu tờ đầu với tờ duyệt | 1 |
| | **Ngoại quan** | | | | | | | |
| OF-09 | Dính mặt sau ★2 | Mực hằn sang tờ phía sau | Mực nhiều; chồng giấy sớm | Tại máy | Loại bỏ | Khác | Phun bột chống dính; chồng thấp | 1 |
| OF-10 | Đốm bụi (hickey) ★3 | Chấm trắng / đốm có vòng | Bụi giấy; mực khô | Tại máy | Chọn lại | Khác | Vệ sinh lô, bản | 1 |
| OF-11 | Sọc, vệt | Vệt ngang / dọc trên hình | Lô mực, lô nước mòn | Tại máy | Loại bỏ | Khác | Kiểm lô định kỳ | 1 |
| OF-12 | Bóng ma (in đúp) | Hình mờ lặp lại | Cao su lỏng; áp lực | Tại máy | Loại bỏ | Khác | Kiểm cao su, áp lực | 1 |
| OF-13 | Trầy, xước mặt in | Vết xước | Đường giấy ra; xếp chồng | Tại máy | Chọn lại | Khác | Kiểm đường ra giấy | 1 |
| | **Bản in** | | | | | | | |
| OF-14 | Bản mòn, trầy bản | Mất chi tiết, vệt trên hình | Bản cũ; bụi | Tại máy | Loại bỏ | Khác | Thay bản theo số lượt | 1 |
| OF-15 | Sai nội dung bản | Sai chữ, sai mã | Duyệt bản sai | Quản lý | Loại bỏ | Khác | So tờ đầu với mẫu duyệt | 1 |
| | **Phủ, cán màng (nếu có)** | | | | | | | |
| OF-16 | Bong màng, nhăn màng, bọt | Màng tách, nhăn, có bọt khí | Nhiệt, keo màng | Tại máy | Loại bỏ | Khác | Chỉnh nhiệt, áp cán | 1 |
| | **Nạp giấy** | | | | | | | |
| OF-17 | Kẹt giấy, nạp đôi ★5 | Hai tờ cùng vào; tờ kẹt rách | Giấy dính tĩnh điện; cài đặt | Tại máy | Loại bỏ | Khác | Giũ giấy; chỉnh đầu hút | 1 |
| | **Chuẩn bị** | | | | | | | |
| OF-18 | Tờ thử, canh màu | Tờ chạy thử đầu đơn | Canh bản, canh màu | Tại máy | Hao hụt kỹ thuật | Thử máy | Ghi đúng ô Thử máy | 3 |

Tổng 18 lỗi, 15 lỗi đang rơi vào "Khác". OF-18 (tờ thử, canh màu) → ô **Thử máy**.

## 3. Tra 21 lỗi in offset (rút gọn từ Sun Chemical)

Bản đủ: thư viện `07_Offset_Boi_Can_mang/SunChemical_Tra_loi_in_offset_to_roi.pdf`.

| Lỗi | Nguyên nhân thường gặp → cách xử lý | Mã MP |
|---|---|---|
| **Mực lùi, chảy kém** | Lô máng lạnh (< 21 °C); máng ít mực; mực đặc lại → đảo mực, khuấy, thêm chút vecni | OF-07 |
| **Chồng màu ngược / nhiễm màu** | Màu in trước quá đậm → giảm mật độ màu trước, tăng màu sau, hoặc đổi thứ tự; giấy không hút; cao su nhả mực kém | OF-08 |
| **Tăng tầng (dot gain)** | Đường cong bản; dung dịch ẩm cũ/sai; nước, lô chà quá nóng; lót cao su sai, áp lớn; lô, cao su mềm; mực độ dính thấp | OF-08 |
| **Bóng ma (ghosting)** | Lô chà sai cài đặt hoặc đường kính; bố trí hình không cân mực; mực quá trong; cao su bị hằn | OF-12 |
| **Đốm (hickey)** | Hạt lạ bám bản/cao su — gỡ bằng băng dính xem: màng mực khô → thay mực máng; xơ giấy → đổi lô giấy hoặc giảm độ dính mực | OF-10 |
| **Xơ giấy, bứt giấy** | Giấy kém; lót cao su sai; cao su quá dính; áp in sai; mực quá dính; mực – nước lệch | OF-10 |
| **Đóng cặn lô định lượng nước** | Tuần hoàn nước bẩn; pha dung dịch sai (máng ≤ 18 °C); bộ định lượng hỏng; lô cài sai; sai chất rửa | OF-06 |
| **Văng mực** | Hệ lô quá nóng; mực – nước lệch; mang quá nhiều mực; lô mòn; mực độ dính thấp | OF-05 |
| **Loang** | Giấy không đều; quá nhiều nước (cả từ đơn vị trước); lớp tráng giấy mềm; áp lớn; cao su cứng, bóng; mực quá đậm | OF-05 |
| **Chồng đống (piling)** | Lớp tráng giấy bong hay mực? kiểm trước; mực nhũ hoá; lô, máng lạnh; áp cao su sai; lô sai độ cứng; mực nghiền kém | OF-11 |
| **Bản mù, mòn bản** | Lô mực/lô nước cài sai; hạt lạ; chất tẩy bản chưa tráng sạch; cao su lót thừa/lỏng; dung dịch ẩm lệch; giấy nhả bột/xơ; cặn canxi; chế bản sai | OF-14 |
| **Chống trầy kém** | Mực chưa khô hẳn (24–48 giờ); mực nhũ hoá; giấy hút mạnh làm "phấn hoá" mực | OF-13 |
| **Truyền mực kém** | Lô bóng, chưa tẩy bóng; cặn canxi; lô cài sai, trương; lạm dụng phụ gia dung dịch ẩm; lô chưa đủ ấm | OF-07 |
| **Chồng mực kém (in 4 màu)** | Mực – nước lệch; mật độ màu sai; giấy hút kém | OF-08 |
| **Khô chậm** | pH giấy ngoài 6–8; giấy không hút; dung dịch ẩm quá axit hoặc nhiều chất thay cồn; chồng tờ cao; nhiều nước | OF-09 |
| **Nhoè kéo (slurring)** | Áp cao su – bản – giấy sai; cao su lỏng; tay kê lệch; giấy mép sóng | OF-04, OF-12 |
| **Sọc (không do bánh răng)** | Cao su lót thừa gây giật; lô chà ép bản quá nặng hoặc quá cứng | OF-11 |
| **Lô không nhận mực (stripping)** | Lô cứng; cặn canxi; hệ lô và nước lạnh; dung dịch ẩm quá "nhẹ" | OF-07 |
| **Đuôi mực (tailing)** | Màng mực dày; mực UV chưa khô đủ (kiểm đèn); mực nhũ hoá; áp in lớn | OF-05 |
| **Bẩn nền (tinting, scumming)** | Dung dịch ẩm bẩn/cũ; lô sai độ cứng hoặc cài chặt; áp bản – cao su lớn; lô > 26 °C, máng nước > 18 °C; cao su bóng; chất rửa nhiều dầu | OF-06 |
| **pH, độ dẫn dao động** | Nước nguồn thay đổi (lọc RO); bộ định lượng sai; tuần hoàn nhiễm bẩn | OF-05, OF-06 |

## 4. Kiểm soát màu giữa các lô [KN ngành]

- Lưu **tờ duyệt màu** có chữ ký cho từng mã hộp; so tờ đầu dưới cùng nguồn sáng.
- Đo mật độ màu (densitometer) các ô kiểm theo tần suất cố định; ghi vào hồ sơ mã hàng.
- Mực khác lô → thử trước khi chạy (OF-08). Chuẩn tham khảo nên mua: ISO 12647-2, G7/GRACoL.
