# Đơn vị đếm và công thức

Nguồn: luật MP MES và quy ước đối chiếu dữ liệu (08–10/2026) [MP-MES]. Đây là chỗ hay hiểu sai nhất khi đọc số — đọc kỹ trước khi so hai máy.

## 1. Mỗi máy đếm một thứ

| Máy | Một lần đếm là | Sản lượng ghi bằng | Kế hoạch ghi bằng | Tốc độ |
|---|---|---|---|---|
| Tổ sóng | 1 nhát **dao** chặt (1 khổ đầy) | nhật ký: **số dao**; **số tấm** = số dao × số tấm/khổ (máy in lấy làm "Sóng vào") | **SL giấy tấm = số nhát dao**, mét dài | m/phút |
| Máy In 1, 2 (flexo) | 1 **nhịp** = 1 **tờ in** | **tờ in** (cột số lượng = nhịp + tờ thử máy) — **không nhân số con** | tờ (nhịp) | nhịp/phút |
| Máy In Offset | 1 nhịp = 1 tờ | **tờ** | tờ | nhịp/phút |
| Máy bế 1, 2 | 1 **nhịp** dao = 1 tờ vào | **con** = nhịp × số con | **nhịp** | nhịp/phút |
| Máy dán 1, 2 | 1 **thùng** đã dán | **thùng** (số con = 1) | **cái** | nhịp/phút |
| Máy bồi | 1 **tấm** | **tấm** | tấm | nhịp/phút |

"Số con" = số sản phẩm ra từ một tờ / một nhịp (tấm in hai con, khuôn bế ba con…). Ở máy in, số con **chỉ dùng để quy ra thùng** khi so với công đoạn
sau — nhật ký máy in đo bằng tờ in.

**Quy ước đối chiếu:** *một tấm sóng = một tờ in = một nhịp bế; sản phẩm (thùng, con) = tờ × số con.* Không cộng chéo tấm với thùng; so hai công đoạn
thì **quy về đơn vị của công đoạn SAU** và ghi rõ đã quy đổi. Không cộng sản lượng của các máy với nhau.

## 2. Chuỗi quy đổi

```
Số nhịp thực hiện = số máy đếm (nhịp) + Chạy trước (NHỊP, thợ gõ — phần bộ đếm không có)
Máy in : sản lượng = số nhịp thực hiện (tờ in)
Máy bế : sản lượng = số nhịp thực hiện × số con        ← nhân MỘT lần, ở bước cuối, trên TỔNG nhịp
Tốc độ  = số nhịp thực hiện ÷ tổng thời gian tính tốc độ  (nhịp/phút)
```

- Máy bế: nhân riêng phần trong ca rồi cộng thẳng phần chạy trước → cả đơn hụt **(số con − 1) × số nhịp chạy trước** mà không có gì báo.
- Start **không** xoá bộ đếm; gõ vào ô Chạy trước phần đã có trên bộ đếm là **đếm hai lần**.
- Tốc độ đo bằng **nhịp/phút** để so được với tốc độ thiết kế và giữa các đơn.
- Thanh tiến độ, ô Đã làm, Còn lại đo bằng **đơn vị sản phẩm** của máy; ô Chạy trước, số nhịp máy, tốc độ dùng **đơn vị bộ đếm**.
- Lỗi: máy in gõ theo **tờ in** (không nhân số con); máy bế theo **con**; máy dán theo **thùng**; máy bồi theo **tấm**; tổ sóng theo **dao**, lưu × số tấm/khổ
  (trừ Sai kết cấu), dao chạy bù bấy nhiêu dao.
- **In 2 mặt**: số nhịp = mặt 1 + mặt 2 (tốc độ chia số này); sản lượng = **số tờ** (chồng giấy).

## 3. Thừa / thiếu và lệch

| Đại lượng | Công thức | Ghi chú |
|---|---|---|
| Thừa / thiếu | Sản lượng − **kế hoạch của máy** | Kế hoạch = "số mà máy sẽ chạy": máy in SL sản xuất, TP số nhịp SX × số con, tổ sóng kế hoạch dao — **không** phải SL đơn hàng (chốt 10/10/2026) |
| SP lệch (máy in) | Sóng vào − số nhịp − tổng lỗi | Giữ công thức cũ để so bản ghi cũ; **Sóng vào** = số tấm của tổ sóng (thợ in không gõ) |
| "Lỗi khác" ERP (máy in) | Tấm sóng chuyển qua (sóng OK) − tổng số lượng in | Không trừ lỗi đã nhập → có thể đếm hai lần; có thể âm |
| Tổng lỗi | Cộng các ô lỗi | Cùng đơn vị với sản lượng của máy (tổ sóng: đã nhân số tấm/khổ) |

## 4. Đối chiếu công đoạn — so cho đúng

1. **Quy về đơn vị công đoạn sau**:
   - sóng → in: **số tấm** sóng (không phải số dao) ↔ **tờ** in;
   - in → bế: tờ ↔ nhịp;
   - bế → dán: con ↔ cái;
   - in → dán: tờ × số con ↔ cái.
2. **Theo phiếu, khi đơn đã xong** — không theo ngày (hàng giao hôm nay, mai mới chạy là **tồn trước máy**).
3. Cộng **mọi bản ghi** của phiếu (dở dang, chuyển ngày, chạy 2 lần, lưu bù, đơn cán màng: "đã dùng" lấy lượt In, "đạt" lấy lượt cuối).
4. Trừ phần **không phải lỗi**: KCS lấy mẫu, mượn tấm, trả lại khâu trước, chênh đếm (máy bế đếm đôi).
5. Phần còn lại mới là hư thật / thất lạc → truy theo phiếu (skill `mp-xu-ly-su-co` → `loi-khac-7-nhom.md`).

## 5. Ví dụ

**Máy bế 2, khuôn 2 con**: bộ đếm 2.750 nhịp, chạy trước 250 nhịp, lỗi 60 con, kế hoạch 6.000 con.
→ nhịp thực hiện = 3.000 → sản lượng = 6.000 con → thừa/thiếu = 0 → đạt = 5.940.
Sai cách (nhân trước rồi cộng chạy trước): 2.750 × 2 + 250 = 5.750 → báo **thiếu 250** oan.

**Máy in, đơn 2 con, cùng 3.000 nhịp**: sản lượng = **3.000 tờ**; muốn so với máy dán thì quy ra 3.000 × 2 = 6.000 thùng (và ghi rõ đã quy đổi).

Máy tính: `python -m mptinh san-luong --nhip 2750 --chay-truoc 250 --so-con 2 --ke-hoach 6000 --loi 60` (máy in: để `--so-con 1`).
