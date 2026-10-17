---
name: mp-kho-giao-hang
description: >
  Kho thành phẩm, đóng kiện và giao hàng ở Minh Phúc: phiếu nhận dạng pallet SX-QT01-BM02/06, xếp pallet theo module ISO 3394 (600×400, 600×500, 550×366)
  cho pallet 1200×800, 1200×1000, 1100×1100, xếp thẳng cột hay so le, CBM, số thùng trong container 20'/40'/40HC (hệ số khai thác 85 %) và xe tải,
  bảo quản chống ẩm (kê pallet cách sàn, cách tường, FIFO, tránh nắng), hàng xuất khẩu (5 lớp BC, Cobb thấp, ký hiệu ISO 780, ISPM-15 chỉ cho gỗ),
  lỗi kho – vận chuyển (CH-01…CH-03, CH-05), vùng giao hàng. Dùng khi xếp kho, đóng hàng, tính xe/container, xử lý hàng hư khi vận chuyển, tư vấn khách bảo quản.
---

# mp-kho-giao-hang — hàng ra khỏi máy còn tốt thì phải tới tay khách còn tốt

Phòng Kế hoạch quản **kho vật tư & thành phẩm** và **kho giấy** [MP-HSNL]. Thùng giao **gấp phẳng, buộc kiện trên pallet** (mẫu MP-045) [MP-Web].
Vùng giao: TP.HCM, Thủ Đức, Bình Dương, Dĩ An, Đồng Nai, Long An, Tây Ninh; phần lớn KCN trong bán kính 20 km.

## Bảng tham chiếu

| Cần gì | Đọc |
|---|---|
| Pallet, module ISO 3394, số thùng mỗi lớp, CBM, container, xe tải, hàng xuất khẩu | [references/pallet-va-container.md](references/pallet-va-container.md) |
| Bảo quản kho, chống ẩm, FIFO, phiếu nhận dạng, kiểm trước khi giao, hàng hư do kho – vận chuyển | [references/bao-quan-va-giao-hang.md](references/bao-quan-va-giao-hang.md) |
| Tính nhanh | `python -m mptinh cbm`, `python -m mptinh pallet` (skill `mp-tinh-toan`) |

## Bốn điều quyết định

1. **Phiếu nhận dạng đúng** cho từng pallet (máy dán in N−1 tờ, tờ cuối in sau khi Lưu đơn) — chống lẫn đơn (CH-05), thiếu hàng (CH-03).
2. **Kê pallet cách sàn 100–150 mm, cách tường 200–300 mm**, tránh nắng mưa, **FIFO** — ẩm là kẻ thù số một (CH-02).
3. **Giới hạn chiều cao chồng** theo BCT của thùng; quấn màng pallet — chống móp, ngã (CH-01).
4. **CBM tính theo thùng ở trạng thái giao** (xếp phẳng), không theo thùng đã dựng.
