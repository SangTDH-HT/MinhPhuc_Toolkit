# Đơn vị đếm và công thức

## 1. Mỗi máy đếm một thứ [MP-MES]

| Máy | Một lần đếm là | Sản lượng ghi bằng | Kế hoạch ghi bằng | Tốc độ |
|---|---|---|---|---|
| Tổ sóng | 1 nhát **dao** chặt (1 khổ) | **tấm** = dao × số tấm/khổ | tấm (SL sản xuất), mét dài | m/phút |
| Máy In 1, 2 (flexo) | 1 **nhịp** | **tấm** = nhịp × số con | nhịp/tấm theo đơn | nhịp/phút |
| Máy In Offset | 1 **nhịp** | **tờ** | | nhịp/phút |
| Máy bế 1, 2 | 1 **nhịp** dao | **con** = nhịp × số con | **nhịp** | nhịp/phút |
| Máy dán 1, 2 | 1 **thùng** đã dán | **thùng** (số con = 1) | **cái** | nhịp/phút |
| Máy bồi | 1 **tấm** | **tấm** | tấm | nhịp/phút |

"Số con" = số sản phẩm ra từ một nhịp/một tấm (in hai con trên một tấm, khuôn bế ba con…).

## 2. Chuỗi quy đổi — nhân số con **một lần, ở cuối**

```
Số nhịp thực hiện = số máy đếm (nhịp) + Chạy trước (NHỊP, thợ gõ — phần bộ đếm không có)
Sản lượng          = số nhịp thực hiện × số con
Tốc độ             = số nhịp thực hiện ÷ tổng thời gian tính tốc độ
```

- Nhân riêng phần trong ca rồi cộng thẳng phần chạy trước → cả đơn hụt **(số con − 1) × số nhịp chạy trước** mà không có gì báo.
- Start **không** xoá bộ đếm; gõ vào ô Chạy trước phần đã có trên bộ đếm là **đếm hai lần**.
- Tốc độ đo bằng **nhịp/phút** để so được với tốc độ thiết kế và giữa các đơn (quy ra tấm thì đơn hai con hiện gấp đôi đơn một con).
- Thanh tiến độ, ô Đã làm, Còn lại đo bằng **đơn vị sản phẩm** (để % hoàn thành có nghĩa); ô Chạy trước, số nhịp máy, tốc độ dùng **đơn vị bộ đếm**.
- Tổ sóng: lỗi nhập theo **dao**, lưu × số tấm/khổ (trừ Sai kết cấu); dao chạy bù bấy nhiêu dao.
- **In 2 mặt**: số nhịp = mặt 1 + mặt 2 (tốc độ chia số này); sản lượng = **số tờ** (chồng giấy).

## 3. Thừa / thiếu và lệch

| Đại lượng | Công thức | Ghi chú |
|---|---|---|
| Thừa / thiếu | Sản lượng − **kế hoạch của máy** | Kế hoạch = "số mà máy sẽ chạy": máy in SL sản xuất, TP số nhịp SX × số con, sóng số tấm — **không** phải SL đơn hàng (chốt 10/10/2026) |
| SP lệch (máy in) | Sóng vào − (sản xuất + chạy trước) − tổng lỗi | Sóng vào đọc từ nhật ký tổ sóng (thợ in không gõ) |
| "Lỗi khác" ERP (máy in) | Tấm sóng chuyển qua (sóng OK) − tổng số lượng in | Không trừ lỗi đã nhập → có thể đếm hai lần; có thể âm |
| Tổng lỗi | Cộng các ô lỗi (đã nhân số con) | Cùng đơn vị với sản lượng |

## 4. Đối chiếu công đoạn — so cho đúng

1. **Cùng đơn vị**: tấm sóng ↔ tấm in (nhịp × số con) ↔ con bế ↔ thùng dán (quy theo số con của từng bước).
2. **Theo phiếu, khi đơn đã xong** — không theo ngày (hàng giao hôm nay, mai mới chạy là **tồn trước máy**).
3. Cộng **mọi bản ghi** của phiếu (dở dang, chuyển ngày, chạy 2 lần, lưu bù).
4. Trừ phần **không phải lỗi**: KCS lấy mẫu, mượn tấm, trả lại khâu trước, chênh đếm (máy bế đếm đôi).
5. Phần còn lại mới là hư thật / thất lạc → truy theo phiếu (skill `mp-xu-ly-su-co` → `loi-khac-7-nhom.md`).

## 5. Ví dụ

Máy in, đơn 2 con: bộ đếm 2.750 nhịp, chạy trước 250 nhịp, lỗi 60 tấm, kế hoạch 6.000 tấm.
→ nhịp thực hiện = 3.000 → sản lượng = 6.000 tấm → thừa/thiếu = 0 → tấm đạt = 5.940.
Nếu sai cách (nhân trước rồi cộng chạy trước): 2.750 × 2 + 250 = 5.750 → báo **thiếu 250** oan.

Máy tính: `python -m mptinh san-luong --nhip 2750 --chay-truoc 250 --so-con 2 --ke-hoach 6000 --loi 60`.
