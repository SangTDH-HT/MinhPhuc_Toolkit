---
name: mp-giay-nguyen-lieu
description: >
  Giấy và vật tư đầu vào của Minh Phúc: giấy mặt (kraftliner, testliner, mặt trắng), giấy sóng, giấy offset
  (Couche, Ivory, Duplex), chỉ tiêu giấy (định lượng, độ ẩm, SCT, RCT, CMT, bục, Cobb, bền tách lớp) và ý nghĩa với thùng,
  cách đọc COA và bảng thông số, nhận giấy cuộn, lấy mẫu, lưu kho, ổn định ẩm, FIFO, tách lô FSC, nhà cung cấp giấy,
  và vật tư phụ (tinh bột, xút, borax, mực gốc nước, keo dán, keo bồi, màng cán, bản in, khuôn, dây đai).
  Dùng khi nhận hàng, khiếu nại nhà cung cấp, chọn giấy cho đơn, tra lỗi có gốc nguyên liệu (nhóm NVL),
  hoặc lập tiêu chuẩn mua hàng.
---

# mp-giay-nguyen-lieu — phần lớn lỗi thùng bắt đầu từ vật liệu

Nguyên liệu chiếm khoảng **75 % giá thành thùng** [AOPack]. Minh Phúc dùng **≥ 1.200 tấn giấy/tháng**, kho giấy > 1.200 tấn. [MP-HSNL]
Nhà cung cấp giấy (HSNL "đối tác liên kết"): Saigon Paper · Giấy Linh Xuân · Thuận An Paper · TKC Kraft · KOA · LM · Đồng Tiến.

## Việc thường gặp

| Việc | Đọc |
|---|---|
| Hiểu một chỉ tiêu giấy, đọc COA, so bảng thông số | [references/giay-cuon-chi-tieu.md](references/giay-cuon-chi-tieu.md) |
| Nhận giấy cuộn, lấy mẫu, lưu kho, cuộn ướt/méo, FIFO, tách lô FSC | [references/nhan-giay-va-luu-kho.md](references/nhan-giay-va-luu-kho.md) |
| Tinh bột – xút – borax, mực, keo dán, keo bồi, màng, bản, khuôn, dây đai | [references/vat-tu-phu.md](references/vat-tu-phu.md) |
| Biểu mẫu kiểm giấy nhập | `templates/phieu-kiem-tra-giay-cuon.md` |
| Lỗi có gốc nguyên liệu tại máy | mã TS-01…05 (tổ sóng), OF-01…02 (offset) — skill `mp-xu-ly-su-co` |

## Ba câu hỏi khi nghi lỗi do giấy

1. **Đổi cuộn / lô khác là hết lỗi?** → nghiêng về nhóm **NVL** (ô 1 trong 6 nhóm nguyên nhân).
2. **Số đo lệch COA?** Đo lại định lượng, độ ẩm, RCT/SCT, Cobb trên mẫu của chính cuộn đó; ghi số lô.
3. **Hai cuộn giấy mặt lệch ẩm?** Đây là nguyên nhân hàng đầu gây **cong tấm** — đo ẩm cả hai cuộn trước khi đổ lỗi máy.

## Nguyên tắc

- Ghi kết quả kiểm theo **số lô / số cuộn** để truy được khi tấm lỗi (nối với số phiếu sản xuất trên MP MES).
- Bảng thông số trong repo là của giấy châu Âu/Nga — **để hiểu cách đọc**; giấy Việt Nam (đa số testliner, giấy sóng tái chế)
  có số thấp hơn. Cần gom COA thật của từng nhà cung cấp đang giao (việc mở, `docs/LO-TRINH.md`).
- Đơn FSC chỉ dùng giấy có **khai báo FSC trên hoá đơn** và phải tách lô trong kho (skill `mp-fsc-iso-attp`).
- Giấy cho hộp tiếp xúc thực phẩm: cần xác nhận tuân thủ (FDA/BfR hoặc tương đương) từ nhà cung cấp.
