---
name: mp-to-song
description: >
  Tổ sóng (dây chuyền tạo sóng, corrugator, 瓦楞纸板生产线) của Minh Phúc: 4 trạm (trạm sóng A/C/E, trạm sóng B, trạm ghép
  "đầu mền", dao chặt), các cụm máy theo đường giấy, giấy cuộn – nối giấy, keo tinh bột Stein-Hall (độ nhớt, điểm gel),
  hơi – nhiệt – độ ẩm, thông số giám sát trong ca, 26 mã lỗi TS-01…TS-26 của xưởng, cong tấm (warp), phồng rộp, bong lớp,
  sóng nghiêng, ván giặt, mép xơ, sáng biên; kế hoạch sóng (khổ giấy, số tấm/khổ, dao chặt), ghép đơn chạy liền,
  nhập lỗi theo dao, nhật ký tổ sóng. Dùng khi vận hành, chỉnh máy, xử lý lỗi tấm, đào tạo thợ sóng, đọc số liệu tổ sóng.
---

# mp-to-song — tấm sai thì in, bế, dán không sửa được

Lỗi ở máy sóng "các công đoạn sau không thể sửa hay bù" [AOPack]. Dây chuyền Minh Phúc chạy sóng **B, C, A, E**, sóng đôi BC/BE/BA,
**150 m/phút** danh định, tấm 3 và 5 lớp [MP-HSNL]. Hãng máy **chưa xác nhận** (cần tem nhãn).

## Bốn trạm của Minh Phúc [MP-MES — mô tả của xưởng]

```
 TRẠM SÓNG A/C/E ─▶ TRẠM SÓNG B ──▶ TRẠM GHÉP ("đầu mền") ──▶ DAO CHẶT (đếm số lượng)
 1 máy một mặt,     máy một mặt      ghép các lớp, bàn         cắt tấm theo chiều dài;
 đổi A, C hoặc E    sóng B           nhiệt máy dán đôi         1 nhát = 1 "khổ" = n tấm
 theo đơn
```

Ba đơn khác nhau có thể ở ba chỗ trên chuyền cùng lúc (quãng giấy từ trạm tới dao). Số lượng đếm ở **dao chặt**;
**số tấm/khổ** = một nhát dao chặt ra mấy tấm (sau dao cắt dọc).

## Việc thường gặp

| Việc | Đọc |
|---|---|
| Hiểu cụm máy, đường giấy, trạm nào làm gì | [references/day-chuyen-va-tram.md](references/day-chuyen-va-tram.md) |
| Thông số phải giám sát; keo tinh bột; hơi – nhiệt; nối giấy; dừng máy dài ngày | [references/thong-so-keo-hoi.md](references/thong-so-keo-hoi.md) |
| Tấm cong, phồng, bong, sóng nghiêng, mép xơ… (26 mã TS + bảng tra sâu) | [references/loi-tam-va-xu-ly.md](references/loi-tam-va-xu-ly.md) |
| Kế hoạch sóng, khổ giấy, ghép đơn, nhập lỗi theo dao, nhật ký, đơn vắt đêm | [references/ke-hoach-va-ghi-so.md](references/ke-hoach-va-ghi-so.md) |
| Kiểm tấm đầu đơn | `templates/kiem-tra-dau-don.md` (phần tổ sóng) |

## Khi có lỗi tấm — trình tự 5 bước

1. **Gọi đúng tên lỗi** theo mã TS-xx (`loi-tam-va-xu-ly.md`), chụp ảnh, đánh dấu vị trí trên khổ (trái/giữa/phải, mặt/đáy).
2. **Khoanh vùng**: lỗi từ giấy (đổi cuộn là hết?), từ keo (độ nhớt, điểm gel, khe keo), từ nhiệt – hơi (nhiệt hai đầu trục, bẫy hơi),
   từ cơ (áp trục, song song, mòn), hay từ tốc độ.
3. **Sửa một biến một lần**, ghi lại đã chỉnh gì.
4. **Ghi lỗi đúng ô** trên MES (Đổ rách, Bong dộp, Dập sóng, Sáng biên, Sai quy cách, Sai kết cấu; còn lại Lỗi khác + mã TS trong ghi chú).
5. Lỗi lặp → báo tổ trưởng / bảo trì; đưa vào sổ lỗi tổ sóng để làm bảng chuẩn.

## An toàn riêng của tổ sóng

Trục nóng, hơi áp lực, xút trong bếp keo, dao cắt ngang và dao cắt dọc, điểm kẹp giữa các trục, cuộn giấy nặng. Khoá năng lượng
(LOTO) trước khi lau trục, thay dao, gỡ kẹt — skill `mp-an-toan-lao-dong`.

## Còn thiếu (ưu tiên lấy tại xưởng)

Tem nhãn + sách từng cụm; **bảng chuẩn keo** hiện tại (công thức, độ nhớt, điểm gel); bảng góc bao gia nhiệt / áp hơi theo loại giấy
và tốc độ (kinh nghiệm thợ chính); sổ lỗi tấm. Ghi vào `docs/CAN-XAC-NHAN.md` khi có.
