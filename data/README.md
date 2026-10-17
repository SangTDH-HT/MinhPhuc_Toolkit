# data/ — dữ liệu máy đọc được

| File | Nội dung | Nguồn | Cập nhật khi |
|---|---|---|---|
| `ma-loi.csv` | 127 mã lỗi (TS, FX, OF, BO, BE, DA, CH): tên, nhận biết, nguyên nhân, khâu, xử lý, ô MES, phòng ngừa, nhóm "Lỗi khác", hạng top 6 | File mổ xẻ "Lỗi khác" của xưởng (10/2026) | Có số đếm thật; chốt ô lỗi mới trên MES |
| `nhom-loi-khac.csv` | 7 nguồn của "Lỗi khác" | File mổ xẻ | |
| `nhom-nguyen-nhan.csv` | 6 nhóm nguyên nhân + ví dụ theo máy | Đề xuất 17/10/2026 | Khi được chốt |
| `o-loi-mes.csv` | Ô lỗi MES từng loại máy, lỗi gõ theo đơn vị nào | Hướng dẫn MES 2.0 | Khi MES đổi ô |
| `may-moc.yaml` | Xưởng, máy, mã MES, đơn vị đếm, năng lực công bố; hãng/model **null = chưa xác nhận** | HSNL, web, MES | Sau khảo sát tem nhãn |
| `song.csv` | Loại sóng: cao, bước, số sóng/30 cm, độ dày tính toán, hệ số co | Web MP, FEFCO QC, IS 2771, KN ngành | Khi đo được số của máy Minh Phúc |
| `phep-thu.csv` | Chỉ tiêu ↔ FEFCO / ISO / TAPPI / TCVN, phòng QC có máy không | FEFCO Testing methods, web MP | |
| `thuat-ngu.csv` | Thuật ngữ Việt – Anh – Trung (tiếng Trung là bản tham khảo, cần người đọc tiếng Trung xác nhận) | Sổ tay 00, web MP | |
| `mau-san-pham.json` | 45 mẫu đã sản xuất (MP-001 … MP-046, không có MP-005) | Catalog web | Web thêm mẫu |
| `khach-hang.csv` | Khách hàng công khai trên web / hồ sơ năng lực | Web, HSNL | |
| `nha-cung-cap.csv` | Nhà cung cấp giấy (đối tác liên kết theo HSNL); các vật tư khác chưa có | HSNL | Bổ sung |

Quy ước: UTF-8, CSV có dấu ngoặc kép, số thập phân kiểu Việt Nam trong cột chữ. **Không** đưa vào đây: giá, số điện thoại cá nhân, tài khoản, mật khẩu,
địa chỉ mạng, dữ liệu đơn hàng có tên khách chưa công khai.
