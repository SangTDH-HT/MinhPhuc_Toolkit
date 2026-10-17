# Pallet, container, xe tải

## 1. Module pallet ISO 3394 [MP-Web]

ISO 3394 quy định kích thước mặt bằng kiện hàng hình hộp sao cho xếp khít các cỡ pallet chuẩn (ISO 3676). Chọn **kích thước phủ bì D × R** của thùng
bằng module hoặc **ước số** của module (chia cạnh cho 2, 3, 4…).

| Pallet (mm) · module | Thùng phủ bì (mm) | Thùng/lớp |
|---|---|---|
| **1200 × 800** (pallet châu Âu) · 600 × 400 | 600 × 400 | 4 |
| | 400 × 300 | 8 |
| | 300 × 200 | 16 |
| **1200 × 1000** · 600 × 500 | 600 × 500 | 4 |
| | 500 × 400 | 6 |
| | 300 × 250 | 16 |
| **1100 × 1100** (pallet vuông, phổ biến châu Á) · 550 × 366 | 550 × 366 | 6 |
| | 550 × 275 | 8 |
| | 366 × 275 | 12 |

Bốn bước: (1) hỏi khách đầu bên kia dùng pallet nào; (2) chọn module; (3) chỉnh kích thước sản phẩm/lót để phủ bì rơi vào module; (4) kiểm chiều cao xếp
theo BCT và chiều cao container/kho.

Thiết kế thùng theo sản phẩm rồi mới xếp pallet → mỗi lớp thừa vài cm, hàng xô trong container, cước tính trên khoảng trống.

**Xếp thẳng cột hay so le?** Thẳng cột giữ trọn BCT (góc thùng chồng lên góc thùng); so le (interlock) giữ kiện chắc hơn khi vận chuyển nhưng **giảm BCT**
— thường xếp thẳng cột và quấn màng / nẹp góc để giữ ổn định. [MP-Web; KN ngành]
Thùng chìa ra ngoài mép pallet (overhang) làm mất BCT đáng kể **[KN ngành: 20–30 %]**.
Máy tính: `python -m mptinh pallet --dai 400 --rong 300 --pallet 1200x800`.

## 2. CBM và container [MP-Web]

```
CBM một thùng (m³) = D × R × C (mét) = D × R × C (cm) ÷ 1.000.000
Số thùng ước tính  = thể tích container × hệ số khai thác ÷ CBM một thùng GIAO
```

| Container | Thể tích lòng trong (tham khảo) | Khai thác ~85 % |
|---|---|---|
| 20′ | ~33 m³ (Maersk 33,2) | ~28 m³ |
| 40′ | ~67 m³ (Maersk 67,7) | ~57 m³ |
| 40′ High Cube | ~76 m³ (Maersk 76,4) | ~65 m³ |

- Hệ số 85 % là mức tham khảo; hàng cồng kềnh, kích thước lẻ, kê pallet cao có thể chỉ 75–80 %; xếp khít kích thước "đẹp" có thể > 85 %.
  Cách chắc nhất: **xếp thử một lớp rồi nhân lên**.
- Ví dụ thùng 40 × 30 × 30 cm = 0,036 m³ → 20′ ≈ 779 · 40′ ≈ 1.581 · 40HC ≈ 1.794 thùng (công cụ web, hệ số 85 %).
- **Thùng giao** thường xếp phẳng (chưa dựng) → CBM nhỏ hơn rất nhiều; tính theo thùng đã dựng là trả thừa cước.
- Tải trọng: container và xe đều có giới hạn khối lượng — hàng nặng có thể chạm giới hạn kg trước khi đầy thể tích.

Máy tính: `python -m mptinh cbm --dai 40 --rong 30 --cao 30`.

## 3. Hàng xuất khẩu [MP-Web]

| Loại hàng | Số lớp | Sóng |
|---|---|---|
| Hàng phổ biến, xếp chồng trong container | 5 lớp | BC |
| Hàng nặng, cồng kềnh, dễ vỡ | 5 lớp định lượng cao | BC / BA |
| Hàng nhẹ (tính kỹ độ bền) | 3 lớp định lượng cao | — |

- Thống nhất **BCT mục tiêu** với khách (khối lượng, số lớp xếp, thời gian lưu kho); **Cobb thấp** cho đường biển ẩm.
- **Ký hiệu vận chuyển ISO 780**: chiều đặt (This way up), dễ vỡ, tránh mưa/ẩm, giới hạn xếp chồng; thêm thông tin lô, mã hàng, nước sản xuất.
- **ISPM-15** (xử lý nhiệt/hun trùng + dấu IPPC) **chỉ áp dụng cho bao bì gỗ nguyên khối** (pallet gỗ, kiện gỗ) — thùng carton được miễn; pallet gỗ kê hàng mới cần.
- Hồ sơ: FSC CoC, ISO 9001, kết quả đo theo lô.
