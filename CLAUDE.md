# Hướng dẫn cho Claude trong repo này

Repo là kho skill và kiến thức cho công việc tại **Công ty TNHH Bao Bì Minh Phúc**.

- Mọi câu hỏi về Minh Phúc (kỹ thuật, máy, quy trình, KCS, bảo trì, sản xuất, MP MES phía người dùng, kho, kinh doanh, đào tạo…): **tải
  `skills/minhphuc/SKILL.md` trước**, rồi skill chuyên sâu nó chỉ tới. Chỉ tải `references/*.md` qua bảng tham chiếu trong `SKILL.md` của skill đó.
- Thứ bậc nguồn: **[MP]** > **[MP-Web]/[MP-HSNL]** > **[Chuẩn]** > **[KN ngành]**. Không bịa máy, thông số, hãng máy; thiếu thì nói "chưa xác nhận".
- **Ngoài phạm vi**: lập trình PLC/HMI, mã nguồn và cấu hình MP MES, TIA Portal/Openness, địa chỉ mạng, tài khoản, mật khẩu, giá. Không thêm các thứ đó vào repo.
- Tính toán: dùng `tools/tinh-toan` (`cd tools/tinh-toan && python -m mptinh …`), ghi công thức và giả định.
- Biểu mẫu: `templates/`. Dữ liệu: `data/` (mã lỗi `data/ma-loi.csv`).
- Sửa repo: theo `CONTRIBUTING.md`; chạy `python scripts/kiem_tra_repo.py` và test máy tính trước khi commit; cập nhật `CHANGELOG.md`.
- Thông tin mới xác nhận tại xưởng: sửa skill liên quan, đổi nhãn nguồn thành [MP], gạch dòng tương ứng trong `docs/CAN-XAC-NHAN.md`.
- Trả lời bằng tiếng Việt, đúng tên máy và mã lỗi của xưởng; việc chạm vào máy luôn nhắc an toàn (LOTO).
