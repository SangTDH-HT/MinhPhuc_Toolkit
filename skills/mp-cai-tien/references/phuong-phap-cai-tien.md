# Phương pháp cải tiến

Phương pháp chuẩn của nghề quản lý sản xuất **[KN ngành]**, áp vào dữ liệu và tổ chức của Minh Phúc.

## 1. PDCA trên một trang A3

| Ô A3 | Nội dung | Nguồn số ở Minh Phúc |
|---|---|---|
| 1. Bối cảnh | Vì sao việc này quan trọng (khách, chi phí, an toàn) | Khiếu nại, báo cáo tháng |
| 2. Hiện trạng | Số đo hiện tại, Pareto, ảnh | MP MES: tab Dữ liệu, Hiệu suất, Nhật ký theo phiếu; phiếu đếm Lỗi khác |
| 3. Mục tiêu | Chỉ số, mức, thời hạn | Cùng định nghĩa chỉ số trước – sau |
| 4. Phân tích | Xương cá 6 nhóm, 5 Why | skill `mp-xu-ly-su-co` |
| 5. Biện pháp | Ai, làm gì, khi nào | |
| 6. Kết quả | Số sau, so mục tiêu | MES cùng khoảng ngày dài như trước |
| 7. Chuẩn hoá & bài học | SOP, phiếu kiểm, đào tạo | `templates/sop-mau.md` |

Mẫu: `templates/a3-cai-tien.md`.

## 2. Lấy số từ MP MES (máy Giám sát, Quản lý trở lên)

| Câu hỏi | Ở đâu |
|---|---|
| Máy nào OEE thấp, thấp ở thành phần nào | NHẬT KÝ → **Hiệu suất** (sẵn sàng × hiệu năng × chất lượng, nhiều ngày) |
| Đơn nào lệch kế hoạch | tab **Dữ liệu → So kế hoạch** |
| Bản ghi bất thường (có hàng không có giờ, tốc độ vô lý) | **Dữ liệu → Đơn cần xem lại** |
| Dữ liệu có đáng tin không | **Dữ liệu → Sức khoẻ dữ liệu** (sửa dữ liệu trước khi kết luận) |
| Dừng máy vì sao | Nhật ký: các cột ngừng + lý do; cảnh báo SX-01, SX-22 |
| Ai sửa gì | Cài đặt → Báo cáo thao tác |
| Hỏi nhanh bằng lời | **Trợ lý** ("hôm qua MI1 có sự cố gì", "đơn nào thiếu so kế hoạch") |
| Xuất ra phân tích | Xuất Excel ở mọi tab |

## 3. Pareto

Gom 2–4 tuần → xếp giảm dần → vẽ cột + đường tích luỹ → chọn 2–3 mục đầu (~80 %). Với lỗi: đếm theo **mã lỗi** (TS/FX/OF/BO/BE/DA/CH), không theo ô
"Khác". Với dừng máy: theo **lý do** đã khai. Máy tính: `python -m mptinh pareto --file du-lieu.csv`.

## 4. Chuẩn hoá công việc

- **SOP tại máy** (`templates/sop-mau.md`): bước, điểm then chốt (vì sao), hình ảnh, thông số chuẩn, kiểm đầu đơn, an toàn.
- **Bảng thông số chuẩn** theo sản phẩm/giấy: tổ sóng (nhiệt, góc bao, keo theo giấy và tốc độ), máy in (anilox, độ nhớt, pH theo mã màu),
  máy dán (keo, áp, tốc độ) — hiện là "kinh nghiệm truyền miệng", cần ghi thành văn bản.
- **Hồ sơ quy cách mã hàng** — lô sau giống lô trước.

## 5. 5S và quản lý trực quan

5S (Sàng lọc · Sắp xếp · Sạch sẽ · Săn sóc · Sẵn sàng) + bảng tại máy: kế hoạch ca, OEE hôm qua, lỗi lớn nhất tuần, cảnh báo an toàn.
Kệ khuôn/bản theo **sổ vị trí** trên MES (mã BI/BK/KB) — chống lấy nhầm bản/khuôn.

## 6. Kaizen nhỏ của thợ

Phiếu đề xuất một trang: vấn đề — đề xuất — kết quả (ảnh trước/sau). Ghi nhận và thưởng nhỏ; nhiều cải tiến nhỏ của thợ cộng lại lớn hơn một dự án lớn.
