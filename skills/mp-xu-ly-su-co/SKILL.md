---
name: mp-xu-ly-su-co
description: >
  Xử lý sự cố chất lượng và sản xuất xuyên mọi công đoạn của Minh Phúc: hệ mã lỗi 127 mã của xưởng (TS tổ sóng, FX flexo, OF offset,
  BO bồi, BE bế, DA dán, CH chung), 6 lỗi hay gặp mỗi máy, mổ xẻ "Lỗi khác" theo 7 nguồn (lỗi thật chưa có ô, nhập thiếu ô, hao hụt kỹ thuật,
  tồn trước máy, chênh đếm, chuyển đi, thất lạc), 6 nhóm nguyên nhân có người chịu trách nhiệm (NVL · Máy móc – khuôn bản · Vận hành ·
  Khâu trước · Kỹ thuật – kế hoạch · Kho – vận chuyển), tra theo triệu chứng, phương pháp 5 Why, xương cá, Pareto, 8D.
  Dùng khi có lỗi hàng, khiếu nại, số "Lỗi khác" cao bất thường, cần tìm nguyên nhân gốc hoặc phân loại lỗi để ghi đúng chỗ.
---

# mp-xu-ly-su-co — gọi đúng tên, tìm đúng gốc, giao đúng người

## Bốn bước cho mọi sự cố

1. **Gọi đúng tên** — tra mã lỗi của xưởng (`data/ma-loi.csv`; bảng theo máy ở skill tổ máy). Không có mã → mô tả bằng "nhận biết (nhìn thấy gì)".
2. **Khoanh vùng** — lỗi sinh ở máy này hay **khâu trước**? Đổi cuộn/lô có hết không? Từ lúc nào (sau giờ nghỉ, sau đổi đơn, sau sửa máy)?
   Tra theo triệu chứng: [references/tra-theo-trieu-chung.md](references/tra-theo-trieu-chung.md).
3. **Tìm nguyên nhân gốc** — 5 Why / xương cá; chọn **1 trong 6 nhóm nguyên nhân** để biết ai phải sửa:
   [references/sau-nhom-nguyen-nhan.md](references/sau-nhom-nguyen-nhan.md), [references/phuong-phap-tim-nguyen-nhan.md](references/phuong-phap-tim-nguyen-nhan.md).
4. **Ghi đúng chỗ và đóng vòng** — ô MES đúng loại; "Lỗi khác" phải kèm mã; hao hụt kỹ thuật, chênh đếm, chuyển đi **không phải lỗi**;
   khắc phục xong thì kiểm lại và cập nhật phiếu kiểm đầu đơn / SOP.

## Bảng tham chiếu

| Cần gì | Đọc |
|---|---|
| Hệ mã lỗi 127 mã, 6 lỗi hay gặp mỗi máy, mã chung CH-xx, ô lỗi MES từng loại máy | [references/ma-loi-xuong.md](references/ma-loi-xuong.md) |
| "Lỗi khác" gồm những gì, công thức ERP – MES, cách tách, phiếu đếm 1–2 tuần | [references/loi-khac-7-nhom.md](references/loi-khac-7-nhom.md) |
| 6 nhóm nguyên nhân, câu hỏi chọn nhóm, ví dụ theo từng máy | [references/sau-nhom-nguyen-nhan.md](references/sau-nhom-nguyen-nhan.md) |
| 5W2H, Pareto, xương cá, 5 Why, 8D, ví dụ giải mẫu | [references/phuong-phap-tim-nguyen-nhan.md](references/phuong-phap-tim-nguyen-nhan.md) |
| Triệu chứng ở khách / ở xưởng → máy nào, mã nào | [references/tra-theo-trieu-chung.md](references/tra-theo-trieu-chung.md) |
| Tra sâu theo tổ máy | `mp-to-song`, `mp-in-flexo`, `mp-xuong-offset`, `mp-be-dan` |
| Lỗi do máy hỏng (cơ khí, mòn, rò dầu) | `mp-bao-tri` |

## Câu hỏi chốt khi phân vân

> "Muốn lỗi này không lặp lại thì phải sửa cái gì?" — sửa **cách làm** → Vận hành · sửa **máy, khuôn, bản** → Máy móc – khuôn bản ·
> đổi **nguyên liệu** → NVL · **khâu trước** phải sửa → Khâu trước · sửa **phiếu, mẫu, file** → Kỹ thuật – kế hoạch · hư **sau khi rời máy** → Kho – vận chuyển.

## Lưu ý về độ tin

Danh sách 127 mã và "6 lỗi hay gặp" là bản **10/2026, xếp theo kinh nghiệm ngành, chưa có số đếm thật** tại xưởng; 6 nhóm nguyên nhân là
**đề xuất** cho phần mềm. Khi có số đếm từ phiếu đếm 1–2 tuần, cập nhật `data/ma-loi.csv` (cột `top6`) và ghi nguồn.
