# Lộ trình phát triển repo

Repo bản 1.0 (17/10/2026) dựng từ: web và hồ sơ năng lực Minh Phúc, thư viện 132 tài liệu chuyên môn, file mổ xẻ 127 mã lỗi của xưởng, tài liệu
hướng dẫn và luật nghiệp vụ MP MES (phía người dùng). Phần lớn thông số vận hành chi tiết còn là **[KN ngành]** — muốn "siêu" thật thì phải nạp
dữ liệu thật của xưởng. Thứ tự đề xuất:

## Giai đoạn 1 — dữ liệu nền của xưởng (1–2 tháng)

1. **Khảo sát tem nhãn toàn bộ máy** (`templates/khao-sat-tem-nhan-may.md`) → cập nhật `data/may-moc.yaml` → tìm sách hãng → tóm vào skill tổ máy.
2. **Phiếu đếm "Lỗi khác" 1–2 tuần** → Pareto thật → sửa cột `top6` của `data/ma-loi.csv`, chốt ô lỗi mới.
3. **Phỏng vấn thợ chính** từng tổ, ghi thành văn bản: bảng chuẩn keo, góc bao gia nhiệt, khe lô kéo, quy ước khuôn, keo máy dán (`docs/CAN-XAC-NHAN.md` mục 2).
4. **Gom COA** giấy từng nhà cung cấp; danh sách nhà cung cấp vật tư phụ.
5. Xử lý xong các dòng "Cần xác nhận" về máy (M1–M9).

## Giai đoạn 2 — chuẩn hoá (2–4 tháng)

1. SOP cho từng máy từ `templates/sop-mau.md` + thông số đã xác nhận; đưa vào skill tổ máy.
2. Phiếu kiểm đầu đơn bắt buộc mọi máy; hồ sơ quy cách cho các mã hàng chạy thường xuyên.
3. Định mức tốc độ mục tiêu theo máy và nhóm sản phẩm (từ dữ liệu MES 1–2 tháng).
4. Bảng chuẩn tấm: công thức giấy ↔ ECT/BCT đo thật (QC ghi theo phiếu sản xuất).
5. Đánh giá rủi ro và quy trình LOTO viết riêng từng máy.

## Giai đoạn 3 — dữ liệu sống (song song)

1. Mẫu báo cáo tuần/tháng từ xuất Excel của MP MES (OEE ba thành phần, Pareto lỗi, Pareto dừng máy) — viết script đọc file Excel xuất ra (không đụng
   cơ sở dữ liệu, không cần quyền đặc biệt), đặt ở `tools/`.
2. Nối số QC theo lô với nhật ký MES theo phiếu → truy xuất một chạm khi khách khiếu nại.
3. Thư viện ca sự cố đã giải: mỗi sự cố lớn một trang (hiện tượng, nguyên nhân gốc, cách sửa, phòng ngừa) trong thư mục `ca-thuc-te` (tạo mới) dưới references của skill mp-xu-ly-su-co.

## Giai đoạn 4 — mở rộng

- Skill riêng cho máy in kỹ thuật số, máy cán màng, máy bế tròn khi có tài liệu.
- Skill giá thành (khi công ty cho phép đưa giá vào kho nội bộ riêng — không đưa vào repo này nếu repo được chia sẻ rộng).
- Bộ câu hỏi đào tạo có chấm điểm; bài giảng PDF xuất từ skill (`scripts/xuat_pdf.py`).
- Bản tiếng Anh của các skill hay dùng cho khách FDI (hồ sơ nhà cung cấp, trả lời kỹ thuật).

## Cách đo repo có "giỏi" lên không

- Tỷ lệ nội dung **[MP]** so với **[KN ngành]** trong các skill tổ máy (mục tiêu > 50 % sau giai đoạn 2).
- Số dòng còn lại trong `docs/CAN-XAC-NHAN.md`.
- Thợ/tổ trưởng hỏi Claude và làm theo được ngay (thu thập phản hồi, sửa skill).
