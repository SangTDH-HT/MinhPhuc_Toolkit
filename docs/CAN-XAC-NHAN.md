# Cần xác nhận tại xưởng

Danh sách những điều repo đang ghi theo một nguồn chưa chắc, hoặc hai nguồn nói khác nhau. Khi xác nhận xong: sửa skill liên quan, đổi nhãn nguồn
thành **[MP]**, ghi ngày và người xác nhận ở cột cuối, rồi chuyển dòng xuống mục "Đã xác nhận".

## 1. Máy móc

| # | Nội dung | Nguồn A | Nguồn B | Ảnh hưởng tới | Xác nhận |
|---|---|---|---|---|---|
| M1 | Máy in flexo mấy màu | HSNL: 5 màu | MES: 6 trạm mực (Máy In 1, 2) | `mp-in-flexo`, `data/may-moc.yaml` | |
| M2 | Số máy dán xưởng flexo | HSNL: 1 máy (150 m/phút) | MES: Máy dán tự động 1 và 2 | `mp-be-dan` | |
| M3 | Máy flexo process 250 sp/phút, máy bế tròn có đang chạy? | HSNL có | Web, MES không có | `mp-cong-ty` | |
| M4 | Công suất 3.500 / 5.500 nhịp/giờ ứng với máy bế 1 hay 2 | HSNL ghi "máy 1, máy 2" | Repo ghép theo số thứ tự | `data/may-moc.yaml` | |
| M5 | Trạm sóng A/C/E: đổi sóng bằng cách nào (cassette?), sóng E chạy ở trạm nào | MES: thẻ "Sóng A/C/E" | — | `mp-to-song` | |
| M6 | "Mền" ở trạm ghép là gì (băng ép / tấm đè trên bàn nhiệt?) | Cách gọi của xưởng; có nâng – hạ mền | — | `mp-to-song` | |
| M7 | Có máy đóng ghim (đóng kim) không | Cờ "Đóng kim" trên kế hoạch ERP | HSNL không nêu | `mp-be-dan` | |
| M8 | Hãng, model, năm của mọi máy (trừ Mitsubishi, YB-1300E, 115SC) | — | — | toàn repo | |
| M9 | Chi nhánh Dĩ An (79 DT743) còn hoạt động, làm gì | HSNL có | Web, chứng nhận không | `mp-cong-ty` | |

## 2. Thông số và chuẩn nội bộ (chưa có trong repo)

| # | Cần lấy | Ai biết | Skill sẽ cập nhật |
|---|---|---|---|
| T1 | Bảng chuẩn keo tinh bột (công thức, độ nhớt, điểm gel, nhiệt) | Tổ sóng, nhà cung cấp tinh bột | `mp-to-song` |
| T2 | Bảng góc bao gia nhiệt / áp hơi theo giấy và tốc độ | Thợ chính tổ sóng | `mp-to-song` |
| T3 | Biên xén tối thiểu, danh sách khổ cuộn đang dùng | Kế hoạch, tổ sóng | `mp-to-song`, `mp-tinh-toan` |
| T4 | Hệ số co sóng, độ dày tấm thực đo của từng sóng trên máy Minh Phúc | Tổ sóng, KCS | `data/song.csv`, `mptinh` |
| T5 | Bảng bù kích thước theo sóng của phòng thiết kế; phần mềm thiết kế đang dùng | Thiết kế | `mp-san-pham-ket-cau` |
| T6 | Khe lô kéo máy in theo độ dày tấm | Thợ chính tổ in | `mp-in-flexo` |
| T7 | Danh sách anilox (dòng, BCM, tình trạng); nhà cung cấp mực, bản, băng dán | Tổ in | `mp-in-flexo`, `data/nha-cung-cap.csv` |
| T8 | Dao cắt khuôn 23,8 hay 23,6 mm; quy ước khấc; độ cứng cao su; nhà làm khuôn | Tổ bế | `mp-be-dan` |
| T9 | Loại keo máy dán (PVA nguội hay keo nhiệt), nhà cung cấp | Tổ thành phẩm | `mp-be-dan` |
| T10 | Tốc độ mục tiêu đã duyệt theo máy và loại đơn (MES đang dùng số mặc định) | Quản đốc | `mp-ke-hoach-san-xuat` |
| T11 | COA giấy từng nhà cung cấp; tiêu chuẩn mua giấy | Mua hàng, KCS | `mp-giay-nguyen-lieu` |
| T12 | Giới hạn chấp nhận nội bộ (cong tấm %, độ dày, Cobb…) và bảng AQL công ty đang áp | KCS | `mp-kcs-chat-luong` |
| T13 | Lịch hiệu chuẩn thiết bị QC; hãng, model máy QC | KCS | `mp-kcs-chat-luong` |
| T14 | Quy trình CoC FSC nội bộ (người phụ trách, nhóm sản phẩm, hệ số quy đổi) | Phụ trách FSC | `mp-fsc-iso-attp` |
| T15 | Danh mục quy trình, biểu mẫu ISO hiện hành (mã biểu mẫu) | Thư ký ISO | `mp-bieu-mau` |
| T16 | Hồ sơ an toàn thực phẩm của giấy, mực, keo cho hộp gà rán, burger | KCS, mua hàng | `mp-fsc-iso-attp` |

## 3. Diễn giải cần đối chiếu nguyên văn

| # | Nội dung | Ghi chú |
|---|---|---|
| D1 | Cách hiểu "hệ thống chuyển giao" FSC (tuyên bố thấp nhất khi trộn loại FSC) | Đối chiếu mục 9 FSC-STD-40-004 V3-1 |
| D2 | Số hiệu văn bản pháp luật về an toàn lao động, PCCC | Tra văn bản hiện hành trước khi trích |
| D3 | EN 1010-5 còn hiệu lực? | Nguồn tra cứu ghi khác nhau |
| D4 | Thuật ngữ tiếng Trung trong `data/thuat-ngu.csv` | Nhờ người đọc tiếng Trung / thợ hãng |
| D5 | Hướng cong tấm về phía mặt khô hơn | KN ngành — kiểm trên máy thật |
| D6 | "6 lỗi hay gặp mỗi máy" | Xếp theo KN ngành — chờ số đếm phiếu đếm 1–2 tuần |

## Đã xác nhận

| # | Nội dung | Kết luận | Người, ngày |
|---|---|---|---|
| | | | |
