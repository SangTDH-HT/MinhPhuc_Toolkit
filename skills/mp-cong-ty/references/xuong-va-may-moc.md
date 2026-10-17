# Xưởng và máy móc

Ba nguồn, độ tin khác nhau:
**[MP-HSNL]** hồ sơ năng lực 2025 (máy và công suất danh định) ·
**[MP-MES]** cấu hình và luật của phần mềm MP MES (máy đang thật sự theo dõi, đơn vị đếm) ·
**[MP-Web]** ảnh thật trong xưởng trên web.

## 1. Hai xưởng, hai dòng chảy

```
XƯỞNG FLEXO (6.000 m²) — thùng carton
 Kho giấy cuộn → TỔ SÓNG (dây chuyền tạo sóng → dao chặt tấm)
              → TỔ IN (Máy In 1, Máy In 2: in flexo + cán lằn + xẻ rãnh)
              → TỔ THÀNH PHẨM (máy bế 1/2 hoặc bế tròn → máy dán 1/2 / đóng kim)
              → KCS → đóng kiện, pallet → kho thành phẩm → giao

XƯỞNG OFFSET (2.000 m², từ 8/2022) — hộp cao cấp
 Giấy tờ rời (Couche/Ivory/Duplex) → máy xén → Máy In Offset 5 màu
              → gia công bề mặt (cán màng, UV, ép kim, dập nổi…) → máy bồi (lên tấm sóng, thường sóng E)
              → bế → dán → KCS → giao
```

Đơn cán màng ở xưởng flexo đi vòng: **máy in in → máy cán màng → quay lại chính máy in để cắt rãnh**
(kế hoạch máy in có một dòng cho cả hai lượt). [MP-MES]

Kế hoạch trên ERP đánh dấu đơn đi qua những công đoạn nào bằng 7 cờ: **Sóng · In · Bế · Bồi · Dán · Đóng kim · Khác**
(1 = có, 0 = không, trống = chưa khai). [MP-MES]

## 2. Danh sách máy theo hồ sơ năng lực [MP-HSNL, MP-Web]

| # | Máy | SL | Năng lực công bố | Việc | Ghi chú |
|---|---|---|---|---|---|
| 1 | Dây chuyền tạo sóng | 1 | Sóng B, C, A, E; sóng đôi BC, BE, BA; 150 m/phút | Ghép giấy mặt + giấy sóng thành tấm 3/5 lớp, chặt tấm | |
| 2 | Máy in flexo 5 màu | 2 | 150 nhịp/phút | In trực tiếp lên tấm, kèm cán lằn + xẻ rãnh (printer-slotter) | MES khai **6 trạm mực** cho Máy In 1, 2 → cần xác nhận |
| 3 | Máy in flexo 5 màu (process) | 1 | 250 sản phẩm/phút | In process nhiều màu | Chỉ HSNL nêu; MES chưa có máy này |
| 4 | Máy bế tự động | 2 | Máy 1: 3.500 nhịp/giờ; máy 2: 5.500 nhịp/giờ; ≥ 58.000 tờ/ngày | Bế hình, khe, lằn | MES: Máy bế tự động 1, 2 |
| 5 | Máy bế tròn tự động | 1 | 150 nhịp/phút | Bế tốc độ cao | Chỉ HSNL nêu |
| 6 | Máy dán tự động (folder-gluer) | 1 | 150 m/phút | Gấp dán tai thùng | MES có **2 máy dán** (Máy dán tự động 1, 2 — máy 2 thêm 9/2026) |
| 7 | Máy in kỹ thuật số | 1 | ≥ 2.000 m²/8 giờ | Làm mẫu, đơn ít, không cần bản | |
| 8 | Máy in offset 5 màu **Mitsubishi** | 1 | 250 nhịp/phút | In tờ rời cho hộp cao cấp | MES: Máy In Offset, 5 trạm mực |
| 9 | Máy bồi tự động **YB-1300E** | 1 | ≥ 56.000 sản phẩm/8 giờ | Bồi tờ in offset lên tấm sóng | MES: Máy bồi |
| 10 | Máy xén **115SC** | 1 | 45 lần/phút | Xén giấy | |
| 11 | Máy cán màng nhiệt | 1 | — | Cán OPP/PE bóng, mờ, 1–2 mặt | ERP: công đoạn "MB – Cán màng bóng" |
| 12 | Máy bế phẳng (xưởng offset) | 1 | — | Bế hộp, khay | |
| 13 | Máy dán tự động (xưởng offset) | 1 | — | Gấp dán hộp offset | |

Phòng QC: máy nén thùng (BCT), nén cạnh (ECT), nén vòng (RCT), máy bục, dụng cụ Cobb, cân định lượng,
máy kéo (lực căng). Chi tiết: skill `mp-kcs-chat-luong`.

> Ảnh máy trong hồ sơ năng lực phần lớn là **ảnh minh hoạ của hãng**. Ngoài Mitsubishi, YB-1300E, 115SC thì hãng,
> model, năm sản xuất **chưa biết** — muốn tra sách hướng dẫn, mã lỗi phải chụp tem nhãn từng máy
> (biểu mẫu `templates/khao-sat-tem-nhan-may.md`).

## 3. Chín máy đang theo dõi trên MP MES [MP-MES]

| Máy | Mã máy trên kế hoạch/nhật ký | Tổ | Một lần đếm là | Sản lượng ghi bằng | Tốc độ ghi bằng | Ô lỗi trên MES |
|---|---|---|---|---|---|---|
| Tổ sóng (dây chuyền) | DS1 | Tổ sóng | một nhát dao chặt | số dao; số tấm = dao × số tấm/khổ | m/phút | Đổ rách · Bong dộp · Dập sóng · Sáng biên · Sai quy cách · Sai kết cấu · Lỗi khác |
| Máy In 1 (flexo) | MI1 | Tổ in | một nhịp = một tờ in | tờ in (không nhân số con) | nhịp/phút | Sóng · Thử máy · In lệch · Nhảy dao · Khác (ERP gọi "Ngoại quan") |
| Máy In 2 (flexo) | MI2 | Tổ in | một nhịp = một tờ in | tờ in (không nhân số con) | nhịp/phút | như Máy In 1 |
| Máy In Offset | MI3 | Tổ in | một nhịp | tờ | nhịp/phút | như Máy In 1 |
| Máy dán tự động 1 | DT1 | Tổ thành phẩm | một thùng | thùng (số con = 1) | nhịp/phút | Sóng · In · Bế · Định hình · Khác |
| Máy dán tự động 2 | DT2 | Tổ thành phẩm | một thùng | thùng | nhịp/phút | như máy dán 1 |
| Máy bế tự động 1 | BF1 | Tổ thành phẩm | một nhịp dao | con = nhịp × số con | nhịp/phút | Sóng · In · Bế · Định hình · Khác |
| Máy bế tự động 2 | BF2 | Tổ thành phẩm | một nhịp dao | con = nhịp × số con | nhịp/phút | như máy bế 1 |
| Máy bồi | BOI | Tổ thành phẩm | một tấm | tấm | nhịp/phút | Sóng · In · Bế · Định hình · Khác |

Các điểm phải nhớ:

- **Dây chuyền sóng có 4 trạm**: trạm sóng A/C/E (một máy sóng một mặt, chạy sóng A, C **hoặc** E theo kế hoạch),
  trạm sóng B, **trạm ghép** (thợ gọi "đầu mền" — ghép các lớp), **dao chặt** (nơi đếm số lượng). Ba đơn khác nhau
  có thể đang ở ba chỗ trên chuyền cùng lúc (do quãng đường giấy từ mỗi trạm tới dao). [MP-MES, mô tả của xưởng 22/09/2026]
- Đơn máy offset **không chuyển** sang máy flexo được và ngược lại (bản kẽm ≠ bản flexo). Chỉ chuyển đơn (chưa chạy) giữa
  Máy In 1 ↔ Máy In 2, máy dán 1 ↔ máy dán 2, máy bế 1 ↔ máy bế 2. Máy dán ↔ máy bế **không** chuyển (khác công đoạn).
- Máy In Offset không có nút Start vật lý ngoài máy; lệnh chạy từ phần mềm.
- Phiếu nhận dạng lô hàng (biểu mẫu **SX-QT01-BM02/06**) chỉ in ở **máy dán** — máy bế ra tấm rời, máy bồi ra tấm,
  chưa thành thùng để xếp pallet.
- Máy bế có hiện tượng **đếm đôi** (cảm biến thấy cả nhíp và tờ) → chênh đếm, không phải hàng hư (mã BE-17).

## 4. Ba kho khuôn – bản [MP-MES]

| Kho | Của máy | Mã vật tư |
|---|---|---|
| Kho bảng in flexo | Máy In 1, Máy In 2 | **BI** + mã sản phẩm |
| Kho bản kẽm offset | Máy In Offset | **BK** + mã sản phẩm |
| Kho khuôn bế | máy bế | **KB** + mã sản phẩm |

Luật đặt mã của xưởng (chốt 27/08/2026): mã bản/khuôn **suy ra từ mã sản phẩm**; đơn mượn khuôn của mã khác
hoặc bản làm lại mang mã riêng thì ghi đè trên kế hoạch. Cùng một mã sản phẩm chạy hai công nghệ là **hai bản khác nhau**.

## 5. Ảnh thật trong xưởng [MP-Web]

Thư mục `C:\MinhPhuc\Website_MinhPhucPack\_raw\assets\images\nha-may\`: toàn cảnh dây chuyền sóng, giá cấp giấy cuộn,
cụm gia công tấm, bàn điều khiển dây chuyền, bảng điều khiển máy in flexo, máy dán thùng, kho giấy cuộn,
tấm carton chờ gia công, phòng QC. Video nhà máy: `Tai_lieu_goc\Video_nha_may\` (4 file).

## 6. Chỗ các nguồn chưa khớp — hỏi lại tại xưởng

| Nội dung | Nguồn A | Nguồn B |
|---|---|---|
| Máy in flexo mấy màu | HSNL: 5 màu | MES: 6 trạm mực (Máy In 1, 2) |
| Số máy dán | HSNL: 1 máy dán xưởng flexo + 1 xưởng offset | MES: Máy dán tự động 1 và 2 cùng tổ thành phẩm |
| Máy in flexo process 250 sp/phút, máy bế tròn | HSNL có | Web, MES không có |
| Số cơ sở | Web, chứng nhận: chỉ Linh Xuân | HSNL: thêm chi nhánh Dĩ An |
| Công đoạn đóng kim | Cờ "Đóng kim" có trên kế hoạch ERP | Không thấy máy đóng ghim trong HSNL |
