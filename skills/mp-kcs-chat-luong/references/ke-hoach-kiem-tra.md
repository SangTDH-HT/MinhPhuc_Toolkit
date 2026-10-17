# Kế hoạch kiểm tra tại Minh Phúc

Phần lớn bảng dưới là **đề xuất [KN ngành]** dựng trên thiết bị QC Minh Phúc đang có — trưởng KCS duyệt rồi đưa vào quy trình ISO.
Chỗ nào xưởng đã có quy định riêng thì quy định của xưởng thắng.

## 1. Điểm kiểm theo dòng chảy

| Điểm kiểm | Chỉ tiêu | Tần suất gợi ý | Thiết bị | Ghi vào |
|---|---|---|---|---|
| Nhập giấy cuộn | Định lượng, độ ẩm, Cobb, RCT (hoặc SCT), bục; ngoại quan cuộn | Mỗi lô, mỗi nhà cung cấp | Cân, máy RCT, bục, Cobb, kéo | `templates/phieu-kiem-tra-giay-cuon.md` |
| Đầu ra máy sóng | Kết cấu (giấy từng lớp), loại + hướng sóng, độ dày tấm, ECT, bám keo (xé), cong tấm, kích thước, vị trí lằn | Đầu mỗi đơn, khi đổi giấy, mỗi 1–2 giờ | Thước, máy ECT, bục | Kiểm đầu đơn (tổ sóng) |
| Sau in – xẻ rãnh | Nội dung bản, màu so mẫu, chồng màu, vị trí in, rãnh, lằn, tai dán, **độ dày sau in** (ép bẹp) | Tờ đầu + định kỳ | Thước, mẫu chuẩn | Kiểm đầu đơn (máy in) |
| Sau bế | Kích thước tâm lằn, lằn (nứt, nông), mép (bavia), tách rác, lệch bế so hình in | Tờ đầu + định kỳ | Thước | Kiểm đầu đơn (máy bế) |
| Sau dán | Khe dán, đuôi cá, bám keo mối dán (≥ 80 % xơ), keo tràn, vuông góc, số thùng mỗi bó | Thùng đầu + định kỳ | Thước, xé tay | Kiểm đầu đơn (máy dán) |
| Sau bồi | Lệch bồi, bám, phồng, cong sau khô, keo tràn | Tấm đầu + định kỳ | Thước, xé tay | Kiểm đầu đơn (máy bồi) |
| Thành phẩm / xuất hàng | **BCT theo lô**, AQL ngoại quan theo bảng FEFCO, kích thước, số lượng, phiếu nhận dạng pallet | Mỗi lô giao | Máy nén thùng | `templates/phieu-kiem-tra-xuat-hang.md` |

## 2. Kiểm đầu đơn (first article) — vì sao bắt buộc

Phần lớn mã lỗi của xưởng có phòng ngừa là "**đo/canh/soát tấm đầu đơn**" (TS-17, TS-20, FX-14, FX-15, FX-18, FX-20, BE-04, DA-07, DA-08…).
Kiểm đầu đơn là chốt rẻ nhất: sai ở tờ đầu thì mất vài tờ; sai cả đơn thì mất cả lô. Quy trình:

1. Thợ chạy tờ/thùng đầu (tờ thử ghi ô **Thử máy**).
2. Thợ tự kiểm theo phiếu (`templates/kiem-tra-dau-don.md`), so **mẫu duyệt** và **lệnh sản xuất**.
3. Tổ trưởng hoặc KCS ký xác nhận → mới chạy hàng loạt.
4. Mẫu đầu đơn đạt: lưu kèm số phiếu (để lô sau "giống lô trước").

## 3. Kiểm trong ca

- Định kỳ theo bảng mục 1; khi **đổi cuộn giấy, đổi mực, sau giờ nghỉ, sau sửa máy** phải kiểm lại (ví dụ thật FX-04 "mực loãng sau giờ nghỉ trưa").
- Thấy lỗi lặp: dừng, báo tổ trưởng; ghi lỗi đúng ô MES; lỗi không có ô → "Khác" + mã lỗi trong ghi chú.

## 4. Kiểm xuất hàng và hồ sơ lô

- Lô = mỗi đơn, hoặc mỗi pallet / mỗi chuyến xe với đơn lớn.
- Lấy mẫu ngẫu nhiên đầu – giữa – cuối lô; cỡ mẫu và số chấp nhận theo bảng AQL; lỗi cấp 1 không cho phép.
- **Phiếu kết quả theo lô** (khách KCN, xuất khẩu yêu cầu): BCT, ECT, RCT, bục, Cobb, định lượng — ghi **chuẩn thử** (ISO/TAPPI), điều kiện thử
  (có ổn định mẫu hay không), số phiếu sản xuất, ngày, người thử.
- Ký 4 ô trên phiếu nhận dạng pallet (người thật nhìn lô hàng).

## 5. Hàng không phù hợp (NCR)

1. **Cách ly và đánh dấu** (thẻ đỏ / khu riêng) — không để lẫn vào hàng đạt (CH-05 lẫn đơn).
2. Lập **phiếu NCR** (`templates/phieu-ncr.md`): mô tả, số lượng, số phiếu, máy, ca, ảnh.
3. Quyết định: dùng tiếp có điều kiện / chọn lại (sort) / sửa / hạ cấp / huỷ — người có thẩm quyền ký.
4. Ghi số hư vào đúng ô MES; số chọn lại ghi rõ trong ghi chú.
5. Tìm nguyên nhân (6 nhóm: NVL · Máy móc – khuôn bản · Vận hành · Khâu trước · Kỹ thuật – kế hoạch · Kho – vận chuyển) → hành động khắc phục.

## 6. Khiếu nại khách hàng

1. Nhận đủ thông tin: mã hàng, số lô/ngày giao, số lượng lỗi, ảnh, mẫu lỗi gửi về, điều kiện sử dụng (kho lạnh? xếp mấy tầng? máy dựng thùng?).
2. **Truy ngược**: số lô → phiếu sản xuất → MES (máy, ca, người vận hành, tốc độ, dừng máy, lỗi đã ghi) → phiếu QC của lô → lô giấy.
3. Thử lại mẫu lưu và mẫu khách gửi ở **23 °C / 50 % RH**.
4. Trả lời theo **8D** (`templates/bao-cao-8d.md`): ngăn chặn tạm thời trong 24–48 giờ, nguyên nhân gốc, khắc phục, phòng ngừa lặp lại.
5. Cập nhật hồ sơ quy cách mã hàng và phiếu kiểm đầu đơn để lỗi không lặp.

## 7. Thiết bị đo và mẫu lưu [KN ngành]

- Lập danh mục thiết bị đo (máy BCT, ECT, RCT, bục, Cobb, cân, thước, máy đo ẩm) với **lịch hiệu chuẩn/kiểm tra** (ngoài: hằng năm; nội bộ: hằng tháng
  bằng mẫu chuẩn hoặc quả cân) — yêu cầu ISO 9001 mục 7.1.5.
- Dao cắt mẫu ECT phải sắc, cắt vuông — dao mòn cho ECT thấp giả.
- Lưu mẫu thành phẩm mỗi lô (ít nhất 1–2 thùng) đủ lâu để trả lời khiếu nại (gợi ý 6–12 tháng tuỳ khách).
