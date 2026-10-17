# Máy in flexo: cấu tạo, chuẩn bị đơn, xẻ rãnh, đếm

## 1. Một trạm in flexo carton [Chuẩn: NZQA 40327]

Hệ cấp mực · **lô gạt mực** (doctor roll) hoặc **dao gạt** (doctor blade, buồng kín) · **trục anilox** · **trục bản** (print cylinder) ·
**trục ép** (impression roll) · các cặp lô kéo tấm (pull rolls, pull collar rolls) · đầu in, lô cao su, tang trống.

- Một màu = một bản = một trạm; in 4 màu là 4 bản, 4 trạm nối tiếp. [MP-Web]
- Trục anilox (gốm, khắc hàng triệu ô) định lượng lớp mực trước khi truyền sang bản — "trái tim" của flexo. [MP-Web; Harper]
- Sau các trạm in: cụm **cán lằn – xẻ rãnh** (slotter) tạo lằn, khe, tai dán, góc cắt của thùng RSC.
- Phụ trợ: máy cấp phôi (feeder) — chuẩn nghề có module riêng [NZQA 40334].

## 2. Chuẩn bị đơn (make-ready)

| Bước | Việc | Kiểm |
|---|---|---|
| 1 | Đọc **tờ phiếu Bắt đầu sản xuất** trên MES: số lượng, quy cách, 6 trạm màu, khuôn bế, **bảng in**, layout, ghi chú, đường đi | Bảng in/khuôn "CHƯA KHAI" (chữ đỏ) thì hỏi trước khi lên máy |
| 2 | Lấy **bảng in** đúng mã: **BI + mã sản phẩm** (đơn mượn bản ghi đè trên kế hoạch); đúng vị trí kệ | Soát mã bản với phiếu (FX-13 sai nội dung bản do lấy nhầm bản) |
| 3 | Kiểm bản trước khi lên máy: bẩn, mòn, rách, bong băng dán | FX-11, FX-12 |
| 4 | Lên bản, **canh tâm trục bản** giữa các đơn (không canh tâm thì in lệch) | NZQA 40327 |
| 5 | Pha mực theo màu duyệt (Pantone), đo **độ nhớt, pH**; châm đủ mực | FX-04…07 |
| 6 | Đặt khe lô kéo theo **độ dày tấm thực đo** (không theo số mặc định) | Chống in ép bẹp sóng |
| 7 | Cài dao xẻ rãnh, bánh cán lằn, dao góc theo quy cách | FX-18…20 |
| 8 | Chạy **tờ đầu**: canh bản, canh chồng màu, so màu với mẫu duyệt, đo rãnh – lằn – tai dán | Ghi tờ thử vào ô **Thử máy** |
| 9 | Đánh dấu **chiều nạp tấm** (tránh in ngược mặt, ngược chiều — FX-16) | |
| 10 | Bấm **Start** trên MES = tuyên bố "chuẩn bị xong" — từ đó máy đứng là **ngừng**, không còn là pha mực | Skill `mp-ke-hoach-san-xuat` |

Mỗi đơn mới (ghi chú có chữ "mới") phải **chạy mẫu trước**; thời gian chạy mẫu là ngừng có kế hoạch, không phải lỗi thợ. [MP-MES]

## 3. Xẻ rãnh – cán lằn [Chuẩn: NZQA 40345; FEFCO QC]

- Thợ phải ra tấm đúng quy cách bằng thiết bị xẻ rãnh, cán lằn.
- Dung sai FEFCO: khe xẻ lệch tâm lằn dọc **±2 mm**, độ sâu khe **±5 mm**, mép khe không xơ; vị trí lằn đúng (2A).
- **[KN ngành]** Khe dán sai, "đuôi cá" ở máy dán thường bắt nguồn từ **lằn và khe ở máy in lệch**, không phải từ máy dán.
- Nhảy dao (FX-17): rãnh xẻ sai nhịp do dao xẻ trượt, tấm trượt → kiểm dao xẻ, bàn nạp. Có ô MES riêng **Nhảy dao**.

## 4. Đếm và đơn vị [MP-MES]

```
Số nhịp thực hiện = số máy đếm (nhịp) + "Chạy trước" (nhịp, thợ gõ — phần bộ đếm không có)
Sản lượng         = số nhịp thực hiện = số TỜ IN        (không nhân số con; cột số lượng cộng thêm tờ thử máy)
Tốc độ            = số nhịp ÷ tổng thời gian            (nhịp/phút — so được với tốc độ thiết kế)
```

- Ô **Chạy trước** là **nhịp**, không phải tấm; Start **không** xoá bộ đếm — gõ thêm phần đã có trên bộ đếm là đếm hai lần.
- Số con chỉ dùng để quy ra thùng khi đối chiếu với máy bế/dán; lỗi gõ theo **tờ in**, không nhân số con.
- "SP lệch" = sóng vào − số nhịp − tổng lỗi; **sóng vào** = số tấm của tổ sóng (số dao × số tấm/khổ), lấy từ nhật ký tổ sóng (thợ in không gõ).
- Máy đủ số lượng → hộp tự lưu (đếm ngược); bấm **Lưu đơn** = **xong đơn** dù thiếu số. Muốn chạy tiếp hôm sau dùng **Chuyển ngày**.

## 5. Đơn in 2 mặt [MP-MES, chốt 12/10/2026]

In hết **mặt 1** cả chồng giấy → lật chồng, thay bản và mực → in **mặt 2** đúng chồng đó, cùng số tờ → **một bản ghi**.
- Tích **In 2 mặt** ở tờ phiếu (ghi chú có "in 2 mặt"/"hai mặt" thì phần mềm tự tích sẵn); quên thì dùng nút **In 2 mặt** / **In tiếp mặt 2**.
- Mặt 1 đủ số → hộp **Xong mặt 1** đếm ngược 90 giây rồi tự sang mặt 2 (phần mềm dừng máy, số về 0, đơn vị "nhịp mặt 2").
- Thời gian **lật mặt** (từ tờ cuối mặt 1 tới lúc chạy mặt 2) tính là **pha mực/chuẩn bị**, không phải ngừng.
- Bản ghi: số nhịp = mặt 1 + mặt 2 (công máy, dùng tính tốc độ); số lượng = **số tờ** (chồng giấy); ghi chú mở đầu `[2 MẶT]`.

## 6. Đơn cán màng — máy in chạy hai lượt [MP-MES, chốt 24/08 và 14/09/2026]

Máy in **in** → hàng sang máy cán màng → quay lại **chính máy in đó** để **cắt rãnh**. Kế hoạch máy in chỉ có **một dòng** cho cả hai lượt;
giờ máy hai lượt tách riêng; hai lượt không chạy cùng lúc, có thể cách nhau mấy ngày. Nhãn lượt `[IN]` / `[CẮT RÃNH]` ở đầu ghi chú.
Lượt cắt rãnh là **đơn thường** — kế hoạch xếp ngày nào chạy ngày đó.

## 7. Chuyển máy [MP-MES]

Chỉ chuyển đơn **Máy In 1 ↔ Máy In 2** (cùng công đoạn In, cùng bảng in flexo). Đơn máy offset không chuyển sang flexo và ngược lại.
Sơ đồ mặt bằng trên tờ phiếu: **MI2 trong, MI1 ngoài** — liếc khối sáng để không chạy nhầm máy.
