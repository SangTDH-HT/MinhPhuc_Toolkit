# Lỗi in flexo: nhận diện, nguyên nhân, xử lý

## 1. 24 mã lỗi máy in flexo của Minh Phúc (FX-01 … FX-24)

Nguồn: file mổ xẻ "Lỗi khác" của xưởng (10/2026) [MP]; dữ liệu đủ ở `data/ma-loi.csv`.
Ô lỗi MES máy in: **Sóng · Thử máy · In lệch · Nhảy dao · Khác**. Nhóm: 1 lỗi thật chưa có tên ô · 2 có ô nhưng nhập thiếu ·
3 hao hụt kỹ thuật · 5 chênh đếm. ★n = thứ hạng "6 lỗi hay gặp" (theo kinh nghiệm ngành, **chưa có số đếm thật**).

| Mã | Tên lỗi | Nhận biết | Nguyên nhân thường gặp | Khâu | Xử lý | Ô MES đang ghi | Phòng ngừa | Nhóm |
|---|---|---|---|---|---|---|---|---|
| | **Tấm vào (khâu trước)** | | | | | | | |
| FX-01 | Tấm sóng cong không nạp được | Kẹt ở bàn nạp | Tấm cong từ tổ sóng | Khâu trước | Ép phẳng hoặc loại | Sóng | Phản hồi tổ sóng; ủ tấm trước khi in | 2 |
| FX-02 | Tấm sóng bong lớp, dập | Phát hiện khi in | Lỗi tổ sóng | Khâu trước | Loại bỏ | Sóng | KCS kiểm tấm trước khi in | 2 |
| FX-03 | Tấm sai kích thước | Không vừa bản, lệch rãnh | Lỗi dao chặt | Khâu trước | Loại bỏ | Sóng | Đo tấm đầu đơn | 2 |
| | **Mực, màu** | | | | | | | |
| FX-04 | In nhòe, lem ★2 | Chữ / hình loang, mờ biên | Mực loãng; áp lực in cao | Tại máy | Loại bỏ | Khác | Kiểm độ nhớt mực; giảm áp lực | 1 |
| FX-05 | In mờ, thiếu mực ★1 | Màu nhạt, lấm tấm trắng | Thiếu mực; trục anilox bẩn | Tại máy | Loại bỏ | Khác | Vệ sinh anilox; châm mực đủ | 1 |
| FX-06 | Đậm nhạt không đều | Màu lúc đậm lúc nhạt trên tấm | Trục mực không đều; tấm cong | Tại máy | Chọn lại | Khác | Chỉnh khe trục mực | 1 |
| FX-07 | Sai màu so mẫu ★4 | Màu khác mẫu duyệt | Pha mực sai; độ nhớt | Tại máy | Loại bỏ | Khác | Duyệt màu tờ đầu; lưu công thức mực | 1 |
| FX-08 | Mực chưa khô, dính tấm khác | Vết mực ở mặt sau tấm kế | Sấy yếu; xếp chồng sớm | Tại máy | Chọn lại | Khác | Tăng sấy; chờ khô mới xếp | 1 |
| FX-09 | Chấm mực văng, vệt sọc | Chấm / vệt mực ngoài hình | Trục mực, dao gạt mòn | Tại máy | Chọn lại | Khác | Thay dao gạt; vệ sinh trục | 1 |
| | **Bản in** | | | | | | | |
| FX-10 | Ăn bông, bít chữ ★3 | Chữ nhỏ, mã vạch bị lấp | Bản bẩn; mực đặc | Tại máy | Loại bỏ | Khác | Lau bản giữa đơn | 1 |
| FX-11 | Mất nét, đứt nét | Chi tiết bị mất | Bản mòn; áp lực thấp | Tại máy | Loại bỏ | Khác | Thay bản mòn | 1 |
| FX-12 | Bản hỏng, bong bản | Vết rách / mất mảng hình | Bản cũ; dán bản không chắc | Tại máy | Loại bỏ | Khác | Kiểm bản trước khi lên máy | 1 |
| FX-13 | Sai nội dung bản | Sai chữ, sai mã, thiếu chi tiết | Duyệt bản sai; lấy nhầm bản | Quản lý | Loại bỏ | Khác | So tờ đầu với mẫu duyệt | 1 |
| | **Vị trí in** | | | | | | | |
| FX-14 | Lệch hình so với tấm | Hình lệch mép, lệch lằn | Canh bản sai; tấm trượt | Tại máy | Loại bỏ | In lệch | Canh tờ đầu | 2 |
| FX-15 | Chồng màu lệch | Các màu không trùng nhau | Lệch bản giữa các đơn vị màu | Tại máy | Loại bỏ | In lệch | Canh chồng màu tờ đầu | 2 |
| FX-16 | In ngược mặt / ngược chiều | Hình in sai mặt hoặc quay ngược | Đặt tấm sai | Tại máy | Loại bỏ | Khác | Đánh dấu chiều nạp | 1 |
| | **Cấn, xẻ rãnh** | | | | | | | |
| FX-17 | Nhảy dao | Rãnh xẻ sai nhịp | Dao xẻ trượt; tấm trượt | Tại máy | Loại bỏ | Nhảy dao | Kiểm dao xẻ, bàn nạp | 2 |
| FX-18 | Rãnh lệch, sai kích thước ★5 | Rãnh lệch so với lằn | Cài đặt dao xẻ | Tại máy | Loại bỏ | Khác | Đo rãnh tấm đầu | 1 |
| FX-19 | Lằn cấn lệch / bể | Lằn sai vị trí hoặc nứt | Bánh cấn lệch; tấm khô | Tại máy | Loại bỏ | Khác | Canh bánh cấn | 1 |
| FX-20 | Tai dán, góc cắt sai | Tai dán ngắn / dài, góc sai | Cài đặt dao góc | Tại máy | Loại bỏ | Khác | Soát tai dán tấm đầu | 1 |
| | **Nạp, ra tấm** | | | | | | | |
| FX-21 | Kẹt tấm, móp, gãy góc ★6 | Tấm móp, gãy khi qua máy | Tấm cong; chỉnh nạp sai | Tại máy | Loại bỏ | Khác | Chỉnh bàn nạp | 1 |
| FX-22 | Trầy xước mặt in | Vết xước trên hình in | Bàn ra tấm, xếp chồng | Tại máy | Chọn lại | Khác | Lót bàn ra; xếp nhẹ tay | 1 |
| | **Chuẩn bị** | | | | | | | |
| FX-23 | Tờ thử, canh màu | Tấm chạy thử đầu đơn | Canh bản, canh màu | Tại máy | Hao hụt kỹ thuật | Thử máy | Ghi đúng ô Thử máy | 3 |
| | **Đếm** | | | | | | | |
| FX-24 | Đếm dư / thiếu, dồn tấm | Số máy đếm khác số thật | Hai tấm qua một lần; cảm biến | Tại máy | Không phải lỗi | Khác | Soát cảm biến đếm | 5 |

Tổng 24 lỗi, 17 lỗi đang rơi vào "Khác". FX-23 (tờ thử, canh màu) là hao hụt kỹ thuật → ô **Thử máy**. FX-24 (đếm dư/thiếu) là chênh đếm.

## 2. Bảng tra lỗi in trên carton (rút gọn từ Sun Chemical)

Bản đủ tiếng Anh trong thư viện: `05_In_flexo/SunChemical_Tra_loi_muc_bao_bi_giay_carton.pdf` (16 lỗi) và `SunChemical_Tra_loi_in_flexo.pdf` (11 lỗi).

| Lỗi | Nguyên nhân thường gặp → cách xử lý | Mã MP gần nhất |
|---|---|---|
| **Màu đậm / bẩn** | Độ nhớt cao → giảm. Màng mực dày → giảm độ nhớt, gạt mực tốt hơn, giảm tốc hoặc anilox thể tích nhỏ hơn. Nhiễm màu cũ → rửa trạm, thay mực | FX-06 |
| **Bắc cầu điểm tram** | Anilox thể tích lớn; áp bản hoặc áp anilox – bản lớn; bụi giấy bám bản (dao cắt cùn, xưởng bụi); mực khô nhanh; bản mềm/mòn; pH thấp | FX-10 |
| **Bít chữ (fill-in)** | Áp bản lớn; bản không phẳng, mòn, lõm, bóng; bản quá mềm; màng mực dày; chữ quá nhỏ so với màng mực; bụi giấy | FX-10 |
| **Viền quầng (halo)** | Chỉ ở mép đầu: giảm áp anilox lên bản, kiểm dán bản. Bản không ôm trục → dán lại. Toàn hình: bản không phẳng/mòn, màng mực dày, bản quá cứng, máy không song song | FX-04 |
| **Tua mép (feathering)** | Áp bản lớn; bản quá cứng; áp anilox – bản lớn; mực khô nhanh (thêm glycol hoặc tăng tốc); pH thấp; bụi giấy | FX-04 |
| **Mắt cá (fisheye)** | Phá bọt quá liều hoặc không tương thích; mực có bọt li ti → thay/thêm mực mới không phá bọt | FX-05 |
| **Sủi bọt** | Hở gioăng bơm phía hút, áp bơm cao, khuấy mạnh, ống hồi không ngập mực, buồng dao gạt kín kém, quá nhiều nước, độ nhớt cao | FX-05 |
| **Lỗ kim (pinholes)** | Mặt giấy có lỗ → giảm độ nhớt cho mực thấm đều; sức căng bề mặt mực cao (mực nước) → thêm chất thấm ướt; áp bản thấp (dùng băng cứng cho mảng đặc); mực khô nhanh; trục ép bẩn; **phá bọt quá liều**; anilox mòn | FX-05 |
| **Màu không ổn định** | Trong một đơn: độ nhớt, pH, giấy, phụ gia, bọt thay đổi → đo, kiểm soát. Giữa các đơn: ghi lại và cố định mọi biến số. Giữa các trạm: khác anilox, áp, gạt mực → chỉnh công thức theo trạm | FX-06, FX-07 |
| **Quệt mực, dính vết** | Mực chưa khô (màng dày) → giảm độ nhớt, gạt tốt hơn, giảm tốc, anilox nhỏ hơn; giấy hút kém. Ở bế/gấp: cao su đệm mòn, áp dao lớn, băng gấp mòn/trượt, thanh dẫn chà lên hình in | FX-08 |
| **In loang lổ (mottle)** | Mặt hoặc độ dày tấm không đều → tăng áp bản hoặc bản mềm hơn; độ nhớt thấp; quá nhiều nước; anilox, lô gạt, bản bẩn/hỏng; mực nhiễm bẩn; bọt; pH thấp | FX-06 |
| **Mực phủ không kín** | Áp bản thiếu; màng mực mỏng so với giấy nhám, hút mạnh → tăng độ nhớt, anilox lớn hơn; bản quá cứng; mực khô nhanh; pH thấp | FX-05 |
| **Chồng mực kém (trapping)** | Lớp dưới chưa khô; lớp trên độ nhớt **thấp hơn** lớp dưới (phải cao hơn); lớp trên khô nhanh; giấy không hút; hai mực không tương thích; pH sai | FX-06 |
| **Sọc in** | Hệ gạt hai trục mang nhiều mực → tăng áp lô gạt hoặc chuyển sang dao gạt; anilox nghẹt, mòn, bẩn; bản cứng/bóng; độ nhớt thấp | FX-09 |
| **Màu không đều theo khổ** | Các trục không song song (đậm nhạt hai bên); lô gạt có rãnh; dao gạt mòn/cong; anilox hỏng/bẩn; thiếu lưu lượng mực; bản dán lỏng; trục nảy do bánh răng, ổ bi | FX-06 |
| **In gợn sóng (washboard)** | Độ dày tấm thay đổi theo bước sóng → dùng tấm không ván giặt (**sửa ở máy sóng**, TS-16); áp bản sai; màng mực quá dày/mỏng; độ nhớt thấp | FX-06 |
| **Màu nhạt** | Quá nhiều nước (nước rửa đọng trong trạm); anilox mòn/bẩn; độ nhớt thấp; màng mực mỏng; áp bản sai; bản cứng, bóng, bẩn; giấy kháng mực | FX-05 |
| **Bám mực kém (adhesion)** | Bề mặt không nhận mực; mực khô kém; mực không hợp vật liệu; độ nhớt cao | — |

Bốn "thủ phạm" chính khi in carton [Luminite]: **mực** (không tương thích, nhiễm bẩn → sọc, ván giặt, loang), **bản** (bẩn, hỏng, mềm, mòn, lỏng),
**pH**, **độ nhớt**. Cải thiện: bảo dưỡng máy (giảm rung lắc), áp "vừa chạm", kiểm bánh răng, giảm nhiễm bẩn.

## 3. In ép bẹp sóng — làm yếu thùng mà mắt thường khó thấy

**[KN ngành]** Khe giữa các cặp lô kéo tấm và giữa trục bản – trục ép quá chặt sẽ ép bẹp sóng, giảm độ dày và **giảm ECT/BCT** dù hình in vẫn đẹp.
Kiểm: đo độ dày tấm **trước và sau máy in** cùng vị trí; đo ECT một mẫu trước và sau in khi đơn yêu cầu BCT cao. Đặt khe lô kéo theo độ dày tấm thực đo.
NZQA liệt kê "in ép bẹp" (printing crush) trong danh mục lỗi in bắt buộc [NZQA 40327].

## 4. Danh mục lỗi in chuẩn nghề [Chuẩn: NZQA 40327, 40335]

Thợ in phải nhận ra và nêu ít nhất hai nguyên nhân, một cách sửa cho từng lỗi: nhoè/quệt mực, sai màu đều, viền quầng, lệch chồng màu hoặc in xiên,
mất hình, hình mờ nét, in ép bẹp sóng, mực phủ không đều, méo hình, bít chữ, chồng mực kém, in bẩn, màu dao động.
