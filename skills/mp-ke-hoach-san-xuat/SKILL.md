---
name: mp-ke-hoach-san-xuat
description: >
  Hệ thống sản xuất của Minh Phúc: dòng chảy đơn hàng từ kinh doanh tới giao hàng, lệnh sản xuất (phiếu), 7 cờ công đoạn, kế hoạch theo máy và
  ngày, STT, trạng thái đơn, dở dang – Chuyển ngày – Ngưng đơn, ca làm việc và Bảng 01, sáu loại thời gian (chạy máy, ngừng không kế hoạch,
  ngừng có kế hoạch, nghỉ ca, bảo trì, pha mực/chuẩn bị) và luật phân loại, đơn vị đếm từng máy (dao, tấm, nhịp, con, tờ, thùng; nhịp × số con),
  tốc độ, thừa/thiếu, SP lệch, đối chiếu công đoạn, chỉ số hiệu suất OEE (sẵn sàng × hiệu năng × chất lượng), hao hụt, đổi đơn.
  Dùng khi lập/đọc kế hoạch, đọc báo cáo nhật ký, giải thích một con số trên MES, tính hiệu suất, tìm chỗ mất năng suất.
---

# mp-ke-hoach-san-xuat — mỗi con số có một định nghĩa

Luật trong skill này là **luật nghiệp vụ đã chốt** khi đưa MP MES vào xưởng (8–10/2026) [MP-MES]: đọc số liệu Minh Phúc thì phải đọc theo luật này,
nếu không sẽ so "tấm" với "nhịp", "ngày" với "phiếu", và kết luận sai.

## Bảng tham chiếu

| Cần gì | Đọc |
|---|---|
| Đơn đi qua xưởng thế nào; kế hoạch, STT, trạng thái; dở dang, Chuyển ngày, Ngưng đơn; hàng mới, hàng mẫu; chuyển máy | [references/dong-chay-don-hang.md](references/dong-chay-don-hang.md) |
| Sáu loại thời gian, thứ tự ưu tiên, 30 giây ân hạn, ca và Bảng 01, tổng thời gian từng loại máy | [references/sau-loai-thoi-gian.md](references/sau-loai-thoi-gian.md) |
| Đơn vị đếm từng máy, nhịp × số con, Chạy trước, thừa/thiếu, SP lệch, đối chiếu công đoạn | [references/don-vi-dem-va-cong-thuc.md](references/don-vi-dem-va-cong-thuc.md) |
| Tốc độ, OEE theo định nghĩa Minh Phúc, hao hụt, đổi đơn, báo cáo ngày/tuần | [references/chi-so-hieu-suat.md](references/chi-so-hieu-suat.md) |
| Cách bấm trên phần mềm | skill `mp-mes-su-dung` |
| Kế hoạch tổ sóng, ghép đơn, khổ giấy | skill `mp-to-song` → `ke-hoach-va-ghi-so.md` |

## Mười luật phải thuộc

1. **Lưu đơn = đơn xong** (dù thiếu số). Muốn chạy tiếp ngày sau: **Chuyển ngày** (máy in, TP) hoặc **Ngưng đơn** (TP).
2. Mỗi giây thuộc **đúng một** trong sáu loại thời gian; **nghỉ ca thắng tất cả** (khi máy không ra hàng).
3. **Bảo trì phải có lý do** mới vào cột bảo trì; bấm chạy lại là **hết bảo trì**.
4. Máy đứng **quá 30 giây** mới là ngừng; dưới 30 giây vẫn là chạy.
5. **Bấm Start = hết chuẩn bị**; chưa chọn đơn hoặc chưa Start là **pha mực/chuẩn bị** (máy in); **hết đơn** là **ngừng có kế hoạch**.
6. Tốc độ = **nhịp ÷ tổng thời gian tính tốc độ** (máy in: chạy + KOKH + pha mực; TP: chạy + KOKH; sóng: mét ÷ (chạy + KOKH)).
7. Sản lượng = **nhịp × số con** — nhân một lần, ở bước cuối; ô **Chạy trước** là **nhịp**.
8. Thừa/thiếu so với **kế hoạch của máy** (số máy sẽ chạy), không so số lượng đơn hàng.
9. Đối chiếu công đoạn tính **theo phiếu khi đơn đã xong**, cùng một đơn vị — không theo ngày.
10. Gộp chỉ số nhiều đơn: **cộng tử rồi chia**, không lấy trung bình các tỷ lệ.
