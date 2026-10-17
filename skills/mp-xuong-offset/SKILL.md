---
name: mp-xuong-offset
description: >
  Xưởng offset của Minh Phúc (2.000 m², từ 8/2022): máy xén 115SC, máy in offset 5 màu Mitsubishi (Máy In Offset trên MES),
  gia công bề mặt (cán màng OPP/PE, UV, varnish/OPV, ép kim, dập nổi, metalize), máy bồi YB-1300E (bồi tờ in lên tấm sóng E),
  bế phẳng và dán hộp. Gồm thông số vận hành offset (nhiệt lô, máng nước, pH giấy, cân bằng mực – nước, thời gian khô),
  21 lỗi in offset tra theo Sun Chemical, 18 mã lỗi OF-01…OF-18 và 14 mã BO-01…BO-14 của xưởng, lỗi bồi (cong, phồng, ván giặt,
  lệch), lỗi cán màng, an toàn máy xén, bản kẽm (mã BK). Dùng khi chạy hoặc xử lý sự cố ở xưởng offset, làm hộp cao cấp, hộp quà.
---

# mp-xuong-offset — hộp cao cấp: màu chuẩn, bồi phẳng, mặt đẹp

Hồ sơ năng lực ghi "sản phẩm offset đang dần nâng cao chất lượng" — đây là mảng Minh Phúc đang đầu tư (hộp quà, hộp thương hiệu, hộp xuất khẩu).

## Dòng chảy

```
Giấy tờ rời (Couche / Ivory / Duplex) → XÉN 115SC → IN OFFSET 5 màu Mitsubishi → gia công bề mặt (cán màng, UV, ép kim, dập nổi…)
   → BỒI lên tấm sóng (thường sóng E) → BẾ phẳng → DÁN → KCS → giao
```
Một tờ in chứa nhiều hộp, bế rồi dán thành hộp (mẫu MP-046). Mặt tấm sóng gợn nên **không in offset trực tiếp lên tấm sóng đẹp được** —
phải in tờ rời rồi bồi. [MP-Web]

## Việc thường gặp

| Việc | Đọc |
|---|---|
| Máy trong xưởng, đếm trên MES, bản kẽm, máy xén | [references/quy-trinh-va-may.md](references/quy-trinh-va-may.md) |
| Chạy máy in offset, thông số, tra 21 lỗi, mã OF-xx | [references/in-offset.md](references/in-offset.md) |
| Bồi sóng, cán màng, mã BO-xx | [references/boi-va-can-mang.md](references/boi-va-can-mang.md) |
| Bế phẳng, dán hộp offset | skill `mp-be-dan` |

## Năm điều quyết định chất lượng hộp offset

1. **Ủ giấy** trong xưởng trước khi in (cong, co giãn — OF-01, OF-02); giữ ẩm xưởng ổn định.
2. **Cân bằng mực – nước** ở mức tối thiểu; lô chà 22–26 °C, máng nước ~18 °C. [Sun Chemical]
3. **So tờ đầu với tờ duyệt màu**; đo mật độ màu định kỳ (OF-07, OF-08).
4. **Chờ mực khô đủ** (oxy hoá 24–48 giờ) trước khi cán màng, bồi; chồng tờ thấp, phun bột chống dính đúng (OF-09).
5. **Bồi**: cân ẩm tờ in và tấm sóng, keo đều, canh mép tờ đầu, ép chồng khi còn ẩm (BO-03…BO-09).

## Ghi lỗi đúng ô MES

- Máy In Offset: **Sóng · Thử máy · In lệch · Nhảy dao · Khác** — tờ thử, canh màu → Thử máy (OF-18).
- Máy bồi: **Sóng · In · Bế · Định hình · Khác** — tấm sóng lỗi → Sóng (BO-01), tờ in lỗi → In (BO-02); tấm canh máy là hao hụt (BO-14).
- Lỗi khác ghi **mã OF-xx / BO-xx** trong ghi chú.
