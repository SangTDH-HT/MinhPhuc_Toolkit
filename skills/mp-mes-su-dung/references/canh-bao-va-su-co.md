# Đèn, cảnh báo và sự cố trên MP MES

Nguồn: hướng dẫn vận hành MES 2.0 và danh mục hệ cảnh báo (10/2026) [MP-MES]. Phần này nói **người dùng làm gì**; sửa kết nối, máy chủ, PLC là việc của Kỹ thuật.

## 1. Đèn trên thanh đầu — làm gì

| Thấy gì | Làm gì |
|---|---|
| **Đèn PLC vàng / đỏ** | Số trên màn đứng yên nhưng máy vẫn đếm. **Không tắt phần mềm.** Xem dây mạng ở tủ điện, đèn RUN của bộ điều khiển; có lại là tự nối. **Ghi tay số trên máy** trong lúc chờ |
| **Đèn Máy chủ đỏ** | Không lưu được đơn. **Không tắt phần mềm, không đổi đơn, cứ chạy tiếp.** Có mạng lại thì lưu như thường. **Quá 10 phút báo Kỹ thuật** |
| Cả PLC và Máy chủ cùng đỏ | Máy tính này mất mạng |
| Lưu đơn báo lỗi | Số liệu còn nguyên trên màn, chưa mất gì. Có mạng lại bấm Lưu đơn lần nữa |
| Hộp "Mất kết nối" | Nút **Copy lỗi** chép chi tiết để gửi Kỹ thuật (không chứa mật khẩu); **Bỏ qua 10 phút** chỉ tắt tiếng, đèn vẫn đỏ |

## 2. Chuông và dải cảnh báo

- **Chuông** trên thanh đầu đổi màu theo mức nặng nhất, kèm số cảnh báo đang mở; bấm xổ bảng: đang có + đã hết hôm nay.
- **Dải cảnh báo** dưới thanh đầu: chỉ cảnh báo thợ phải biết; không chặn thao tác. Có **Xem cách xử lý** (Làm gì trước · Nghĩa là gì · Thường do đâu),
  **Đã biết**, **Tạm ẩn 10 phút**, **Chép cho Kỹ thuật** (để dán Zalo).
- Ba mức: **Nghiêm trọng** (đang mất số / không làm việc được — tam giác) · **Cảnh báo** (có chuyện, số chưa mất — vòng tròn) ·
  **Báo sớm** (chưa có chuyện, nhưng đà này sắp có — mũi tên đi lên).
- Ở máy Giám sát: tab **CẢNH BÁO** (Đang có — băng sự cố 24 giờ; Lịch sử; Sức khoẻ trạm). Mở màn một máy thì chuông thu lại còn máy đó.

## 3. Danh mục cảnh báo (36 mã) — nghĩa với người dùng

Mức và ngưỡng là đặt ban đầu (10/2026), có thể đổi.

**Sản xuất (SX) — tổ trưởng, quản đốc cần để ý nhất**

| Mã | Tên | Mức | Làm gì |
|---|---|---|---|
| SX-01 | Máy đứng chưa khai lý do (mặc định 10 phút) | Cảnh báo | Bấm Tạm dừng / dòng ngừng, chọn đúng lý do; đơn phải dừng giữa chừng thì Ngưng đơn hoặc Chuyển ngày |
| SX-02 | Máy báo chạy mà không ra hàng | Cảnh báo (thợ thấy) | Kiểm kẹt, hết giấy, cảm biến đếm |
| SX-03 | Bộ đếm tăng khi máy báo dừng | Cảnh báo | Báo Kỹ thuật (cảm biến/đếm) |
| SX-04 | Mất cảm biến nhíp máy bế (khi đã lắp) — quay về đếm như cũ | Cảnh báo | Báo Kỹ thuật; soát số đếm đôi |
| SX-05 | Đơn đã vượt kế hoạch mà máy vẫn chạy (mặc định 5 %) | Cảnh báo | Dừng, kiểm số; lưu đơn |
| SX-06 | Máy chạy mà chưa chọn đơn | Cảnh báo (thợ thấy) | Chọn đơn ngay — số đếm lúc chưa có đơn không thuộc đơn nào |
| SX-21 | Tốc độ đang tụt | Báo sớm | Xem tấm cong, giấy, mực, máy |
| SX-22 | Máy dừng vặt liên tục | Báo sớm | Tìm nguyên nhân dừng lặp (bảo trì, vật liệu) |
| SX-23 | Đơn sắp xong | Báo sớm | Chuẩn bị đơn kế (bản, khuôn, giấy, mực) |

**Kết nối (KN)**: KN-01 mất kết nối PLC · KN-02 mất máy chủ dữ liệu · KN-03 trạm mất mạng · KN-04 PLC đứng · KN-05 PLC chập chờn ·
KN-06 lệnh xuống máy không tới · KN-07 máy chủ phản hồi chậm · KN-08 Giám sát không thấy trạm · KN-09 đang chạy chế độ giả lập ·
KN-21…23 báo sớm đường truyền chậm dần / rớt nhiều lần. → Người dùng: làm theo mục 1, báo Kỹ thuật kèm "Chép cho Kỹ thuật".

**Hệ thống (HT)**: ổ đĩa sắp đầy, đồng hồ lệch giờ máy chủ, cài đặt vừa phục hồi, phần mềm đơ, dùng nhiều bộ nhớ, có bản bắt buộc, lỗi lặp lại,
và báo sớm đĩa/bộ nhớ tăng dần. → Báo Kỹ thuật; không tự cài đặt lại.

**Dữ liệu (DL)**: DL-01 lưu đơn đang kẹt (quá 60 giây) — **Nghiêm trọng**, đừng tắt phần mềm; DL-05 có khoảng giờ không đếm được.

**Giám sát (GS)**: GS-01 trạm mất tin (máy đang chạy thì Nghiêm trọng) · GS-02 nhiều trạm mất tin cùng lúc · GS-03 máy Giám sát không đọc được máy chủ ·
GS-04 trạm chạy bản phần mềm cũ · GS-21 tin của trạm đến chập chờn.

## 4. Khi phải ghi tay

Mất kết nối lâu, mất điện máy tính: ghi tay **giờ bắt đầu – kết thúc, số trên bộ đếm máy, lỗi, lý do dừng** → sau đó Quản lý **Thêm nhật ký** ở máy
Giám sát để ghi bù. Mẫu: `templates/phieu-ghi-tay-khi-mat-ket-noi.md`.
