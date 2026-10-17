# Kiến trúc repo

## 1. Lớp kiến thức

```
                ┌──────────────────────────── skills/minhphuc (router) ────────────────────────────┐
                │ thứ bậc nguồn · phạm vi · định tuyến · cách trả lời                               │
                └───────────────┬───────────────────────┬───────────────────────┬──────────────────┘
   Nền công ty                 Tổ máy                    Chất lượng – hệ thống      Công cụ
   mp-cong-ty                  mp-to-song                mp-kcs-chat-luong          mp-tinh-toan → tools/tinh-toan
   mp-san-pham-ket-cau         mp-in-flexo               mp-xu-ly-su-co             mp-bieu-mau  → templates/
   mp-giay-nguyen-lieu         mp-xuong-offset           mp-fsc-iso-attp            mp-thu-vien  → sources/, thu-vien/
   mp-ho-tro-kinh-doanh        mp-be-dan                 mp-an-toan-lao-dong        mp-dao-tao
   mp-kho-giao-hang            mp-bao-tri                mp-ke-hoach-san-xuat       mp-cai-tien
                                                         mp-mes-su-dung
                ┌───────────────────────────────── data/ ───────────────────────────────────────────┐
                │ ma-loi.csv (127 mã) · may-moc.yaml · song.csv · phep-thu.csv · thuat-ngu.csv · …    │
                └───────────────────────────────────────────────────────────────────────────────────┘
```

## 2. Một skill gồm gì

```
skills/<tên>/
  SKILL.md          frontmatter (name = tên thư mục, description: khi nào dùng) + quy tắc chính + bảng tham chiếu
  references/*.md   kiến thức chi tiết; mỗi dữ kiện ghi nguồn trong ngoặc vuông
```
SKILL.md ngắn (đọc trong 1–2 phút), chỉ đường tới references. Claude chỉ tải reference khi cần — giữ ngữ cảnh gọn.

## 3. Nguồn gốc nội dung

| Nội dung | Từ đâu |
|---|---|
| Công ty, sản phẩm, khách, máy công bố | Cào minhphucpack.com + hồ sơ năng lực 2025 (17/10/2026) |
| Kiến thức nghề (tiêu chuẩn, tra lỗi, khung năng lực) | 9 sổ tay tiếng Việt soạn từ 132 tài liệu công khai (17/10/2026) |
| 127 mã lỗi, 7 nhóm Lỗi khác, 6 nhóm nguyên nhân | File của xưởng (10/2026) — trích bằng script chỉ đọc |
| Luật sản xuất (thời gian, đơn vị, lưu đơn, ghép đơn…) và cách dùng MES | Tài liệu nghiệp vụ và hướng dẫn vận hành MP MES 2.0 (10/2026), chỉ phần người dùng |

## 4. Những thứ cố ý không có

Mã nguồn và cấu hình phần mềm, chương trình PLC/HMI, TIA Portal/Openness; địa chỉ mạng, tài khoản, mật khẩu; giá; tài liệu PDF của bên thứ ba
(bản quyền — tải lại bằng `scripts/tai_thu_vien.py`). `scripts/kiem_tra_repo.py` chặn các mẫu bí mật và từ khoá ngoài phạm vi.

## 5. Kiểm tra tự động

`python scripts/kiem_tra_repo.py` (hoặc `pwsh scripts/validate-repo.ps1`): manifest hợp lệ; mọi skill có frontmatter đúng; router trỏ tới mọi skill;
mọi liên kết tương đối và đường dẫn `templates/…`, `data/…` tồn tại; không lộ địa chỉ IP, mật khẩu, từ khoá ngoài phạm vi; CSV đều cột.
`python -m unittest discover -s tools/tinh-toan/tests` kiểm máy tính.
