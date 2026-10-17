# Hướng dẫn cho agent

Kho skill nội bộ của Bao Bì Minh Phúc (`minhphuc-toolkit`).

- Bắt đầu mọi việc ở `skills/minhphuc/SKILL.md` (định tuyến tới 21 skill chuyên sâu).
- Chỉ tải `references/*.md` của một skill qua bảng trong `SKILL.md` của chính skill đó.
- Ngoài phạm vi: lập trình PLC/HMI, mã nguồn – cấu hình MP MES, TIA Portal/Openness, địa chỉ mạng, tài khoản, mật khẩu, giá.
- Sau khi thêm/đổi tên skill hoặc sửa nội dung: `python scripts/kiem_tra_repo.py` và `python -m unittest discover -s tools/tinh-toan/tests`.
- Quy tắc viết: `CONTRIBUTING.md`.
