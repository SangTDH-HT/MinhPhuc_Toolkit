# Hướng dẫn dùng MinhPhuc Toolkit với Claude

## 1. Cài

**Cách A — cài như plugin Claude Code (dùng ở mọi thư mục):**

```
/plugin marketplace add SangTDH-HT/MinhPhuc_Toolkit
/plugin install minhphuc-toolkit@minhphuc-toolkit
```
Repo riêng tư: máy cần đăng nhập GitHub có quyền đọc repo (`gh auth login`). Hoặc dùng bản trên máy: `/plugin marketplace add C:\MinhPhuc_Toolkit`.
Cập nhật: `/plugin marketplace update minhphuc-toolkit`.

**Cách B — mở thẳng thư mục repo** trong Claude Code (VS Code hoặc terminal): `CLAUDE.md` tự hướng Claude tới skill `minhphuc`.

## 2. Hỏi thế nào cho được việc

Nói rõ **máy**, **mã hàng / số phiếu**, **hiện tượng**, **số đo** (nếu có). Ví dụ theo vai:

| Vai | Câu hỏi mẫu |
|---|---|
| Thợ tổ sóng | "Tấm 5 lớp BC đang cong lên ở đầu ra, cuộn mặt mới thay, xử lý sao?" |
| Thợ in | "Máy In 2 in nền đỏ bị sọc ngang và nhạt dần, mực đỏ độ nhớt 28 giây." |
| Thợ bế | "Máy bế 2 rác lỗ tay cầm không rơi, khuôn mới về." |
| Thợ dán | "Máy dán 1 khe dán lúc 4 lúc 10 mm, đơn thùng 5 lớp." |
| Tổ trưởng | "Hôm qua Máy In 1 tốc độ bình quân thấp, ngừng không kế hoạch 95 phút — đọc số sao, nên làm gì?" |
| KCS | "Lô 12.000 thùng, kiểm xuất AQL thế nào? Lập phiếu kiểm xuất cho mã hàng X." |
| KCS | "Khách báo thùng bẹp ở kho lạnh sau 3 tuần — làm 8D." |
| Bảo trì | "Lập lịch bảo trì phòng ngừa cho máy dán tự động 1." |
| Kế hoạch | "Đơn 520 mm rộng, khổ 1.600 và 1.800 cái nào hao biên ít hơn?" |
| Kinh doanh | "Khách cần thùng đựng 12 chai 1,5 L, xếp 6 tầng, kho mát — tư vấn kết cấu và cần báo giá gì." |
| Quản lý | "Tóm tắt 6 nhóm nguyên nhân Lỗi khác và đề xuất 3 dự án cải tiến quý tới." |
| Người mới | "Em mới vào tổ in, tuần đầu cần học gì?" |

## 3. Claude sẽ làm gì

- Tải skill `minhphuc` → chọn skill chuyên sâu → trả lời bằng ngôn ngữ xưởng, gắn nguồn ([MP], [MP-Web], [Chuẩn], [KN ngành]).
- Tính toán bằng `tools/tinh-toan` (ghi công thức, giả định).
- Lập biểu mẫu từ `templates/` (điền sẵn phần biết được).
- Nói rõ khi thông tin **chưa xác nhận** và cách lấy.

## 4. Giới hạn

- Không có: lập trình PLC/HMI, mã nguồn và cấu hình MP MES, tài khoản, mật khẩu, địa chỉ mạng, giá bán/giá mua.
- Thông số **[KN ngành]** là điểm xuất phát — kiểm trên máy thật trước khi đưa vào quy trình.
- Tài liệu gốc (PDF tiêu chuẩn, sổ tay hãng) không nằm trong repo — xem skill `mp-thu-vien`.

## 5. Góp kiến thức

Thấy sai hoặc có số liệu thật của xưởng: sửa skill theo `CONTRIBUTING.md`, hoặc nhờ Claude "cập nhật skill mp-to-song: bảng chuẩn keo tổ sóng là …".
