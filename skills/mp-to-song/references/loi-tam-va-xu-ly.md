# Lỗi tấm: nhận diện, nguyên nhân, xử lý

## 1. 26 mã lỗi tổ sóng của Minh Phúc (TS-01 … TS-26)

Nguồn: file mổ xẻ "Lỗi khác" của xưởng (10/2026) [MP]; dữ liệu đủ ở `data/ma-loi.csv`.
Ô lỗi trên MES tổ sóng: **Đổ rách · Bong dộp · Dập sóng · Sáng biên · Sai quy cách · Sai kết cấu · Lỗi khác**.
Cột "Nhóm" = nhóm của "Lỗi khác" (1 lỗi thật chưa có tên ô · 2 có ô nhưng nhập thiếu · 3 hao hụt kỹ thuật · 7 thất lạc/vận chuyển —
xem skill `mp-xu-ly-su-co`). ★n = thứ hạng trong "6 lỗi hay gặp nhất" (xếp theo kinh nghiệm ngành, **chưa có số đếm thật**).

| Mã | Tên lỗi | Nhận biết | Nguyên nhân thường gặp | Khâu | Xử lý | Ô MES đang ghi | Phòng ngừa | Nhóm |
|---|---|---|---|---|---|---|---|---|
| | **Giấy cuộn** | | | | | | | |
| TS-01 | Giấy cuộn ướt, ẩm | Tấm mềm, loang ẩm, dễ bong lớp | Cuộn để nơi ẩm, mưa dột, kê sát nền | Nguyên liệu | Loại bỏ | Lỗi khác | Kê pallet, che bạt; đo ẩm trước khi lên máy | 1 |
| TS-02 | Rách mép, móp cuộn | Mép giấy rách, gãy trong tấm | Kẹp cuộn mạnh, va đập khi vận chuyển | Nguyên liệu | Cắt bỏ phần hư | Đổ rách | Kẹp đúng lực; xếp cuộn đứng | 2 |
| TS-03 | Sai loại giấy / định lượng | Tấm mỏng, yếu; màu giấy khác | Lấy nhầm cuộn | Nguyên liệu | Loại bỏ | Sai kết cấu | Dán nhãn cuộn rõ; soát kết cấu trước khi chạy | 2 |
| TS-04 | Mối nối giấy lọt vào tấm ★5 | Vết băng keo nối; tấm dày cục bộ | Không cắt bỏ đoạn nối khi nối cuộn | Tại máy | Loại bỏ | Lỗi khác | Đánh dấu và cắt bỏ tấm có mối nối | 1 |
| TS-05 | Lẫn giấy khác màu | Một phần tấm khác màu | Nối nhầm cuộn khác màu | Tại máy | Loại bỏ | Lỗi khác | Soát màu cuộn trước khi nối | 1 |
| | **Sóng** | | | | | | | |
| TS-06 | Sóng nghiêng / ngã | Đỉnh sóng ngã một phía; tấm yếu | Trục sóng mòn; lực căng giấy | Tại máy | Loại bỏ | Lỗi khác | Kiểm trục sóng định kỳ | 1 |
| TS-07 | Sóng cao thấp, không đều | Độ dày tấm không đều | Trục mòn; hơi / áp ép không đều | Tại máy | Loại bỏ | Lỗi khác | Kiểm áp hơi, trục ép | 1 |
| TS-08 | Sóng bể, xẹp | Sóng bị đè bẹp | Lực ép lớn; trục ép | Tại máy | Loại bỏ | Dập sóng | Chỉnh áp ép theo loại sóng | 2 |
| | **Keo** | | | | | | | |
| TS-09 | Thiếu keo, bong lớp | Lớp mặt tách khỏi sóng | Keo ít, keo loãng; nhiệt thấp | Tại máy | Loại bỏ | Bong dộp | Kiểm độ nhớt keo mỗi ca | 2 |
| TS-10 | Dư keo, keo tràn | Đốm keo, vệt keo; mặt cứng | Lượng keo cao | Tại máy | Chọn lại | Lỗi khác | Chỉnh khe trục keo | 1 |
| TS-11 | Keo chưa chín / tấm ướt ★4 | Tấm mềm, ẩm; bong khi xếp | Nhiệt bàn sấy thấp; chạy nhanh | Tại máy | Để khô hoặc loại | Lỗi khác | Giữ nhiệt bàn sấy; giảm tốc khi giấy dày | 1 |
| | **Hình dạng tấm** | | | | | | | |
| TS-12 | Cong lên / cong xuống ★1 | Tấm không nằm phẳng | Chênh ẩm giữa mặt và đáy; nhiệt | Tại máy | Ép phẳng hoặc loại | Lỗi khác | Cân nhiệt / ẩm hai lớp mặt | 1 |
| TS-13 | Cong chữ S, xoắn | Tấm vặn hai đầu | Lực căng giấy không đều | Tại máy | Loại bỏ | Lỗi khác | Chỉnh phanh cuộn | 1 |
| TS-14 | Phồng rộp ★2 | Bọt khí giữa các lớp, ấn vào lún | Thiếu keo cục bộ; hơi nước | Tại máy | Loại bỏ | Lỗi khác | Kiểm trục keo, nhiệt | 1 |
| TS-15 | Nhăn mặt giấy ★3 | Nếp nhăn trên mặt tấm | Lực căng giấy; trục dẫn lệch | Tại máy | Loại bỏ | Lỗi khác | Chỉnh trục dẫn, lực căng | 1 |
| TS-16 | Sọc vằn mặt (lộ sóng) | Mặt gợn theo đỉnh sóng | Giấy mặt mỏng; ép quá tay | Tại máy | Chọn lại | Lỗi khác | Giảm áp ép với giấy mỏng | 1 |
| | **Cán lằn, xả biên** | | | | | | | |
| TS-17 | Lằn cấn lệch | Lằn sai vị trí | Cài đặt bánh cán | Tại máy | Loại bỏ | Sai quy cách | Soát vị trí lằn ở tấm đầu đơn | 2 |
| TS-18 | Lằn nứt / quá sâu | Gấp bị nứt mặt giấy | Lằn sâu; giấy khô giòn | Tại máy | Loại bỏ | Lỗi khác | Chỉnh độ sâu lằn theo giấy | 1 |
| TS-19 | Biên thiếu giấy (sáng biên) | Mép tấm lộ sóng, hụt lớp | Giấy chạy lệch; khổ giấy hẹp | Tại máy | Loại bỏ | Sáng biên | Canh giấy giữa; chọn khổ đủ | 2 |
| | **Dao chặt** | | | | | | | |
| TS-20 | Sai chiều dài / khổ | Kích thước ngoài dung sai | Cài đặt dao; trượt giấy | Tại máy | Loại bỏ | Sai quy cách | Đo tấm đầu đơn | 2 |
| TS-21 | Cắt xéo, không vuông ★6 | Tấm hình bình hành | Lệch dao; giấy chạy lệch | Tại máy | Loại bỏ | Lỗi khác | Kiểm vuông góc mỗi đơn | 1 |
| TS-22 | Mép xơ, bavia | Mép cắt tưa | Dao cùn | Tại máy | Chọn lại | Lỗi khác | Mài / thay dao theo lịch | 1 |
| TS-23 | Tấm rách khi chặt | Tấm bị xé ở đường cắt | Dao cùn; giấy ướt | Tại máy | Loại bỏ | Đổ rách | Thay dao; kiểm ẩm | 2 |
| | **Ngoại quan** | | | | | | | |
| TS-24 | Dính dầu mỡ, bẩn | Vết dầu, vết đen | Trục, xích rò dầu | Tại máy | Chọn lại | Lỗi khác | Vệ sinh máy đầu ca | 1 |
| | **Chuyển đơn** | | | | | | | |
| TS-25 | Tấm chuyển đơn, đầu cuộn | Tấm giữa hai đơn; đoạn đầu cuộn | Đổi đơn khi chạy liên tục | Tại máy | Hao hụt kỹ thuật | Lỗi khác | Ghi riêng là hao hụt, không tính lỗi | 3 |
| | **Xếp chồng** | | | | | | | |
| TS-26 | Móp, gãy khi xếp | Góc móp, tấm gãy | Xếp chồng cao; ngã chồng | Vận chuyển - kho | Loại bỏ | Lỗi khác | Giới hạn chiều cao chồng | 7 |

Tổng 26 lỗi, 18 lỗi đang rơi vào "Lỗi khác". TS-25 (tấm chuyển đơn, đầu cuộn) là **hao hụt kỹ thuật**, ghi riêng, không tính lỗi.

## 2. Cong tấm (warp, 翘曲) — tra sâu

| Kiểu cong | Mô tả | Nguyên nhân chính | Hướng xử lý |
|---|---|---|---|
| Cong ngang (CD) — lên / xuống | Cong theo chiều ngang máy | Độ ẩm hai mặt giấy lệch nhau — **[KN ngành]** tấm cong về phía mặt khô hơn (mặt đó co nhiều hơn) | Cân nhiệt hai lớp giấy mặt: tăng góc bao gia nhiệt cho mặt ướt hơn, giảm cho mặt khô hơn; xem lượng keo; đổi cuộn lệch ẩm **[KN ngành]** |
| Cong dọc (MD) | Cong theo chiều chạy máy | **[KN ngành]** Lực căng hai lớp giấy mặt chênh | Cân lực căng: phanh giá cuộn, lực căng cầu dẫn, băng tải máy dán đôi |
| Cong chéo, cong xoắn ("cánh quạt") | Trục cong chạy chéo tấm | Hỏng thiết bị (giá cuộn, tay bao nhiệt, trục, băng tải trên); ẩm lệch theo khổ (ẩm, keo, nhiệt không đều); cuộn giấy (hướng xơ, mép chùng, định lượng/độ dày sai); lực căng lệch (mép chùng, giá cuộn lệch, tay bao không thăng bằng, trục không song song, băng tải lệch, áp trục ép không đều) | Kiểm lần lượt bốn nhóm nguyên nhân [Chuẩn: NZQA 40328] |
| Cong chữ S (TS-13) | Cong ngược chiều nhau trên một tấm | **[KN ngành]** Ẩm hoặc nhiệt lệch theo khổ; bẫy hơi một đầu trục hỏng; lực căng không đều | Đo nhiệt hai đầu trục, kiểm bẫy hơi, kiểm cuộn, chỉnh phanh cuộn |

Đo cong: đặt tấm lên mặt phẳng, chiều cong úp lên; độ cao lớn nhất ÷ khoảng cách hai mép tựa × 100 %, đo tại đầu ra máy sóng.
[Chuẩn: FEFCO; NZQA 40351] Tấm cong làm kẹt ở máy in, máy bế (FX-01, FX-21, BE-14) — ép phẳng hoặc ủ tấm trước khi chạy tiếp.

## 3. Các lỗi khác — tra sâu

| Lỗi | Nguyên nhân | Hướng xử lý | Nguồn |
|---|---|---|---|
| **Gãy sóng** — thấy ngay sau trục ép | Giấy sóng khô (ẩm < 6 %); căng quá đường giấy sóng (phanh giá cuộn mạnh, kẹp lõi chặt, lô gia ẩm chạy chậm hơn giấy hoặc không quay); giấy sóng kém | Tăng ẩm giấy sóng (phun hơi), giảm phanh, cho lô gia ẩm chạy nhanh hơn giấy 1–5 % | AOPack |
| **Tấm mỏng / độ dày thấp** | Độ dày giấy và biên dạng trục sóng; căng giấy sóng; áp trục sóng/trục ép không đều hoặc thiếu; thiếu nhiệt nên sóng ướt dễ bẹp; ngón giữ chỉnh sai, thanh ngón cong, ngón sai bán kính sau mài trục; bơm chân không nghẹt; keo quá nhiều làm sóng ướt | Kiểm từng nguyên nhân; độ song song trục, tỷ lệ tốc độ, nhiệt độ và độ nhớt keo | AOPack |
| **Phồng rộp / tách lớp** (TS-09, TS-14) | Truyền nhiệt kém, không đủ nhiệt để keo dán; vệt liên tục hoặc từng chỗ; tách lớp cả mảng hoặc ở mép | Kiểm nhiệt, hơi, bẫy hơi, tốc độ; kiểm keo (khe keo, độ nhớt, điểm gel) | AOPack |
| **Mối keo "khoá kéo"** (zipper) | Nhiệt quá cao trên giấy mặt hoặc giấy sóng, keo không thấm vào bề mặt | Giảm nhiệt / góc bao, chỉnh tốc độ | AOPack |
| **Ván giặt** (washboard, 搓衣板) (TS-16) | Keo nhiều hoặc loãng; giấy mặt mỏng; áp bàn nhiệt lớn; nhiệt cao + keo nhiều | Giảm khe keo, tăng hàm lượng rắn keo, giấy mặt nặng hơn, giảm áp đè | KN ngành |
| **Sóng nghiêng / bẹp** (TS-06, TS-08) | Áp đè máy dán đôi lớn, tốc độ băng tải lệch, căng cầu dẫn, trục kéo bóp tấm, trục sóng mòn | Giảm áp, kiểm tốc độ băng tải, kiểm trục sóng | KN ngành |
| **Vệt khô keo** | Lô keo bẩn, khe keo không đều, đập chắn keo hở, keo đặc cục bộ | Vệ sinh lô keo, chỉnh khe keo, lọc keo | KN ngành |
| **Nhăn giấy** (TS-15) | Lực căng không đều, mép cuộn chùng, trục dẫn không song song, ẩm không đều | Chỉnh phanh, căn giá cuộn, đổi cuộn | KN ngành |
| **Tấm "xanh"** — keo chưa hồ hoá đủ (TS-11) | Tốc độ cao so với nhiệt, điểm gel keo cao, thiếu hơi | Giảm tốc, tăng nhiệt, chỉnh keo | NZQA 40328; KN ngành |
| **Mép xơ, lằn nứt, cắt xéo** (TS-18, TS-21, TS-22) | Dao cùn, sai tốc độ dao so với tấm; lằn quá sâu (nứt) hoặc quá nông (gấp sai chỗ); tấm không vuông | Mài/thay dao, chỉnh độ sâu lằn theo giấy, kiểm vuông góc | KN ngành |
| **Sáng biên** (TS-19) | Giấy chạy lệch; khổ giấy hẹp | Canh giấy giữa; chọn khổ đủ | MP |

## 4. Danh mục lỗi tấm chuẩn nghề [Chuẩn: NZQA 40328, 40342]

Cong lên, cong xuống, cong chéo, cong chữ S; phồng rộp; nhăn; gợn sóng giấy; mối nối; vạch khe; xơ mép; tách lớp hoặc bám keo kém
(cục bộ / diện rộng); sóng bị cắt, gãy, bẹp; sóng thấp; sóng nghiêng; sóng cao thấp không đều; vết lõm; vết cọ xát; vệt khô keo;
ván giặt; nứt lằn; tấm không cắt khổ, cắt khổ xấu; lệch; không gấp gọn theo lằn; giấy mặt lắp ngược; tấm ướt; tấm "xanh".
Thợ máy một mặt phải xử lý được: lệch, ván giặt, tấm ướt, tách lớp, gập mép, sóng nghiêng/biến dạng, nhăn, lõm, tấm bẹp hỏng.

## 5. Lỗi tổ sóng hiện ra ở công đoạn sau

| Thấy ở | Mã | Gốc ở tổ sóng |
|---|---|---|
| Máy in | FX-01, FX-02, FX-03 | Tấm cong, bong lớp, sai kích thước |
| Máy in | "in gợn sóng" | Ván giặt (TS-16) |
| Máy bồi, máy bế, máy dán | BO-01, BE-01, DA-03 | Tấm cong, bong, sai khổ |

Khâu sau ghi đúng ô **Sóng** trên MES, KCS phản hồi tổ sóng; đừng để rơi vào "Lỗi khác".
