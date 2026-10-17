# Báo giá — phần kỹ thuật

Repo **không chứa giá** (giá giấy, đơn giá công đoạn là dữ liệu kinh doanh nội bộ). Phần dưới giúp kinh doanh tính **lượng vật tư và công đoạn**
đúng, để ghép với bảng giá của phòng Kinh doanh.

## 1. Yếu tố làm nên giá [MP-Web]

| Yếu tố | Ảnh hưởng |
|---|---|
| Số lớp (3 hay 5) | 5 lớp dùng nhiều giấy hơn |
| Loại sóng | Sóng càng cao, hệ số co càng lớn → tốn nhiều giấy sóng hơn |
| Định lượng và loại giấy | g/m² càng cao càng đắt; kraft đắt hơn test |
| Kích thước và số lượng | Thùng lớn tốn giấy; số lượng lớn giảm đơn giá (chia chi phí khuôn, bản, chuẩn bị máy) |
| Số màu in | Càng nhiều màu càng tốn bản và mực |
| Gia công sau in | Cán màng, ép kim, UV, dập nổi, bế, dán đều cộng thêm |

Nguyên liệu chiếm khoảng **75 % giá thành thùng** [AOPack] → tính đúng diện tích và định lượng giấy là phần quan trọng nhất.

## 2. Chuỗi tính lượng giấy

```
1. Kích thước phôi (thùng RSC):  dài ≈ 2(D+t) + 2(R+t) + tai dán;  rộng ≈ C + R + 3t
2. Diện tích phôi (m²)          = dài × rộng / 10⁶
3. Định lượng tấm (g/m²)        ≈ Σ giấy mặt + Σ giấy sóng × hệ số co (+ keo)
4. Khối lượng giấy / thùng (g)  ≈ diện tích phôi × định lượng tấm
5. Cộng hao hụt                 : biên xén khổ, đầu cuộn, chuyển đơn, tờ thử, lỗi (theo số liệu xưởng)
```

Máy tính: `python -m mptinh phoi-rsc`, `python -m mptinh dinh-luong`. Hệ số co gần đúng: A 1,50–1,55 · C 1,42–1,48 · B 1,32–1,38 · E 1,22–1,30 [KN ngành].
Ví dụ 400 × 300 × 250, sóng C, 3 lớp 150/120/150: phôi ≈ 1.451 × 562 mm = 0,815 m²; tấm ≈ 474 g/m² + keo → ~0,39–0,40 kg giấy/thùng chưa tính hao hụt.

## 3. Số phôi trên một khổ (tổ sóng) và hao biên

```
Số phôi/khổ  = số nguyên lớn nhất sao cho  số phôi × rộng tấm + biên xén ≤ khổ giấy cuộn
Hao biên (%) = (khổ giấy − số phôi × rộng tấm) / khổ giấy × 100
```
Chỉnh kích thước vài mm có thể tăng số phôi/khổ hoặc số hộp/tờ in → giảm hao giấy — đây là chỗ Minh Phúc "chủ động tối ưu khi báo giá". [MP-Web]
Khổ cuộn đang có trong kho và biên xén tối thiểu của dây chuyền: hỏi kế hoạch/tổ sóng (chưa có trong repo). Máy tính: `python -m mptinh kho-giay`.

## 4. Công đoạn tính tiền

Theo 7 cờ công đoạn: Sóng · In (số màu, flexo/offset) · Bế (cần khuôn mới?) · Bồi · Dán (hay ghim — Đóng kim) · Khác (cán màng, UV, ép kim…).
Chi phí một lần: **khuôn bế** (mã KB…), **bảng in flexo** (BI…, mỗi màu một bản), **bản kẽm offset** (BK…). Đơn bổ sung mã cũ không tốn lại các khoản này
nếu khuôn, bản còn dùng được (kiểm sổ vị trí và tình trạng).

## 5. Kiểm báo giá trước khi gửi

- Kết cấu đủ bền cho tải và môi trường khách nêu (skill `mp-san-pham-ket-cau`).
- Kích thước lọt lòng ↔ phủ bì đúng; đã tính theo pallet/container nếu khách xuất khẩu.
- Số màu, mặt in, gia công đúng yêu cầu.
- Thời gian: mẫu 1–3 ngày, hàng loạt 3–5 ngày sau duyệt mẫu — kiểm tải máy với kế hoạch trước khi hứa đơn gấp.
