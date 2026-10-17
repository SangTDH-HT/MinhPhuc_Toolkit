# Kế hoạch sóng, ghép đơn và ghi sổ tổ sóng

Luật dưới đây là luật nghiệp vụ đã chốt khi đưa MP MES vào tổ sóng (9–10/2026) [MP-MES]. Cách bấm trên phần mềm: skill `mp-mes-su-dung`.

## 1. Một dòng kế hoạch sóng có gì

| Nhóm | Thông tin |
|---|---|
| Nhận diện | STT, số đơn hàng, **phiếu sản xuất** (lệnh SX), khách hàng, mã hàng, tên hàng, kiểu sản phẩm, ghi chú, số PO |
| Số lượng | SL đơn hàng, SL sản xuất, **SL giấy tấm** (= số **nhát dao** phải chặt — dao đếm theo cột này), **SL mét dài** (= SL giấy tấm × tổng dài), **số tấm/khổ**, cột dao chặt (hiện trên tab Đơn hàng, không dùng để đếm) |
| Quy cách | Quy cách phủ bì, **quy cách cán lằn**, tổng dài, tổng rộng, **khổ giấy LT** (lý thuyết), **khổ giấy SD** (sử dụng) |
| Kết cấu | Kiểu sóng; giấy từng lớp: **Mặt · B · Giữa · E · A · C · Đáy** |
| Công đoạn | 7 cờ: Sóng · In · Bế · Bồi · Dán · Đóng kim · Khác (1 có / 0 không / trống chưa khai) |
| Thời gian | Ngày sản xuất, thời gian sóng, từ giờ – đến giờ |

Đơn có STT = 0 **không vào** thứ tự chạy (hiện ở ô "đơn chưa có thứ tự chạy").

## 2. Thứ tự chạy khi văn phòng thêm/đổi đơn (chốt 13/10/2026)

- Đơn **đã chạy** và **đang chạy** giữ nguyên chỗ; đơn đang chạy không bị ảnh hưởng.
- Các đơn còn lại xếp theo **STT của kế hoạch**, đứng sau đơn đang chạy.
- Đơn có STT nhỏ hơn đơn đang chạy (văn phòng chèn lên trước) thì xếp **ngay sau** đơn đang chạy.
- Thứ tự thợ đã tự đổi trên phần mềm vẫn được giữ (đã ghi STT lên máy chủ).

## 3. Ghép đơn chạy liền (chốt 14/10/2026)

**Ghép = tích các đơn chạy chung cuộn giấy (cùng giấy, cùng khổ) thành một nhóm.** Trong nhóm, chạy xong đơn trước là chạy luôn đơn sau,
**không cần bấm Start**; mỗi đơn vẫn lưu nhật ký riêng. Ngoài nhóm, chạy xong một đơn dao dừng chờ **Start**.

Ví dụ của xưởng: đang chạy đơn 1; đơn 2 không ghép; ghép 3+4, 7+8, 9+11:
```
1 ─Start─▶ 2 ─Start─▶ [3 → 4] ─Start─▶ 5 ─Start─▶ 6 ─Start─▶ [7 → 8] ─Start─▶ [9 → 11] ─Start─▶ 10 …
```
- Đơn trong nhóm không liền nhau thì đơn sau được dời lên ngay sau đơn trước (9, 11, 10).
- Văn phòng đánh lại STT / thêm đơn **không làm rã nhóm**: mỗi lần nạp kế hoạch, nhóm được dán lại liền nhau.
- **Ghép thêm** = tích đơn mới cùng một đơn của nhóm. Bỏ ghép = bỏ tích; nhóm còn dưới 2 đơn thì tự bỏ.
- Phần mềm báo ✓ khớp hẳn / ✓ cùng giấy cùng khổ, hoặc ⚠ lệch — đơn lệch giấy/khổ thì cân nhắc trước khi ghép.
- Cụm sóng đã chạy giấy của một đơn chen giữa thì không ghép qua được.

Khác với **ghép khổ** trong kế hoạch sóng truyền thống (xếp hai quy cách song song trên cùng bề ngang giấy để giảm biên) — đó là việc của
người lập kế hoạch khi chọn khổ giấy, xem mục 7.

## 4. Nhập lỗi theo dao (chốt 14/10/2026 — "ghi như phần mềm cũ")

- Thợ nhập lỗi **theo dao** (số nhát dao bị lỗi).
- **Lỗi mấy dao thì dao chạy bù bấy nhiêu dao.**
- Khi lưu, nhật ký ghi lỗi = số dao lỗi × **số tấm/khổ** (trừ **Sai kết cấu**).
- Tấm đạt, so kế hoạch, đối chiếu công đoạn giữ công thức cũ.
- Ô lỗi: Đổ rách · Bong dộp · Dập sóng · Sáng biên · Sai quy cách · Sai kết cấu · Lỗi khác. Lỗi không có ô → Lỗi khác + **mã TS-xx** trong ghi chú.
- Mét lỗi nhập ở màn hình hai cụm sóng (ô nhập tự cộng dồn; nhập âm để sửa).

## 5. Chốt sổ và sửa nhật ký

- Bản ghi tổ sóng có hai trạng thái: **0** = phần mềm vừa chốt tự động, chưa ai xác nhận · **1** = tổ trưởng đã nhập **số thực** và chốt.
- Nhật ký sóng: ô đầu là **Số dao** (số nhát đã chặt — như phần mềm cũ). Từ 15/10/2026 MES ghi thêm **số tấm** = số dao × số tấm/khổ;
  máy in lấy số tấm này làm **"Sóng vào"** (bản ghi cũ chưa có thì tự nhân theo số tấm/khổ của kế hoạch). So kế hoạch, đối chiếu, trợ lý vẫn đo **dao**.
  → Khi so sóng với in: so **tấm** với **tấm**, đừng so số dao với số tờ in.
- **Vận hành được sửa nhật ký tổ sóng** (chốt 13/10/2026) — riêng tổ sóng; nhật ký máy in và thành phẩm vẫn do KCS sửa.
- Đơn **vắt đêm**: đợi dao chặt xong đơn dở rồi mới sang kế hoạch ngày mới; nhật ký đơn vắt đêm ghi **ngày bắt đầu đơn**.
- Phiếu nhận dạng tổ sóng tích các ô công đoạn theo 7 cờ của kế hoạch (Bồi đứng trước Bế trên tờ phiếu).

## 6. Thời gian và tốc độ

- Tốc độ tổ sóng tính bằng **mét/phút** = mét dài (số dao × tổng dài tấm) ÷ tổng thời gian.
- Tổng thời gian tổ sóng = **chạy + ngừng không kế hoạch (KOKH)**; ngừng có kế hoạch, bảo trì, nghỉ ca không vào tổng (chốt 02/10/2026).
- Dừng ngắn dưới **30 giây** vẫn tính chạy (ân hạn); đứng quá 30 giây mới là ngừng.
- Chi tiết 6 loại thời gian: skill `mp-ke-hoach-san-xuat`.

## 7. Chọn khổ giấy và hao biên [KN ngành]

```
Khổ giấy cần (mm) = số tấm/khổ × tổng rộng tấm + biên xén hai mép
Hao biên (%)      = (khổ giấy SD − số tấm/khổ × tổng rộng) / khổ giấy SD × 100
Mét dài cần       ≈ số dao × tổng dài tấm / 1000 × (1 + % hao đầu đơn, đổi đơn)
```

- Biên xén tối thiểu tuỳ máy (dao cắt dọc cần ăn vào mép để mép tấm sạch) — **giá trị của dây chuyền Minh Phúc chưa có**, hỏi tổ sóng.
- Chọn khổ giấy SD ≥ khổ LT gần nhất trong các khổ cuộn đang có trong kho; khổ quá hẹp → **sáng biên** (TS-19).
- Ghép khổ (hai quy cách cùng giấy chạy song song) giảm hao biên nhưng hai đơn phải cùng kết cấu giấy, cùng sóng.
- Hao hụt kỹ thuật (tấm chuyển đơn, đầu cuộn — TS-25) ghi riêng, không tính lỗi.

Máy tính: `python -m mptinh kho-giay --rong-tam 520 --so-tam 3 --kho 1600`.
