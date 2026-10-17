# Khoá năng lượng – treo thẻ (LOTO) và quy tắc làm việc gần máy

Nguyên tắc chung trước mọi lần chỉnh, sửa, gỡ kẹt: **dừng truyền động, cắt điện – khoá – treo thẻ, xả khí nén và hơi** [Chuẩn: TAPPI; HSE PIS18].
Quy trình chi tiết dưới đây là **[KN ngành]**, cần viết thành quy trình riêng cho từng máy (điểm cách ly cụ thể).

## 1. Các dạng năng lượng phải cách ly

| Dạng | Ở đâu | Cách ly |
|---|---|---|
| Điện | Mọi máy | Cầu dao/aptomat chính → khoá |
| Khí nén | Kẹp, xi lanh, bộ nối giấy, máy dán | Van chặn + xả áp |
| Hơi | Tổ sóng (lô gia nhiệt, bàn nhiệt), bếp keo | Van chặn + xả áp + chờ nguội |
| Thuỷ lực | Máy xén, bàn nâng (nếu có) | Xả áp, chèn |
| Cơ năng dự trữ | Bánh đà máy bế, lò xo | Chờ dừng hẳn, chèn |
| Trọng lực | Bàn ép, dao xén, bàn nâng xếp tấm, cuộn giấy treo | Hạ xuống vị trí thấp nhất hoặc chèn cơ khí |
| Nhiệt | Trục nóng, keo nóng | Chờ nguội, bảo hộ |
| Hoá chất | Đường keo, mực | Đóng van, xả |

## 2. Sáu bước LOTO

1. **Báo** người vận hành và người liên quan: máy sắp được khoá.
2. **Dừng máy** theo trình tự bình thường.
3. **Cách ly** mọi nguồn năng lượng (bảng trên).
4. **Khoá và treo thẻ**: mỗi người làm việc một ổ khoá riêng + thẻ có tên, ngày, lý do; nhiều người dùng khoá nhóm (hasp).
5. **Xả năng lượng dư** (áp khí, hơi, chèn bộ phận rơi được).
6. **Thử**: bấm Start/thử nút để chắc máy không chạy, rồi trả nút về vị trí dừng.

Gỡ khoá: dọn dụng cụ, lắp lại che chắn, đếm người, báo vận hành, **người treo khoá tự gỡ khoá của mình**.
Mẫu phiếu: `templates/phieu-loto.md`.

## 3. Gỡ kẹt và nút nhích

- Kẹt giấy/tấm ở khe trục, bàn ép, băng tải: **không** kéo khi máy chạy hoặc khi chỉ mới bấm dừng (máy còn quay theo quán tính).
- Gỡ kẹt nhỏ ở vùng **có che chắn khoá liên động**: mở cửa che chắn (máy tự cắt), gỡ, đóng lại — kiểm khoá liên động còn hoạt động.
- Gỡ kẹt phải đưa tay vào vùng nguy hiểm không có khoá liên động → **LOTO**.
- **Nút nhích (jog)** để quay trục từ từ khi xỏ giấy, canh bản: một người bấm, người đó **nhìn thấy** mọi người, không ai trong vùng kẹp; nói to trước khi bấm.

## 4. Bảo hộ cá nhân theo khu

| Khu | Bảo hộ |
|---|---|
| Mọi khu sản xuất | Giày bảo hộ, quần áo gọn (không áo rộng, không khăn quàng), tóc dài buộc gọn |
| Tổ sóng (trục nóng) | Găng chịu nhiệt khi chạm vùng nóng; **không găng vải khi gần trục đang quay** |
| Bếp keo | Kính che mặt, găng chống hoá chất, tạp dề |
| Thay dao, cầm khuôn | Găng chống cắt |
| Khu ồn (tổ sóng, máy bế) | Nút/chụp tai |
| Rửa mực, dung môi | Găng hoá chất, khẩu trang khi thông gió kém |
| Khu hộp tiếp xúc thực phẩm | Mũ trùm tóc, khẩu trang, rửa tay (skill `mp-fsc-iso-attp`) |

## 5. Huấn luyện

Thợ mới phải được huấn luyện **trên đúng máy mình đứng**: vị trí nút dừng khẩn, điểm cách ly, vùng nguy hiểm, quy trình gỡ kẹt, LOTO — ký sổ
huấn luyện (skill `mp-dao-tao`). Kiểm tra thiết bị an toàn (nút dừng khẩn, công tắc cửa, rèm ánh sáng) **đầu mỗi ca** như một mục của phiếu giao ca.
