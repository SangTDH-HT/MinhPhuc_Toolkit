---
name: mp-san-pham-ket-cau
description: >
  Sản phẩm và kết cấu thùng, hộp carton của Minh Phúc: tấm 3 lớp / 5 lớp, loại sóng A B C E và sóng đôi
  BC BE BA, giấy mặt – giấy sóng, mã kiểu hộp FEFCO (0201 nắp gài, 0200, 0203, nhóm 03 nắp rời – âm dương,
  nhóm 04 hộp gấp – khay, nhóm 09 vách ngăn), ký hiệu bản vẽ dieline, quy ước kích thước lọt lòng – phủ bì,
  khoảng cách lằn, tính phôi, mối nối, hướng sóng, chọn kết cấu theo tải và môi trường, 45 mẫu đã sản xuất.
  Dùng khi đọc hoặc lập quy cách đơn hàng, tư vấn khách chọn thùng, kiểm bản vẽ kết cấu, tính kích thước phôi,
  hay giải thích vì sao thùng yếu do chọn sai kết cấu.
---

# mp-san-pham-ket-cau — đọc quy cách như đọc bản vẽ

Người kỹ thuật phải nói được ngay: tấm gì, sóng gì, kiểu hộp mã mấy, kích thước đo thế nào, hướng sóng ra sao,
mối nối kiểu gì — và kết cấu đó có chịu nổi tải của khách không.

## Việc thường gặp → làm thế nào

| Việc | Cách làm | Đọc |
|---|---|---|
| Đọc một quy cách đơn hàng | Kiểm theo danh sách 8 mục bên dưới | [references/kich-thuoc-phoi-va-ban-ve.md](references/kich-thuoc-phoi-va-ban-ve.md) |
| Khách hỏi "nên dùng thùng gì" | Hỏi đủ 6 thông tin → chọn sơ bộ theo ngành → ước BCT → làm mẫu → đo | [references/chon-ket-cau.md](references/chon-ket-cau.md) |
| Phân biệt sóng, đổi sóng | Bảng sóng: chiều cao, bước, độ dày, hệ số co | [references/tam-carton-va-song.md](references/tam-carton-va-song.md) |
| Gọi tên kiểu hộp, đọc mã FEFCO | Bảng nhóm mã + ký hiệu dieline | [references/kieu-hop-fefco.md](references/kieu-hop-fefco.md) |
| Tính khoảng cách lằn, kích thước phôi, diện tích, khối lượng thùng | Công thức + máy tính `tools/tinh-toan` (`phoi-rsc`, `dinh-luong`) | [references/kich-thuoc-phoi-va-ban-ve.md](references/kich-thuoc-phoi-va-ban-ve.md), skill `mp-tinh-toan` |
| Tra sản phẩm Minh Phúc đã làm | 45 mẫu MP-001 … MP-046 | [references/san-pham-minh-phuc.md](references/san-pham-minh-phuc.md), `data/mau-san-pham.json` |

## Danh sách kiểm một quy cách (8 mục)

1. **Kiểu hộp** — mã FEFCO (0201, 0200, 0203, 03xx, 04xx, 09xx) hoặc bản vẽ riêng.
2. **Kích thước lọt lòng** D × R × C (mm), D là cạnh dài miệng thùng; hộp nắp rời ghi thêm cao nắp (…/40).
3. **Số lớp và sóng** — 3 lớp (B, C, E, A) hay 5 lớp (BC, BE, BA). Minh Phúc **không làm 7 lớp**.
4. **Giấy từng lớp** — định lượng và loại cho Mặt / Sóng / (Giữa) / Sóng / Đáy (kế hoạch tổ sóng ghi theo các cột
   Mặt · B · Giữa · E · A · C · Đáy).
5. **Hướng sóng** — mặc định song song khe xẻ (sóng đứng khi dựng thùng); giấy tấm phải ghi rõ.
6. **Mối nối** — dán keo (phổ biến), ghim (thùng lớn), băng; tai dán ≥ 30 mm.
7. **In** — số màu, mặt in, vị trí, mẫu duyệt; offset thì giấy mặt + gia công bề mặt.
8. **Yêu cầu bền / môi trường** — tải xếp chồng (số tầng × kg), kho lạnh (Cobb), thời gian lưu kho, xuất khẩu.

Thiếu mục nào thì hỏi lại kinh doanh/kế hoạch trước khi chạy — đơn sai kết cấu là lỗi nhóm
"Kỹ thuật – kế hoạch" (skill `mp-xu-ly-su-co`).

## Nguyên tắc

- Công thức (McKee, IS 2771, hệ số an toàn) chỉ để **định hướng**; con số chốt là **đo trên mẫu thật** ở phòng QC.
- Độ dày tấm không xác định loại sóng — phải xét **bước sóng** (đếm sóng trên 30 cm hoặc đo bước).
- Đừng hứa với khách thứ Minh Phúc không làm: 7 lớp, túi ESD, túi chắn ẩm, gói hút ẩm.
- Bảng bù kích thước theo sóng mà phòng thiết kế Minh Phúc đang dùng **chưa có trong repo** — số trong
  `kich-thuoc-phoi-va-ban-ve.md` là chuẩn FEFCO và kinh nghiệm ngành; khi có bảng nội bộ thì bảng nội bộ thắng.
