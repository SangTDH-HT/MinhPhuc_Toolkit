# Nhật ký thay đổi

## 1.1.0 — 18/10/2026

- Sửa đơn vị đếm theo quy ước MP MES mới nhất: máy in đo bằng tờ in (không nhân số con), chỉ máy bế nhân số con; tổ sóng ghi số dao,
  số tấm = số dao × số tấm/khổ là "Sóng vào" của máy in; quy ước đối chiếu tấm sóng = tờ in = nhịp bế.
- `mp-mes-su-dung`: thêm hướng dẫn Trợ lý trong MES và mục gộp phiếu giống hệt ở máy in.
- Trang trí repo: banner mặt cắt tấm 5 lớp sóng BC (`assets/banner.svg`, vẽ bằng `scripts/ve_banner.py`), README mới có bản đồ skill theo dây chuyền,
  huy hiệu, mẫu issue và PR, CODEOWNERS; workflow kiểm tra tự động soạn sẵn ở `.github/cho-bat/` (bật khi tài khoản đẩy có quyền workflow).
- `scripts/kiem_tra_repo.py`: kiểm thêm huy hiệu phiên bản README khớp `plugin.json`.

## 1.0.0 — 17/10/2026

Bản đầu tiên.

- 22 skill: `minhphuc` (định tuyến) + 21 skill chuyên sâu (công ty, sản phẩm – kết cấu, giấy, tổ sóng, in flexo, xưởng offset, bế – dán, KCS,
  xử lý sự cố, bảo trì, kế hoạch – hệ thống sản xuất, MP MES phía người dùng, an toàn lao động, FSC – ISO – ATTP, kho – giao hàng, hỗ trợ kinh doanh,
  tính toán, biểu mẫu, đào tạo, cải tiến, thư viện).
- Nguồn: web minhphucpack.com + hồ sơ năng lực 2025 (cào 17/10/2026); 9 sổ tay soạn từ 132 tài liệu chuyên môn công khai; file mổ xẻ 127 mã lỗi
  "Lỗi khác" của xưởng; tài liệu nghiệp vụ và hướng dẫn vận hành MP MES 2.0 (phần người dùng).
- `data/`: 127 mã lỗi, 7 nhóm Lỗi khác, 6 nhóm nguyên nhân, ô lỗi MES, máy móc, sóng, phép thử, thuật ngữ Việt – Anh – Trung, 45 mẫu sản phẩm,
  khách hàng, nhà cung cấp.
- `tools/tinh-toan`: máy tính `mptinh` (13 lệnh, 21 test).
- `templates/`: 18 biểu mẫu.
- `scripts/`: kiểm tra repo (manifest, frontmatter, router, liên kết, bí mật, phạm vi, CSV), xuất PDF, tải lại thư viện.
- `docs/`: kiến trúc, hướng dẫn sử dụng, danh sách cần xác nhận, lộ trình.
