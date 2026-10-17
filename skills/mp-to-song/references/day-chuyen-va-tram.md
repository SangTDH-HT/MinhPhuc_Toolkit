# Dây chuyền tạo sóng: cụm máy và trạm

## 1. Các cụm máy theo thứ tự đường giấy

| # | Cụm (Việt) | Tiếng Anh | Tiếng Trung | Làm gì | Trạm Minh Phúc |
|---|---|---|---|---|---|
| 1 | Giá đỡ cuộn + nối giấy tự động | Reel stand, splicer | 原纸架, 接纸机 | Cấp cuộn, đổi cuộn không dừng máy | mỗi trạm |
| 2 | Lô gia nhiệt sơ bộ, lô gia ẩm | Preheater, preconditioner | 预热器, 预调器 | Làm nóng giấy mặt (bắt đầu hồ hoá keo), làm mềm giấy sóng bằng nhiệt + hơi ẩm để tạo sóng không gãy | trạm sóng |
| 3 | Máy tạo sóng một mặt | Single facer | 单面机 | Trục sóng tạo sóng, lô keo bôi keo đỉnh sóng, trục ép dán giấy sóng với giấy mặt | **trạm sóng A/C/E**, **trạm sóng B** |
| 4 | Cầu dẫn | Bridge | 天桥 | Tích giấy một mặt thành nếp gấp, cho máy dán đôi chạy khác tốc độ khi đổi cuộn, đổi đơn | giữa trạm sóng và trạm ghép |
| 5 | Gia nhiệt ba trục + máy tráng keo | Triplex preheater, glue machine | 三联预热器, 涂胶机 | Làm nóng giấy một mặt, bôi keo đỉnh sóng mặt còn lại | **trạm ghép** |
| 6 | Máy dán đôi — bàn nhiệt | Double backer, hot plates | 双面机, 热板 | Dán giấy mặt ngoài, hồ hoá keo, đuổi ẩm | **trạm ghép** ("mền" = băng/đệm ép trên bàn nhiệt) |
| 7 | Dao cắt ngang loại bỏ | Rotary shear | 旋转剪切 | Cắt bỏ đoạn hỏng, đổi quy cách | |
| 8 | Dao cắt dọc – cán lằn | Slitter-scorer | 纵切压线机 | Cắt khổ, cán lằn theo chiều máy — quyết định kiểu hộp | |
| 9 | Dao cắt ngang chiều dài | Cut-off knife | 横切机 | Cắt tấm đúng chiều dài — **nơi MES đếm "dao"** | **dao chặt** |
| 10 | Xếp tấm | Stacker | 堆码机 | Xếp chồng, chuyển sang máy in hoặc kho | |
| — | Bếp keo | Starch kitchen | 制胶系统 | Nấu keo tinh bột theo công thức | |
| — | Hệ hơi | Steam system | 蒸汽系统 | Lò hơi, van, bẫy hơi, thu nước ngưng cho mọi trục nóng | |

[Chuẩn: FEFCO; AOPack; NZQA 40340] — cột "Trạm Minh Phúc" ghép theo mô tả của xưởng [MP-MES]; chi tiết cơ khí từng trạm cần tem nhãn.

Máy một mặt gồm: giá cuộn, trục sóng, trục ép, lô gia nhiệt, cụm keo, khí nén, dẫn giấy, hút chân không. Hai loại: truyền thống và
**cassette** (thay trục sóng nhanh, hợp đơn ngắn đổi sóng nhiều). Giữ giấy sóng sát trục sóng dưới bằng **ngón giữ** hoặc **hút chân không**. [AOPack]

## 2. Sóng nào chạy ở trạm nào [MP-MES]

- Trạm A/C/E: một máy một mặt, chạy sóng **A, C hoặc E** tuỳ đơn (màn hình MES ghi "Sóng A/C/E"; đổi sóng là đổi trục sóng — cách đổi cần xác nhận).
- Trạm B: sóng **B**.
- Tấm 3 lớp: một trạm sóng + trạm ghép. Tấm 5 lớp BC: trạm B + trạm C + trạm ghép (thêm giấy mặt giữa).

## 3. Thao tác đầu ngày và trong ca tại trạm [MP-MES — luật của xưởng]

- Đầu ngày thợ phải bấm **Bắt đầu** ở màn hình trạm sóng thì trạm mới được đếm; sang ngày mới phải bấm lại.
- Nhập **mét lỗi** ở màn hình hai cụm sóng: gõ số mét vào ô nhập, máy tự cộng dồn sang ô bên cạnh, ô nhập về 0 sau 2 giây;
  **nhập số âm để sửa** khi gõ nhầm.
- Trạm ghép có **đèn/còi "sắp hết đơn"** khi phần đơn còn lại ở trạm ghép ≤ ngưỡng mét cài đặt — chuẩn bị đổi đơn, đổi giấy.
- Phần mềm MES đếm theo dao; dao đứng quá **5 phút** lúc tắt phần mềm thì coi như máy tắt (không cộng quãng tắt vào giờ chạy).

## 4. Đơn vị và đại lượng

| Đại lượng | Nghĩa |
|---|---|
| Dao (nhát dao) | Một lần dao cắt ngang chặt = một **khổ** đầy ("tấm giấy" khổ đầy theo cách gọi của kế hoạch) |
| Số tấm/khổ | Một nhát dao ra mấy tấm (số đường cắt dọc) |
| SL giấy tấm (kế hoạch) | Số **nhát dao** phải chặt — dao đếm tới số này thì tự chốt đơn |
| Số dao (nhật ký sóng) | Số nhát đã chặt; so kế hoạch, đối chiếu, mét, tốc độ tổ sóng đều đo theo **dao** |
| Số tấm thực | = số dao × số tấm/khổ — số tấm rời sang máy in (máy in lấy làm "Sóng vào"; MES ghi thêm cột này từ 15/10/2026) |
| Mét dài | = số dao × tổng dài tấm — dùng tính tốc độ (m/phút) và mét lỗi |
| Khổ giấy LT / SD | Khổ giấy lý thuyết / khổ giấy sử dụng thực (cột trên kế hoạch) |
| Tổng dài × tổng rộng | Kích thước tấm (phủ bì tấm) |
| Quy cách phủ bì, quy cách cán lằn | Kích thước tấm và vị trí các lằn do dao cắt dọc – cán lằn tạo |
