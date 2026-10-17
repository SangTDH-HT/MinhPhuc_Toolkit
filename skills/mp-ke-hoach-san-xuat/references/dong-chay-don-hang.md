# Dòng chảy đơn hàng và kế hoạch

## 1. Từ khách tới kho [MP-Web][MP-MES]

```
Kinh doanh nhận yêu cầu → tư vấn, báo giá (≤ 4 giờ) → Thiết kế: dieline + mẫu in KTS (1–3 ngày) → khách duyệt mẫu (kết cấu + màu)
 → Kế hoạch lập LỆNH SẢN XUẤT (phiếu) + 7 cờ công đoạn → kế hoạch từng máy theo ngày (STT)
 → Tổ sóng → Tổ in → Tổ thành phẩm (bế / bồi / dán / đóng kim) → KCS → phiếu nhận dạng pallet → kho thành phẩm → giao (3–5 ngày sau duyệt mẫu)
```

- **7 cờ công đoạn** trên kế hoạch: Sóng · In · Bế · Bồi · Dán · Đóng kim · Khác — 1 có, 0 không, trống = **chưa khai** (khác "không qua").
- Phòng Kế hoạch quản cả **kho vật tư & thành phẩm, kho giấy** [MP-HSNL] — kế hoạch máy gắn chặt với tồn giấy.
- Mã đã có **khuôn bế + bản in** thì đơn bổ sung không phải chuẩn bị lại → nhanh hơn nhiều; cần gấp thì báo trước để xếp lịch.

## 2. Kế hoạch từng máy

- Mỗi máy một danh sách đơn **theo ngày**, xếp bằng **STT**. Đơn có STT = 0 không vào thứ tự chạy.
- Thứ tự hiển thị cho thợ: **Đang chạy** → **Còn phải làm** (chờ, trạng thái lạ) → **Hoàn thành**; trong nhóm xếp theo STT.
- **Chỉ một đơn "đang chạy"** cùng máy cùng ngày (trừ tổ sóng: ba đơn có thể ở ba trạm).
- Văn phòng thêm/đổi đơn: đơn đã chạy và đang chạy **giữ chỗ**; còn lại theo STT kế hoạch (luật tổ sóng 13/10/2026; tổ sóng có thêm luật ghép đơn).
- Đơn có ghi chú chứa chữ **"mới"** = **hàng mới**, phải chạy mẫu trước; thời gian chạy mẫu là **ngừng có kế hoạch**, không phải lỗi thợ.
- Đơn có ghi chú **"hàng mẫu"** → quãng máy đứng tính **ngừng có kế hoạch**.

## 3. Trạng thái và lưu đơn

| Trạng thái | Nghĩa |
|---|---|
| Chờ | Còn phải làm |
| Đang chạy | Đã chọn chạy trên máy |
| Hoàn thành | Đã lưu đơn |
| Dở dang | Chỉ qua **Chuyển ngày** (hoặc lượt In của đơn cán màng) |

- **Lưu đơn = xong đơn** dù thiếu số (chốt 27/08/2026). Lưu hỏng (mất mạng) thì số liệu cả ca **còn nguyên** trên màn hình — sửa mạng rồi lưu lại.
- Cách lưu theo loại máy (MES 2.0):
  - **Máy in**: đủ số mà máy đứng yên → hộp đếm ngược **90 giây** rồi tự lưu; bấm **Lưu đơn** → hộp xác nhận sản lượng, lỗi, giờ chạy, giờ ngừng.
  - **Thành phẩm** (dán, bế, bồi): **không tự lưu** — đủ số vẫn phải Tạm dừng, đếm lại, ghi lỗi rồi bấm Lưu đơn (lưu ngay).
  - **Tổ sóng**: dao chặt đủ số dao là **dao tự chốt** đơn và đưa đơn kế vào dao; tổ trưởng sau đó **xác nhận số tấm thực**.
- Chống ghi trùng: cùng lệnh, cùng máy, cùng ngày, cùng giờ bắt đầu thì không ghi lần hai.

## 4. Chuyển ngày, Ngưng đơn, vắt đêm

| Tình huống | Làm gì | Kết quả |
|---|---|---|
| Hết giờ, đơn đang chạy dở | **Chuyển ngày → Chỉ đơn đang chạy** | Lưu nhật ký dở dang hôm nay; đơn lên đầu ngày mai |
| Hết giờ, còn cả loạt đơn | **Chuyển ngày → Cả N đơn chưa xong** | Lưu đơn đang chạy + dời cả loạt sang mai, giữ thứ tự |
| Máy TP phải dừng đơn giữa chừng để chạy đơn khác (gấp, thiếu phôi…) | **Ngưng đơn** → chọn *chạy tiếp hôm nay* hoặc *mai mới chạy*; khai máy làm gì từ giờ tới đơn kế (chạy đơn khác / máy nghỉ / máy hỏng) | Hôm nay chạy tiếp = **một bản ghi**, ghi chú "Chạy 2 lần: 07:30-09:10, 13:00-15:00"; mai = dở dang, kế hoạch giữ nguyên số |
| Quên chốt đơn ngưng / đóng phần mềm khi đơn dở | Sáng hôm sau phần mềm **hỏi một lần**: lưu bù + chạy tiếp / lưu bù đơn đã xong / để sau | Bản ghi mang ngày hôm đó, ghi chú "Lưu bù sáng …" |
| Tổ sóng chạy qua nửa đêm | Đợi dao chặt xong đơn dở rồi mới sang kế hoạch ngày mới | Nhật ký đơn vắt đêm ghi **ngày bắt đầu đơn** |

Nút mặc định của Chuyển ngày là đường **hẹp** (chỉ một đơn) — bấm nhầm thì dời ít, sửa được.

## 5. Chuyển máy — đơn chạy được ở đâu

| Cặp | Chuyển được? | Vì sao |
|---|---|---|
| Máy In 1 ↔ Máy In 2 | **Có** | Cùng công đoạn In, cùng bảng in flexo |
| Máy In Offset ↔ flexo | Không | Bản kẽm ≠ bản flexo |
| Máy dán 1 ↔ Máy dán 2 | **Có** | Cùng công đoạn Dán |
| Máy bế 1 ↔ Máy bế 2 | **Có** | Cùng công đoạn Bế (hướng dẫn MES 2.0, 10/2026) |
| Máy dán ↔ máy bế | Không | Khác công đoạn (Dán ≠ Bế phẳng) |
| Máy bồi ↔ máy khác | Không | |

Chỉ chuyển **đơn chưa chạy**; vận hành bấm được.

Thêm cặp chuyển máy là việc **phải hỏi xưởng**, không suy ra từ việc hai máy dùng chung bảng dữ liệu.

## 6. Đơn đặc biệt

- **In 2 mặt**: in mặt 1 cả chồng → lật → mặt 2 cùng số tờ → một bản ghi; lật mặt là chuẩn bị (skill `mp-in-flexo`).
- **Cán màng**: máy in in → cán màng → quay lại máy in cắt rãnh; một dòng kế hoạch, giờ hai lượt tách riêng.
- **Đơn gấp** thêm ngay tại máy: **KCS trở lên** (tổ sóng: vận hành); đơn mới luôn ở trạng thái **Chờ** (thêm đơn không phải ra lệnh chạy —
  thợ vẫn phải tích chọn); ghi chú tự gắn "Thêm tại máy — người, giờ" để văn phòng đối chiếu; một phiếu chạy nhiều đợt trong ngày là bình thường.
  Sửa đơn (số lượng, số con, màu, ghi chú): **Quản lý trở lên** (tổ sóng: vận hành); khách, tên hàng, mã hàng sửa trên ERP.
- **Quên Chuyển ngày** hôm qua: ĐƠN HÀNG → **Lấy đơn ngày khác** → chọn ngày → tích đơn (máy in; thành phẩm có từ bản 15/10/2026).
