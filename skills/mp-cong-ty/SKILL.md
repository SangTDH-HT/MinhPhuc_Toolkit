---
name: mp-cong-ty
description: >
  Hồ sơ Công ty TNHH Bao Bì Minh Phúc: pháp lý, lịch sử, địa chỉ, chứng nhận ISO 9001 và FSC CoC,
  sơ đồ tổ chức, hai xưởng (flexo và offset), danh sách máy và công suất công bố, các máy đang theo dõi
  trên MP MES (mã máy, đơn vị đếm), khách hàng, ngành hàng, vùng giao hàng, cam kết bán hàng và
  định hướng phát triển. Dùng khi câu hỏi cần biết "Minh Phúc có gì, làm gì, cho ai", khi viết tài liệu
  giới thiệu, hồ sơ nhà cung cấp, trả lời khách, hoặc khi cần đối chiếu máy thật trước khi tra kỹ thuật.
---

# mp-cong-ty — Minh Phúc là ai, có gì

Đây là nền của cả repo: mọi câu trả lời kỹ thuật phải khớp với những gì Minh Phúc thật sự có.
Không bịa máy, không bịa khách hàng, không bịa thông số. Thiếu thì ghi "chưa xác nhận".

## Tóm tắt một màn

- **Công ty TNHH Bao Bì Minh Phúc** (Minh Phuc Packaging Co., Ltd) — MST 0314500525, vốn 40 tỷ.
  Thành lập 2011 (tiền thân Bao Bì Thành Đồng), đổi tên Minh Phúc 8/2017. Giám đốc: Lê Quốc Sinh. [MP-Web]
- Nhà máy: 34-36-36A Đường số 9, KP5, P. Linh Xuân, TP.HCM (Thủ Đức cũ) — 9.000 m²
  (xưởng flexo 6.000 m², xưởng offset 2.000 m² từ 8/2022). [MP-Web][MP-HSNL]
- Công suất công bố: > 100.000 sản phẩm/ngày; giấy nguyên liệu ≥ 1.200 tấn/tháng; kho giấy > 1.200 tấn.
- **ISO 9001:2015** (SGS, VN20/00151) và **FSC CoC** SGSHK-COC-370661, nhãn FSC-C197558, hệ thống
  chuyển giao (transfer system). [MP-Web][chứng nhận gốc]
- Sản phẩm: thùng carton 3 và 5 lớp (không làm 7 lớp), giấy tấm, vách ngăn, hộp in offset bồi sóng,
  hộp âm dương, túi giấy, hộp tiếp xúc thực phẩm (gà rán, burger).
- Hai xưởng: **flexo** (sóng → in flexo → bế → dán) và **offset** (xén → in offset → cán màng → bồi → bế → dán).

## Bảng tham chiếu

| Cần gì | Đọc |
|---|---|
| Pháp lý, lịch sử, địa chỉ, chứng nhận, tổ chức, cam kết bán hàng | [references/ho-so-cong-ty.md](references/ho-so-cong-ty.md) |
| Hai xưởng, 13 máy theo hồ sơ năng lực, 9 máy trên MP MES, đơn vị đếm, chỗ còn vênh | [references/xuong-va-may-moc.md](references/xuong-va-may-moc.md) |
| Khách hàng, ngành hàng và quy cách thường dùng theo ngành, vùng giao | [references/khach-hang-nganh-hang.md](references/khach-hang-nganh-hang.md) |
| Tầm nhìn, nhịp đầu tư, năm hướng phát triển và đòi hỏi với người kỹ thuật | [references/dinh-huong-phat-trien.md](references/dinh-huong-phat-trien.md) |
| Danh sách máy dạng dữ liệu | [../../data/may-moc.yaml](../../data/may-moc.yaml) |
| 45 mẫu đã sản xuất (MP-001 … MP-046) | [../../data/mau-san-pham.json](../../data/mau-san-pham.json) |

## Quy tắc khi trả lời

1. Máy nào Minh Phúc **không có** thì nói rõ (ví dụ: không làm thùng 7 lớp, không làm túi chống tĩnh điện).
2. Hãng/model máy: chỉ biết chắc **Mitsubishi** (offset 5 màu), **YB-1300E** (máy bồi), **115SC** (máy xén).
   Các máy khác chưa có tem nhãn → hỏi hoặc ghi "chưa xác nhận", không đoán hãng.
3. Số liệu công bố (150 m/phút, 3.500/5.500 nhịp/giờ…) là **năng lực danh định**, không phải tốc độ chạy thực tế
   hằng ngày. Tốc độ thực tế lấy từ nhật ký MP MES (xem `mp-ke-hoach-san-xuat`).
4. Có chỗ các nguồn chưa khớp (chi nhánh Dĩ An, flexo 5 màu hay 6 trạm mực…) — xem mục cuối của
   `xuong-va-may-moc.md` và `docs/CAN-XAC-NHAN.md`; nêu cả hai nguồn khi trả lời.
5. Tên người cụ thể chỉ dùng khi nguồn công khai (Giám đốc); còn lại dùng vai trò (tổ trưởng, KCS, kế hoạch…).
