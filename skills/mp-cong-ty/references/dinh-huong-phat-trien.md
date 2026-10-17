# Định hướng phát triển và đòi hỏi với người kỹ thuật

Web và hồ sơ năng lực không có mục "kế hoạch tương lai" ghi rõ. Dưới đây là **dấu hiệu có bằng chứng** [MP-Web][MP-HSNL];
phần "đòi hỏi" là suy luận để định hướng việc học và việc cải tiến — gắn nhãn [Suy luận].

## 1. Nhịp đầu tư

2011 thành lập → 8/2017 đổi tên, đầu tư máy → 2019 mở rộng xưởng flexo → 8/2022 xưởng offset → 2024 FSC →
2025 chi nhánh Dĩ An (theo HSNL) → 2026 web mới + MP MES. Cứ 2–3 năm một bước lớn. [Suy luận]

## 2. Năm hướng và đòi hỏi

| # | Hướng | Bằng chứng | Đòi hỏi ở kỹ thuật [Suy luận] |
|---|---|---|---|
| 1 | Bao bì xanh, FSC, xuất khẩu EU | Trang "Bao bì xanh" (FSC, mực gốc nước, giấy tái chế, tối ưu vật liệu); FSC trên mọi trang; nhắc ESG, quy định chống phá rừng EU | Tách và đánh dấu lô giấy FSC trong kho và trên chuyền, giữ truy xuất theo FSC-STD-40-004, in đúng nhãn FSC-STD-50-001; quản lý mực gốc nước |
| 2 | Nhà máy FDI trong KCN, khách xuất khẩu | Web tiếng Anh; trang theo ngành (may mặc, giày da, điện tử, thuỷ sản, nông sản); ISO 3394, container, ISTA | Hồ sơ quy cách cố định cho từng mã, "lô sau giống lô trước"; giữ khuôn – bản để chạy bổ sung nhanh; phiếu kết quả QC theo lô; hiểu thử nghiệm vận chuyển ISTA |
| 3 | Hộp cao cấp, quà tặng, hộp tiếp xúc thực phẩm | Xưởng offset Mitsubishi đủ gia công; hộp PNJ, hộp quà Tết; hộp gà rán, burger | Quản lý màu offset giữa các lô, chất lượng bồi (không phồng, không tách lớp), gia công bề mặt; vệ sinh và vật liệu đạt chuẩn hộp tiếp xúc thực phẩm |
| 4 | Bán hàng số, rút ngắn báo giá – mẫu | Công cụ BCT/CBM, dựng hộp 3D, catalog 45 mẫu, báo giá 4 giờ, mẫu 1–3 ngày | Nhiều đơn nhỏ, quy cách riêng → **đổi khuôn, đổi bản nhanh** (SMED), kế hoạch chạy máy chặt; chuyển mẫu kỹ thuật số sang hàng loạt không lệch màu, lệch kích thước |
| 5 | Chất lượng đo bằng máy | "Kiểm soát chất lượng bằng máy đo, không chỉ bằng cảm quan"; phòng QC 7 thiết bị | Hiểu quan hệ thông số máy sóng (keo, nhiệt, ép) ↔ ECT/BCT; đọc số QC để chỉnh máy; nối dữ liệu MP MES với dữ liệu QC theo lô |

## 3. Chân dung người kỹ thuật giỏi ở Minh Phúc [Suy luận]

1. Nắm chắc **cả hai xưởng**: flexo (sóng → in → bế → dán) và offset (xén → in → gia công → bồi → bế → dán).
2. Biết **vật liệu**: loại giấy, định lượng, hướng sóng, độ ẩm, keo, mực gốc nước — phần lớn lỗi thùng bắt đầu từ vật liệu.
3. **Đo và đọc số QC** (BCT, ECT, RCT, bục, Cobb) để truy ngược về máy.
4. **Đổi đơn nhanh**: khuôn bế, bản in, chỉnh máy theo quy cách từng đơn.
5. Hiểu **FSC, ISO 9001, an toàn thực phẩm** ở mức thao tác trên chuyền.
6. Đọc **số liệu MP MES** (6 loại thời gian, tốc độ, lỗi, Lỗi khác) để tìm chỗ mất năng suất.
7. Bảo trì phòng ngừa cho từng máy, ghi sổ máy, biết khi nào dừng máy.

## 4. Những việc lớn đang mở (10/2026)

- Tách "Lỗi khác" thành mã lỗi thật: file mổ xẻ 127 mã + phiếu đếm 1–2 tuần (skill `mp-xu-ly-su-co`).
- Lắp cảm biến nhíp chống đếm đôi cho máy bế (phần mềm đã làm sẵn, chờ lắp).
- Khảo sát tem nhãn máy để có sách hướng dẫn chính hãng (`templates/khao-sat-tem-nhan-may.md`).
- Lộ trình phát triển của repo này: `docs/LO-TRINH.md`.
