# MinhPhuc Toolkit

Bộ skill và kho kiến thức cho **Claude** phục vụ công việc tại **Công ty TNHH Bao Bì Minh Phúc** (thùng carton sóng 3–5 lớp, hộp in offset bồi sóng):
kỹ thuật, máy móc, quy trình, KCS – chất lượng, giấy và vật tư, xử lý sự cố, bảo trì, an toàn, FSC – ISO 9001 – an toàn thực phẩm, kế hoạch và hệ thống
sản xuất, **MP MES ở phía người dùng**, kho – giao hàng, hỗ trợ kinh doanh, đào tạo, cải tiến.

Nền tảng là **Minh Phúc thật**: máy Minh Phúc có, sản phẩm Minh Phúc làm, mã lỗi và luật sản xuất xưởng đã chốt. Kiến thức ngành (FEFCO, ISO, TAPPI,
NZQA, Sun Chemical…) bổ sung và luôn ghi nguồn.

Biên soạn: Nguyễn Hữu Sáng · bản 1.0 · 17/10/2026 · repo nội bộ (riêng tư).

## Cài và dùng

```
/plugin marketplace add SangTDH-HT/MinhPhuc_Toolkit
/plugin install minhphuc-toolkit@minhphuc-toolkit
```
hoặc mở thẳng thư mục repo trong Claude Code. Chi tiết, câu hỏi mẫu theo vai: [docs/HUONG-DAN-SU-DUNG.md](docs/HUONG-DAN-SU-DUNG.md).

## 22 skill

| Skill | Dùng khi |
|---|---|
| [minhphuc](skills/minhphuc/SKILL.md) | **Cửa vào mọi việc** — định tuyến, thứ bậc nguồn, cách trả lời |
| [mp-cong-ty](skills/mp-cong-ty/SKILL.md) | Công ty, hai xưởng, 13 máy công bố + 9 máy trên MES, khách hàng, định hướng |
| [mp-san-pham-ket-cau](skills/mp-san-pham-ket-cau/SKILL.md) | Tấm, sóng, FEFCO, kích thước, phôi, chọn kết cấu, 45 mẫu |
| [mp-giay-nguyen-lieu](skills/mp-giay-nguyen-lieu/SKILL.md) | Giấy cuộn, chỉ tiêu, nhận giấy, kho, vật tư phụ |
| [mp-to-song](skills/mp-to-song/SKILL.md) | Tổ sóng 4 trạm, keo – hơi, cong tấm, 26 mã TS, ghép đơn |
| [mp-in-flexo](skills/mp-in-flexo/SKILL.md) | Máy In 1, 2: mực, anilox, bản, 24 mã FX, in 2 mặt |
| [mp-xuong-offset](skills/mp-xuong-offset/SKILL.md) | Offset Mitsubishi, bồi YB-1300E, cán màng, xén 115SC, mã OF/BO |
| [mp-be-dan](skills/mp-be-dan/SKILL.md) | Bế, khuôn, máy dán, phiếu pallet, mã BE/DA |
| [mp-kcs-chat-luong](skills/mp-kcs-chat-luong/SKILL.md) | Phép thử, AQL, dung sai FEFCO, kế hoạch kiểm, số QC → chỉnh máy |
| [mp-xu-ly-su-co](skills/mp-xu-ly-su-co/SKILL.md) | 127 mã lỗi, "Lỗi khác" 7 nguồn, 6 nhóm nguyên nhân, 5 Why, 8D |
| [mp-bao-tri](skills/mp-bao-tri/SKILL.md) | Bảo trì phòng ngừa theo máy, bôi trơn, máy hỏng, sổ máy |
| [mp-ke-hoach-san-xuat](skills/mp-ke-hoach-san-xuat/SKILL.md) | Dòng chảy đơn, 6 loại thời gian, đơn vị đếm, OEE Minh Phúc |
| [mp-mes-su-dung](skills/mp-mes-su-dung/SKILL.md) | Thao tác MP MES 2.0, cảnh báo, máy Giám sát, vai – quyền |
| [mp-an-toan-lao-dong](skills/mp-an-toan-lao-dong/SKILL.md) | Mối nguy theo máy, LOTO, hoá chất, PCCC |
| [mp-fsc-iso-attp](skills/mp-fsc-iso-attp/SKILL.md) | FSC CoC, ISO 9001 ở xưởng, hộp tiếp xúc thực phẩm |
| [mp-kho-giao-hang](skills/mp-kho-giao-hang/SKILL.md) | Pallet ISO 3394, CBM – container, bảo quản, giao hàng |
| [mp-ho-tro-kinh-doanh](skills/mp-ho-tro-kinh-doanh/SKILL.md) | Tư vấn khách, báo giá kỹ thuật, mẫu, chuyển đơn mới |
| [mp-tinh-toan](skills/mp-tinh-toan/SKILL.md) | Máy tính: BCT, McKee, ECT, định lượng, phôi, CBM, pallet, AQL, OEE |
| [mp-bieu-mau](skills/mp-bieu-mau/SKILL.md) | 18 biểu mẫu in được |
| [mp-dao-tao](skills/mp-dao-tao/SKILL.md) | Lộ trình, khung NZQA, ma trận kỹ năng, câu hỏi kiểm tra |
| [mp-cai-tien](skills/mp-cai-tien/SKILL.md) | A3, Pareto, SMED, 14 dự án ưu tiên |
| [mp-thu-vien](skills/mp-thu-vien/SKILL.md) | Thư viện tài liệu gốc, độ tin nguồn, thêm tài liệu |

## Cấu trúc

```
.claude-plugin/   plugin.json, marketplace.json
skills/           22 skill (SKILL.md + references/)
data/             ma-loi.csv (127 mã), may-moc.yaml, song.csv, phep-thu.csv, thuat-ngu.csv, mau-san-pham.json, …
templates/        18 biểu mẫu Markdown
tools/tinh-toan/  máy tính kỹ thuật Python (python -m mptinh), có test
scripts/          kiem_tra_repo.py, validate-repo.ps1, xuat_pdf.py, tai_thu_vien.py
sources/          nguon.tsv, trang-web.tsv, danh-muc-thu-vien.md
docs/             KIEN-TRUC, HUONG-DAN-SU-DUNG, CAN-XAC-NHAN, LO-TRINH
```

## Kiểm tra

```
python scripts/kiem_tra_repo.py                       # manifest, frontmatter, router, liên kết, bí mật, phạm vi, CSV
python -m unittest discover -s tools/tinh-toan/tests  # máy tính
```

## Phạm vi và bảo mật

- **Không có**: lập trình PLC/HMI, mã nguồn – cấu hình MP MES, TIA Portal; địa chỉ mạng, tài khoản, mật khẩu; giá.
- Tài liệu PDF của bên thứ ba **không** đưa lên git (bản quyền) — tải lại bằng `scripts/tai_thu_vien.py`; danh mục ở `sources/`.
- Thông số **[KN ngành]** là điểm xuất phát, phải kiểm tại xưởng. Việc cần xác nhận: [docs/CAN-XAC-NHAN.md](docs/CAN-XAC-NHAN.md).
- Lộ trình làm repo mạnh hơn: [docs/LO-TRINH.md](docs/LO-TRINH.md). Góp nội dung: [CONTRIBUTING.md](CONTRIBUTING.md).
