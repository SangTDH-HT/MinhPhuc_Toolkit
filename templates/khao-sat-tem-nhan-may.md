# PHIẾU KHẢO SÁT TEM NHÃN MÁY

Mục đích: biết đúng hãng, model, năm của từng máy để tìm sách hướng dẫn, sơ đồ, danh mục phụ tùng, mã lỗi chính hãng.
Mỗi máy (và mỗi cụm lớn của dây chuyền sóng) một phiếu. Ảnh đặt tên: `<mã máy>_<cụm>_<loại ảnh>.jpg` (vd `DS1_trac-song-B_tem.jpg`).

| Mục | Ghi |
|---|---|
| Tên máy trong xưởng | |
| Mã máy trên MES (DS1, MI1, MI2, MI3, DT1, DT2, BF1, BF2, BOI, …) | |
| Cụm (với dây chuyền sóng: giá cuộn, máy một mặt A/C/E, máy một mặt B, cầu dẫn, gia nhiệt, máy tráng keo, máy dán đôi, dao cắt dọc, dao cắt ngang, xếp tấm, bếp keo, lò hơi) | |
| Vị trí trong xưởng | |

## 1. Tem nhãn chính — chụp rõ, đủ sáng

| Hãng | Model | Số máy (serial) | Năm SX | Nước SX | Khổ máy / khổ tối đa | Tốc độ tối đa | Điện áp / công suất |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 2. Tem các bộ phận chính

| Bộ phận | Hãng | Mã / model | Thông số (kW, vòng/phút, áp…) | Ảnh |
|---|---|---|---|---|
| Động cơ chính | | | | ☐ |
| Hộp số | | | | ☐ |
| Bơm (keo, mực, chân không, thuỷ lực) | | | | ☐ |
| Biến tần (chỉ để tra tài liệu) | | | | ☐ |
| Bộ điều khiển / màn hình máy (chỉ để tra tài liệu) | | | | ☐ |

## 3. Màn hình điều khiển của máy

☐ Ảnh trang thông số chính ☐ Ảnh trang báo lỗi / danh sách mã lỗi của hãng ☐ Ảnh trang giờ chạy / bộ đếm

## 4. Tài liệu đang có

| Tài liệu | Có? | Ngôn ngữ | Nơi để |
|---|---|---|---|
| Sách vận hành | ☐ | | |
| Sách bảo trì / bôi trơn | ☐ | | |
| Sơ đồ điện | ☐ | | |
| Danh mục phụ tùng | ☐ | | |
| Biên bản lắp đặt, nghiệm thu | ☐ | | |

## 5. Nhà cung cấp / dịch vụ

Đại lý bán: …… · Đơn vị sửa gần nhất: …… · Liên hệ (công ty, không ghi số cá nhân vào git): ……

| Người khảo sát | Ngày | Bảo trì xác nhận |
|---|---|---|
| | | |

Sau khảo sát: cập nhật `data/may-moc.yaml` (hãng, model, năm) và sổ lý lịch máy (`templates/so-ly-lich-may.md`); tìm sách theo skill `mp-bao-tri`.
