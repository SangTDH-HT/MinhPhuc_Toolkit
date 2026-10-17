# Góp nội dung cho MinhPhuc Toolkit

## 1. Thứ bậc nguồn — gắn nhãn cho mọi dữ kiện

| Nhãn | Nghĩa | Ví dụ |
|---|---|---|
| **[MP]** | Đã xác nhận tại xưởng (anh Sáng, tổ trưởng, KCS) hoặc luật/dữ liệu MP MES đã chốt | "Lưu đơn = đơn xong (chốt 27/08/2026)" |
| **[MP-MES]** | Lấy từ tài liệu nghiệp vụ / hướng dẫn MP MES (phía người dùng) | Đơn vị đếm từng máy |
| **[MP-Web] / [MP-HSNL]** | Công ty công bố (web, hồ sơ năng lực, chứng nhận) | "Máy bồi YB-1300E ≥ 56.000 sp/8 giờ" |
| **[Chuẩn: tên]** | Tiêu chuẩn / tài liệu nghề có tên, ghi rõ tên (và trang nếu được) | [Chuẩn: FEFCO QC], [NZQA 40351] |
| **[KN ngành]** | Kinh nghiệm chung của nghề, chưa kiểm tại Minh Phúc | Hệ số co sóng gần đúng |
| **[Suy luận]** | Rút ra từ dữ liệu, không ai công bố | Định hướng phát triển |

Cao thắng thấp. Hai nguồn vênh: ghi cả hai và thêm một dòng vào `docs/CAN-XAC-NHAN.md`.

## 2. Phạm vi

**Có**: mọi việc kỹ thuật, sản xuất, chất lượng, an toàn, kho, kinh doanh kỹ thuật, đào tạo, cải tiến của Minh Phúc; MP MES ở mức **người dùng**
(thao tác, ý nghĩa con số, luật nghiệp vụ, cảnh báo).
**Không**: lập trình PLC/HMI, mã nguồn – cơ sở dữ liệu – cấu hình MP MES, TIA Portal/Openness; địa chỉ mạng, tài khoản, mật khẩu, mã PIN;
giá mua – bán; số điện thoại cá nhân; dữ liệu khách chưa công khai; PDF của bên thứ ba. `scripts/kiem_tra_repo.py` sẽ chặn phần lớn các thứ này.

## 3. Viết một skill

```
skills/<ten-skill>/            tên chữ thường, gạch nối, không dấu, tiền tố mp-
  SKILL.md                     frontmatter + quy tắc chính + bảng tham chiếu (ngắn, đọc 1–2 phút)
  references/<chu-de>.md       kiến thức chi tiết
```
Frontmatter:
```yaml
---
name: mp-ten-skill          # trùng tên thư mục
description: >
  Nói rõ skill chứa gì (từ khoá máy, lỗi, tiêu chuẩn) và DÙNG KHI NÀO — Claude chọn skill dựa vào đoạn này.
---
```
- Mọi file trong `references/` phải được `SKILL.md` nhắc tới (bảng tham chiếu) — không để file mồ côi.
- Thêm skill mới vào bảng định tuyến của `skills/minhphuc/SKILL.md` và bảng trong `README.md`.
- Liên kết nội bộ dùng đường dẫn tương đối; đường dẫn trong dấu `…` bắt đầu bằng `templates/`, `data/`, `docs/`… phải tồn tại.

## 4. Văn phong

- Tiếng Việt của xưởng: đúng tên máy (Máy In 1, Máy bế tự động 2, tổ sóng, trạm ghép…), đúng mã lỗi (TS-12, FX-04…), đúng ô MES.
- Bảng cho thứ tra cứu; câu ngắn cho thứ làm theo. Số có đơn vị; kiểu số Việt Nam (1.234,5).
- Viết cho người đứng máy làm theo được ngay; "vì sao" cho tổ trưởng; "số nào, ai chịu" cho quản lý.
- Việc chạm vào máy: nhắc dừng máy đúng cách / LOTO.
- Tên người: chỉ tên công khai; còn lại dùng vai trò.

## 5. Dữ liệu và công cụ

- `data/*.csv`: UTF-8, có dấu ngoặc kép, đều cột. `data/ma-loi.csv` là nguồn mã lỗi — cập nhật từ file của xưởng (mở file Excel gốc **chỉ đọc**).
- Công thức mới: thêm vào `tools/tinh-toan/mptinh/` có docstring ghi nguồn + test với ví dụ kiểm được.
- Biểu mẫu mới: `templates/`, thêm dòng vào bảng của `skills/mp-bieu-mau/SKILL.md`.

## 6. Trước khi commit

```
python scripts/kiem_tra_repo.py
python -m unittest discover -s tools/tinh-toan/tests
```
Cập nhật `CHANGELOG.md`; tăng `version` trong `.claude-plugin/plugin.json` (và huy hiệu phiên bản trong README) khi phát hành bản mới.

Kiểm tra tự động trên GitHub: workflow soạn sẵn ở `.github/cho-bat/kiem-tra.yml`. Muốn bật thì cấp quyền workflow cho tài khoản đẩy
(`gh auth refresh -h github.com -s workflow`), chuyển file vào thư mục `.github/workflows` rồi đẩy lên.
