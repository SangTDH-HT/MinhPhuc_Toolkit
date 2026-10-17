# Máy dán hộp và đóng kiện

## 1. Máy dán hộp (folder-gluer, 糊箱机) — máy dán tự động 1, 2

**Bộ phận** [Chuẩn: NZQA 40322]:
- Cụm keo: bánh keo, vòi keo, trống keo, bồn keo nóng/nguội, đế keo, bơm, đầu phun keo nóng chảy, ống keo, điều khiển định thời, điều khiển áp lực.
- Cụm gấp: băng gấp, thanh gấp, băng tải mang tờ, thanh cần, lô là phẳng, "lưỡi kiếm", lô ép băng tải.

**Trình tự lên máy (make-ready)** [Heidelberg]:
bộ cấp tờ (vách bên, cửa cấp, giá đỡ chồng tờ, rung, hút) → canh lề (thanh canh, băng tải dưới, lô trên) → **gấp mồi lằn 1 và lằn 3** (pre-break)
→ (khoá đáy nếu có) → hệ keo (bồn keo, súng phun, đường keo) → **gấp cuối** (lô dẫn, áp băng tải, lô lằn, tốc độ băng gấp) → cụm chuyển →
**ép và ra hàng** (áp lực ép, thời gian ép).

**Danh mục lỗi chuẩn nghề** [NZQA 40322]: lỗi gấp — khe dán thay đổi, **đuôi cá**, lỗi lằn, gãy, nứt tách, gấp sai thứ tự; lỗi keo — không keo /
đứt quãng, quá nhiều, sai thời điểm, lệch vị trí ngang, bám kém. Phân biệt **dán trong** và **dán ngoài**.

| Lỗi | Nguyên nhân thường gặp [KN ngành] | Hướng xử lý |
|---|---|---|
| Khe dán lệch, thay đổi | Lằn gấp lệch từ máy in/bế; tốc độ băng gấp hai bên khác; thanh gấp sai vị trí | Kiểm lằn công đoạn trước; cân tốc độ băng; chỉnh thanh |
| Đuôi cá | Lằn không song song/không vuông; băng gấp hai bên lệch tốc; gấp mồi chưa đủ | Kiểm lằn, cân băng, tăng gấp mồi |
| Không keo / đứt quãng | Vòi nghẹt, cảm biến tờ hỏng, độ nhớt cao, hết keo | Vệ sinh vòi, kiểm cảm biến, chỉnh keo |
| Keo tràn, dính nắp | Keo nhiều, sai thời điểm, lệch vị trí | Giảm lượng, chỉnh định thời, dời đường keo |
| Bám kém | Vùng dán có lớp phủ/vecni/mực; bụi; thời gian ép ngắn; keo lạnh, độ nhớt thấp | Chừa vùng dán không in, vệ sinh, tăng thời gian ép, kiểm keo |

**Keo nguội và độ nhớt** [Intercol]:
- Dán tốt bắt đầu từ tấm tốt và keo tốt; keo phải ra **lượng không đổi**. Độ nhớt cao → định lượng không chuẩn; thấp → keo chảy, bám kém.
- Độ nhớt chịu nhiệt độ môi trường: keo thiết kế ~20 °C, ống keo dưới mái tôn mùa nóng có thể lên 40 °C; thợ hay bù bằng chỉnh áp, hành trình kim →
  quá trình mất ổn định.
- Nên dùng **áp lực keo tuyến tính theo tốc độ máy** (khởi động chậm cần ít áp, đủ tốc cần áp cao hơn).
- Keo dính sai chỗ làm thùng không mở được, dính chùm, **đứng máy dựng thùng tự động của khách** → khiếu nại. Có loại keo pha chất phát quang
  an toàn thực phẩm để camera kiểm keo nhìn thấy.
- Loại keo máy dán Minh Phúc đang dùng (nguội PVA hay nóng chảy) **chưa xác nhận**.

**Chuẩn chấp nhận** [FEFCO QC]: khe dán **6–8 mm**, sóng đơn ±4 mm, sóng đôi −4/+6 mm; lệch mép (đuôi cá) ≤ 0,5 % chiều cao phôi, tối thiểu 3 mm;
mối dán đạt khi xé ra **≥ 80 %** diện tích keo còn xơ giấy.

## 2. 17 mã lỗi máy dán của Minh Phúc (DA-01 … DA-17)

Nguồn: file mổ xẻ "Lỗi khác" [MP]; ô MES: **Sóng · In · Bế · Định hình · Khác**. ★n = thứ hạng "6 lỗi hay gặp" (chưa có số đếm thật).

| Mã | Tên lỗi | Nhận biết | Nguyên nhân thường gặp | Khâu | Xử lý | Ô MES đang ghi | Phòng ngừa | Nhóm |
|---|---|---|---|---|---|---|---|---|
| | **Vào (khâu trước)** | | | | | | | |
| DA-01 | Phôi lỗi từ bế | Lằn bể, rác chưa tách | Lỗi máy bế | Khâu trước | Loại bỏ | Bế | Chọn phôi trước khi dán | 2 |
| DA-02 | Lỗi in | Lệch màu, sai màu | Lỗi máy in | Khâu trước | Loại bỏ | In | Chọn phôi trước khi dán | 2 |
| DA-03 | Lỗi sóng | Phôi cong, bong lớp | Lỗi tổ sóng | Khâu trước | Loại bỏ | Sóng | KCS kiểm phôi | 2 |
| | **Dán** | | | | | | | |
| DA-04 | Bung mép dán ★1 | Mép dán hở, không dính | Thiếu keo; keo khô nhanh | Tại máy | Dán lại hoặc loại | Khác | Kiểm súng keo, nhiệt keo | 1 |
| DA-05 | Keo tràn ★2 | Keo dính ra ngoài mép | Lượng keo nhiều | Tại máy | Chọn lại | Khác | Giảm keo; chỉnh vị trí súng | 1 |
| DA-06 | Keo chưa khô, bung khi xếp | Thùng bung sau khi bó | Ép chưa đủ thời gian | Tại máy | Dán lại | Khác | Tăng thời gian ép | 1 |
| | **Gấp, định hình** | | | | | | | |
| DA-07 | Dán so le (đuôi cá) | Hai mép không thẳng hàng | Canh dẫn hướng; lằn sai | Tại máy | Loại bỏ | Định hình | Canh dẫn hướng tấm đầu | 2 |
| DA-08 | Khe mép dán sai | Khe quá to hoặc quá nhỏ | Gấp lệch; kích thước phôi | Tại máy | Loại bỏ | Định hình | Đo khe tấm đầu | 2 |
| DA-09 | Thùng xéo, không vuông | Thùng dựng lên bị lệch | Gấp không theo lằn | Tại máy | Loại bỏ | Định hình | Kiểm lằn phôi; chỉnh dây gấp | 2 |
| DA-10 | Gấp ngược lằn | Gấp sai chiều lằn | Đặt phôi sai chiều | Tại máy | Loại bỏ | Định hình | Đánh dấu chiều nạp | 2 |
| DA-11 | Gãy, nứt lằn khi gấp ★6 | Mặt giấy nứt ở lằn | Giấy khô; lằn sâu | Tại máy | Loại bỏ | Khác | Phản hồi khâu bế / sóng | 1 |
| | **Ngoại quan** | | | | | | | |
| DA-12 | Dính thùng vào nhau ★3 | Thùng dính khi ép bó | Keo tràn; chưa khô | Tại máy | Gỡ hoặc loại | Khác | Giảm keo; chờ khô | 1 |
| DA-13 | Móp góc, trầy ★4 | Góc thùng móp, mặt trầy | Băng tải, bàn ép | Tại máy | Chọn lại | Khác | Kiểm băng tải, thanh dẫn | 1 |
| | **Nạp phôi** | | | | | | | |
| DA-14 | Kẹt phôi, nạp đôi ★5 | Phôi kẹt hoặc hai phôi cùng vào | Phôi cong, dính nhau | Tại máy | Loại bỏ | Khác | Giũ phôi; chỉnh bàn nạp | 1 |
| | **Đếm, bó** | | | | | | | |
| DA-15 | Đếm sai số trong bó | Bó thừa / thiếu thùng | Đếm tay; cảm biến | Tại máy | Không phải lỗi | Khác | Soát bộ đếm bó | 5 |
| DA-16 | Cột dây sai, bó lỏng | Bó bung khi vận chuyển | Máy cột dây; thao tác | Tại máy | Bó lại | Khác | Kiểm lực cột | 1 |
| | **Chuẩn bị** | | | | | | | |
| DA-17 | Phôi canh máy | Phôi chạy thử đầu đơn | Canh dẫn hướng, keo | Tại máy | Hao hụt kỹ thuật | Khác | Ghi riêng là hao hụt | 3 |

Tổng 17 lỗi, 10 lỗi đang rơi vào "Khác". DA-17 (phôi canh máy) là hao hụt kỹ thuật; DA-15 (đếm sai số trong bó) là chênh đếm.

## 3. Đếm và đơn ở máy dán [MP-MES]

- Một lần đếm = **một thùng** đã dán (số con luôn 1). Kế hoạch máy dán ghi bằng **cái**.
- Chuyển đơn được giữa **máy dán 1 ↔ máy dán 2** (cùng công đoạn Dán); không chuyển sang máy bế.
- **Ngưng đơn**: dừng giữa chừng để chạy đơn khác — chạy tiếp trong ngày thì vẫn **một bản ghi** (ghi chú "Chạy 2 lần: …"), mai mới chạy thì kế hoạch
  giữ nguyên số; quên chốt thì sáng hôm sau phần mềm hỏi lưu bù (skill `mp-mes-su-dung`).

## 4. Phiếu nhận dạng lô hàng — SX-QT01-BM02/06 (chỉ máy dán) [MP-MES]

- Khổ A5 dọc, **mỗi pallet một tờ**, dán lên pallet thùng đi nhập kho.
- Người dùng nhập **số thùng một pallet** (một số chung cả xưởng, sửa ngay trên hộp thoại khi mặt hàng xếp khác); phần mềm chia lô:
  `3.410 ÷ 300 = 11 pallet đầy + 1 pallet lẻ 110 thùng = 12 tờ`.
- In trước **N−1 tờ**, **luôn chừa tờ cuối** (kể cả khi chia chẵn) — chạy hụt chỉ ăn vào pallet cuối; bấm Lưu đơn biết sản lượng thật mới in tờ cuối.
- Ô "Số pallet" ghi **thứ tự / tổng** (3/12) — thợ kho nhìn tờ cuối biết đủ hay thiếu.
- Đầu tờ chừa ~15 mm cho **nẹp giấy** (nẹp ngậm mép trên).
- Bốn ô **cố tình để trống**: Người kiểm tra · QC sản phẩm · QC giấy tấm · Kiểm tra — chữ ký và kết luận của **người thật** nhìn tận mắt lô hàng.
- Có thêm dòng **Quy cách** để phân biệt hai lô cùng khách cùng ngày.
- Tổ sóng cũng có phiếu nhận dạng riêng, tích ô công đoạn theo kế hoạch.

## 5. Xếp, đóng kiện, đai

- Xếp sản phẩm ra pallet và đóng kiện, đai đúng yêu cầu là hai kỹ năng riêng [NZQA 40333, 40326].
- Thùng giao **gấp phẳng, buộc kiện trên pallet** (mẫu MP-045). [MP-Web]
- **Kiểm lực cột dây** (DA-16 bó lỏng, bung khi vận chuyển); soát bộ đếm bó (DA-15). [MP]
- **[KN ngành]** Dùng nẹp góc khi đai; đai quá căng làm bẹp mép thùng phía ngoài kiện; quấn màng pallet; nhãn kiện có mã đơn, số lượng, số lô.
- Pallet, container, bảo quản thành phẩm: skill `mp-kho-giao-hang`.

## 6. Đóng kim (đóng ghim)

Kế hoạch ERP có cờ công đoạn **Đóng kim**. Chuẩn mối ghim [IS 2771]: ghim cách nhau **≤ 60 mm**, ghim đầu/cuối cách mép **≤ 25 mm**, chồng mép
**≥ 30 mm**. Máy đóng ghim của Minh Phúc chưa có trong danh sách máy — cần xác nhận.
