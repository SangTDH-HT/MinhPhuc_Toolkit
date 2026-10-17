# Sáu loại thời gian và luật phân loại

Nguồn: luật đang chạy trong MP MES và các câu đã chốt 25/08 – 13/10/2026 [MP-MES]. Phần mềm **tự phân loại từng giây** — thợ không chọn cột.

## 1. Sáu loại

| # | Loại | Khi nào |
|---|---|---|
| 0 | **Chạy máy** | Sản lượng đang tăng |
| 1 | Ngừng **không** kế hoạch (KOKH) | Máy đứng, không thuộc loại nào khác |
| 2 | Ngừng **có** kế hoạch (COKH) | Máy đứng, đơn ghi chú "hàng mẫu" — hoặc **kế hoạch không còn đơn nào** |
| 3 | Nghỉ ca | Máy đứng trong khung giờ nghỉ |
| 4 | Bảo trì | Thợ chọn bảo trì **và đã ghi lý do** |
| 5 | Pha mực / chuẩn bị | Còn đơn để chạy nhưng chưa chọn đơn hoặc chưa bấm Start (máy in) |

Tách bốn loại ngừng vì báo cáo hiệu suất **chỉ trừ ngừng không kế hoạch**. Gộp hết vào một chỗ thì máy nào cũng thành kém.

## 2. Thứ tự ưu tiên (xét từ trên xuống)

| | Điều kiện | Ra |
|---|---|---|
| 1 | Trong khung nghỉ **và** sản lượng không tăng | Nghỉ ca |
| 2 | Thợ chọn bảo trì **và** đã ghi lý do | Bảo trì |
| 3 | Sản lượng đang tăng | Chạy máy |
| 4 | Thợ bấm nút **Pha mực** | Pha mực |
| 4b | Kế hoạch không còn đơn nào | Ngừng có kế hoạch |
| 4c | Chưa chọn đơn, hoặc chưa bấm Start cho đơn này | Pha mực |
| 5 | Start bật, sản lượng đứng **chưa quá 30 giây** | Chạy máy (ân hạn) |
| 6 | Đơn ghi chú "hàng mẫu" | Ngừng có kế hoạch |
| 7 | Còn lại | Ngừng không kế hoạch |

## 3. Những chỗ dễ hiểu nhầm

- **Nghỉ ca thắng tất cả** — nhưng máy vẫn ra hàng trong giờ nghỉ thì **không** tính nghỉ.
- **Bảo trì chưa ghi lý do** → rơi xuống ngừng không kế hoạch (để "bảo trì" không thành chỗ giấu máy hỏng). **Bấm chạy lại là hết bảo trì**, lý do giữ vào ghi chú.
- **30 giây ân hạn**: máy in chậm nhất cũng vài chục tấm một phút; dưới 30 giây đứng (với tay lấy giấy) vẫn là chạy. Khi chắc chắn là ngừng (quá 30 giây,
  hoặc thợ bấm Tạm dừng / ghi bảo trì trước mốc đó), số giây ân hạn đã cộng vào chạy được **trả về** cột ngừng. Ân hạn nối qua cả lần tắt – mở phần mềm.
- **Pha mực hỏi đúng một câu**: đã bấm Start cho một đơn đã chọn chưa? Chưa → pha mực (chuẩn bị). Đã Start → máy đứng là ngừng.
- **Hết đơn không phải pha mực**: kế hoạch trống hoặc mọi đơn đã xong → máy đứng vì không có việc → **ngừng có kế hoạch**.
- Nút **Pha mực** kéo quãng đứng sau Start ra khỏi KOKH (pha mực cho đơn kế là đang làm việc) — nhưng không thắng nghỉ ca, bảo trì.
- **In 2 mặt**: quãng lật mặt là pha mực/chuẩn bị.
- **Ngưng đơn** (TP): quãng từ lúc ngưng tới đơn kế thuộc bản ghi **kế tiếp** — khai ngay lúc ngưng: chạy đơn khác (chuẩn bị của đơn kế), máy nghỉ
  (ngừng có kế hoạch, hết khi chọn đơn kế), máy hỏng (bảo trì, hết khi Start).

## 4. Ca và Bảng 01 (chốt 09/10/2026)

| Ca đang chạy | Khung nghỉ ca (máy không chạy là nghỉ ca) |
|---|---|
| Ca hành chính | Ô nghỉ dòng Ca hành chính (trưa, mặc định 11:30–12:30) **và** ô nghỉ dòng Tăng ca (chiều, mặc định 16:30–17:00) |
| Ca 01 / Ca 02 | Chỉ ô nghỉ của chính dòng đó (mặc định Ca 01 11:30–12:30, Ca 02 17:00–18:00) |

- Ca nhận theo **giờ mở** phần mềm; chạy liền qua giờ vào ca sau thì **tự đổi ca** (tên ca + khung nghỉ), đơn đang chạy không bị cắt.
- **Trước giờ vào ca** đồng hồ đứng (tới sớm bật máy tính không tính giờ) — trừ khi máy **ra hàng**: lần ra hàng đầu tiên kéo giờ bắt đầu đơn về lúc đó.
  Bấm Start suông không ra tấm thì không kéo. Lưu đơn trước giờ vào ca thì đơn sau tính từ giờ vào ca.
- Bảng 01 (ca, giờ nghỉ, tăng ca) do Quản lý nhập ở Cài đặt từng trạm.
- **Tổ sóng không có cột nghỉ ca**: dao đứng là ngừng không kế hoạch, trừ khi khai "Dừng có kế hoạch" hoặc "Dừng bảo trì" (có lý do) ở khung Thời gian.
- Máy thành phẩm: **chuẩn bị** (canh khuôn, lên keo, chạy thử) hiện riêng trên Trang chủ, nhưng khi lưu nhật ký **cộng chung vào ngừng không kế hoạch**.
- Giờ làm việc văn phòng công bố: Thứ 2 – Thứ 7, 07:30 – 16:30. [MP-Web]

## 5. Tổng thời gian và tốc độ theo loại máy (chốt 02/10/2026)

| Loại máy | Tổng thời gian tính tốc độ ("thời gian tổ máy làm chủ") | Tốc độ |
|---|---|---|
| Máy in (flexo, offset) | chạy + KOKH + pha mực | nhịp ÷ tổng → **nhịp/phút** |
| Thành phẩm (dán, bế, bồi) | chạy + KOKH (**chuẩn bị gộp vào KOKH**) | nhịp ÷ tổng → **nhịp/phút** |
| Tổ sóng | chạy + KOKH | mét ÷ tổng → **m/phút** |

Ngừng có kế hoạch, bảo trì, nghỉ ca **không** vào tổng — tổ máy không quyết được những quãng đó.
Kiểm một dòng nhật ký: sáu cột giờ cộng lại phải khớp khoảng **Từ → Đến** của bản ghi.

## 6. Khi phần mềm tắt giữa ca

Phần mềm lưu "phiên làm việc"; mở lại thì **bù** quãng tắt theo cột thợ đã khai (bảo trì / chờ giấy / hàng mẫu); tổ sóng: dao đứng ≤ 5 phút lúc tắt thì
quãng tắt vào cột ngừng theo luật, > 5 phút coi như máy tắt. Mất kết nối máy chủ: số vẫn đếm, chưa lên máy chủ — **đừng tắt phần mềm**, chờ mạng rồi lưu.
