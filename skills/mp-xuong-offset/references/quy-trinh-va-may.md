# Xưởng offset: máy, gia công, đếm và bản kẽm

## 1. Máy [MP-HSNL][MP-Web][MP-MES]

| Máy | Năng lực công bố | Trên MES | Ghi chú |
|---|---|---|---|
| Máy xén **115SC** | 45 lần/phút | — | Xén giấy cho in và thành phẩm |
| Máy in offset 5 màu **Mitsubishi** | 250 tờ/phút | **Máy In Offset** (mã MI3), **5 trạm mực**, đếm nhịp, sản lượng = tờ | **Không có nút Start vật lý** ngoài máy — lệnh chạy từ phần mềm |
| Máy cán màng nhiệt | — | — (ERP: công đoạn "MB – Cán màng bóng") | OPP/PE bóng, mờ, 1–2 mặt |
| Máy bồi tự động **YB-1300E** | ≥ 56.000 sp/8 giờ | **Máy bồi** (mã BOI), 1 lần cảm biến = 1 tấm, sản lượng = tấm | Không in phiếu nhận dạng (ra tấm, chưa thành thùng) |
| Máy bế phẳng (xưởng offset) | — | (tổ thành phẩm) | Bế hộp, khay |
| Máy dán tự động (xưởng offset) | — | (tổ thành phẩm) | Gấp dán hộp |

Model, năm, khổ tối đa, hệ cấp ẩm của máy Mitsubishi **chưa có** — cần tem nhãn (`templates/khao-sat-tem-nhan-may.md`).

## 2. Gia công bề mặt có tại Minh Phúc [MP-HSNL tr. 26]

UV bóng / mờ / satin / định hình · phủ varnish, OPV · cán màng OPP/PE 1 hoặc 2 mặt · tráng metalize · ép kim · dập nổi · đóng mắt cáo ·
túi giấy có quai.

## 3. Bản kẽm — kho thứ ba [MP-MES]

| Kho | Của máy | Mã |
|---|---|---|
| Bảng in flexo | Máy In 1, 2 | BI + mã sản phẩm |
| **Bản kẽm offset** | Máy In Offset | **BK + mã sản phẩm** |
| Khuôn bế | máy bế | KB + mã sản phẩm |

- Cùng một mã sản phẩm chạy hai công nghệ là **hai bản khác nhau** (hai mã khác nhau trong sổ vị trí).
- Đơn máy offset **không chuyển** sang máy flexo được và ngược lại (bản kẽm không lắp lên máy flexo).
- Kế hoạch có 6 ô màu nhưng máy offset có **5 đơn vị màu**; đơn lỡ ghi màu vào trạm 6 thì phần mềm vẫn hiện để sửa (không giấu).
- Thay bản kẽm theo số lượt in (OF-14). Sơ đồ kệ kho bản kẽm **chưa có bản vẽ** — đang tạm chép cách xếp của kho bảng in.

## 4. Máy xén (guillotine) [Chuẩn: ICPCBF2210, ICPCBF3210]

- Chuẩn bị: đọc lệnh; xác định **cạnh tay kê và cạnh lề** của tờ; **kiểm độ sắc dao** (dao cùn phải báo và thay); thay **thanh kê dao**
  (cutting stick) khi cần.
- Thiết lập: chỉnh máy, **áp lực kẹp giấy** theo lệnh; cắt mẫu, kiểm, chỉnh; trong sản xuất theo dõi dao, thanh kê, áp lực, vị trí dao so mẫu duyệt.
- Báo hỏng hóc vượt phạm vi cho người phụ trách; kiểm lại sau sửa.
- **An toàn [KN ngành]**: rèm ánh sáng, điều khiển hai tay, **không bao giờ với tay vào vùng dao khi máy còn điện**; thay dao bằng dụng cụ chuyên dùng,
  khoá năng lượng (LOTO) — skill `mp-an-toan-lao-dong`.

## 5. Đơn vị đếm trên MES

| Máy | Một lần đếm | Sản lượng | Tốc độ |
|---|---|---|---|
| Máy In Offset | nhịp | tờ | nhịp/phút |
| Máy bồi | tấm | tấm | nhịp/phút (= tấm/phút) |

Máy bồi đi chung Trang chủ tổ thành phẩm (máy dán, máy bế); có **Ngưng đơn** để dừng giữa chừng rồi chạy tiếp một bản ghi (skill `mp-mes-su-dung`).
