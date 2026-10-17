# Sổ lý lịch máy và tài liệu máy

## 1. Vì sao cần tem nhãn

Ảnh máy trong hồ sơ năng lực phần lớn là **ảnh minh hoạ của hãng**; web chỉ nêu đúng **Mitsubishi** (offset 5 màu), **YB-1300E** (máy bồi),
**115SC** (máy xén). Không có hãng/model thì không tìm được sách hướng dẫn, sơ đồ, danh mục phụ tùng, mã lỗi chính hãng. [MP-Web][MP-HSNL]

## 2. Khảo sát tem nhãn — chụp gì ở mỗi máy

Dùng `templates/khao-sat-tem-nhan-may.md`. Mỗi máy (và mỗi cụm lớn của dây chuyền sóng):
1. Tem nhãn chính: hãng, model, số máy (serial), năm sản xuất, nước sản xuất, khổ máy, tốc độ tối đa, điện áp, công suất.
2. Tem động cơ chính, hộp số, bơm, quạt lớn (hãng, kW, vòng/phút, mã).
3. Tem biến tần, bộ điều khiển (chỉ để tra tài liệu — **không** sửa chương trình).
4. Màn hình điều khiển: ảnh trang thông số, trang báo lỗi (để lập bảng mã lỗi của hãng).
5. Tài liệu giấy đang có ở phòng Bảo trì: sách vận hành, sách bảo trì, sơ đồ điện, danh mục phụ tùng.
6. Nhà cung cấp/đại lý đã bán, đã sửa máy; liên hệ.

Danh sách cụm cần chụp của dây chuyền sóng: giá cuộn + bộ nối (mỗi trạm), máy một mặt A/C/E, máy một mặt B, cầu dẫn, gia nhiệt ba trục, máy tráng keo,
máy dán đôi (bàn nhiệt), dao cắt dọc – cán lằn, dao cắt ngang, xếp tấm, bếp keo, lò hơi.

## 3. Sổ lý lịch máy

Mẫu `templates/so-ly-lich-may.md`, mỗi máy một sổ (giấy hoặc file):
- Thông tin máy (từ tem nhãn), ngày đưa vào dùng, vị trí trong xưởng, mã máy trên MES (DS1, MI1, MI2, MI3, DT1, DT2, BF1, BF2, BOI).
- Bản đồ bôi trơn, lịch bảo trì phòng ngừa (từ `bao-tri-phong-ngua-theo-may.md`).
- Danh sách phụ tùng hao mòn và phụ tùng quan trọng: mã, nhà cung cấp, thời gian đặt hàng, tồn tối thiểu.
- Nhật ký hỏng – sửa: ngày, hiện tượng, nguyên nhân gốc, việc đã làm, phụ tùng, giờ dừng, người sửa.
- Thay đổi, cải tạo máy (ngày, nội dung, người duyệt).

## 4. Tìm sách hãng khi đã có tem nhãn

1. Trang web hãng (mục download/support) theo model chính xác.
2. Đại lý tại Việt Nam / Trung Quốc (nhiều máy carton là hàng Trung Quốc — tra bằng tên tiếng Trung của máy, xem bảng thuật ngữ `data/thuat-ngu.csv`).
3. Lưu bản tải về vào thư viện ngoài git (`thu-vien/may-moc/<máy>/`), ghi nguồn vào `sources/nguon.tsv` (skill `mp-thu-vien`).
4. Tóm tắt phần dùng nhiều (thông số, lịch bảo trì, bảng mã lỗi) vào skill tổ máy tương ứng, gắn nguồn **[Sách hãng]**.
