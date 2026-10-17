# Sáu nhóm nguyên nhân — mỗi nhóm một người chịu trách nhiệm

Nguồn: đề xuất "Lỗi khác — 6 ô theo nguyên nhân, dùng chung cho mọi máy" của xưởng (17/10/2026) [MP]. Đề xuất ban đầu cho phần mềm; dùng được ngay
như **khung phân tích nguyên nhân** (thay cho 6M) vì mỗi nhóm có người sửa — nhìn số là biết ai cần vào cuộc.

## 1. Sáu nhóm

| Nhóm | Gồm những gì | Hỏi nhanh để chọn nhóm | Ai xử lý |
|---|---|---|---|
| **1. NVL** | Nguyên liệu mua về (giấy, keo, mực, màng, dây đai) kém hoặc sai loại: chưa vào máy đã không đạt. Máy chỉnh đúng, thợ làm đúng vẫn hư | Đổi cuộn / lô khác là hết lỗi? | Kho, mua hàng |
| **2. Máy móc – khuôn bản** | Máy, khuôn bế, bản in, dao, cao su mòn, hỏng, kẹt, bẩn; rò dầu, cảm biến sai, nhiệt không lên: chỉnh đúng mà máy không giữ được | Phải sửa hoặc thay phụ tùng máy, khuôn, bản mới hết? | Bảo trì; tổ khuôn bản |
| **3. Vận hành** | Người đứng máy chỉnh, canh, pha, thao tác sai hoặc bỏ bước kiểm tờ đầu | Chỉnh lại, làm lại đúng cách là hết? | Tổ trưởng máy |
| **4. Khâu trước** | Bán thành phẩm do công đoạn trước làm ra, nhận về đã hư sẵn. Máy đã có ô Sóng / In / Bế thì ghi ô đó như cũ; nhóm này cho phần còn lại (lỗi bồi, hoặc không rõ khâu nào) | Nhận về máy đã hư sẵn? | Tổ khâu trước; KCS |
| **5. Kỹ thuật – kế hoạch** | Thợ làm đúng phiếu nhưng **phiếu sai**: lệnh SX, thông số, mẫu duyệt, nội dung bản, mã khuôn, lẫn đơn | Phải sửa phiếu, mẫu, file thiết kế mới hết? | Phòng kỹ thuật, kế hoạch |
| **6. Kho – vận chuyển** | Ra khỏi máy còn tốt, hư sau đó: khi chờ, khi chở, khi xếp (ẩm mưa, xe nâng, ngã pallet, chồng quá cao) | Hàng rời máy còn tốt, hư lúc sau? | Kho, vận chuyển |

**Không** thuộc 6 nhóm: tờ thử, tấm canh máy, tấm chuyển đơn → hao hụt kỹ thuật (máy in: ô Thử máy) · tồn trước máy, chênh do cách đếm, KCS lấy mẫu →
không phải lỗi.

**Phân vân giữa hai nhóm** thì hỏi: *"Muốn lỗi này không lặp lại thì phải sửa cái gì?"*

## 2. Ví dụ theo từng máy

| Nhóm | Tổ sóng | Máy In 1, 2 (flexo) | Máy In Offset | Máy bồi | Máy bế 1, 2 | Máy dán 1, 2 |
|---|---|---|---|---|---|---|
| 1. NVL | Giấy cuộn ẩm, rách mép · keo kém, loãng · giấy khác màu, sai định lượng từ nhà cung cấp | Mực kém, khác lô | Giấy cong, nhăn, co giãn · mực khác lô | Keo kém, sai loại keo | — (chỉ nhận tấm từ khâu trước) | Keo kém, khô quá nhanh · dây đai kém |
| 2. Máy móc – khuôn bản | Trục sóng mòn → sóng nghiêng, cao thấp · dao cùn → mép xơ · rò dầu · bàn sấy không đủ nhiệt | Anilox, dao gạt mòn → chấm mực, sọc · sấy yếu · bàn nạp kẹt tấm · bản bẩn, mòn → ăn bông, mất nét | Lô mực, lô nước mòn → sọc · cao su lỏng → bóng ma · đầu hút → nạp đôi · bản mòn, trầy | Trục keo không đều → hở mép · trục ép mòn → phồng rộp | Đầu hút → nạp đôi · bàn nạp kẹt tấm · khuôn hỏng, dao gãy · cao su bung · dao lỗ cùn → rác kẹt | Súng keo tắc · băng tải, thanh dẫn → móp góc · bàn nạp kẹt phôi |
| 3. Vận hành | Không cắt mối nối · cong vênh, nhăn do chỉnh nhiệt, lực căng · chạy nhanh → keo chưa chín · cắt xéo | Nhoè, mờ, thiếu mực do chỉnh mực, áp lực · pha sai màu · cài dao xẻ lệch rãnh · in ngược mặt | Đậm nhạt không đều · thiếu/dư nước · chồng giấy sớm → dính mặt sau · đốm bụi | Lệch bồi · keo tràn · ép quá tay → dập sóng · bồi ngược · xếp khi keo chưa khô | Áp lực quá cao → dập, hằn mặt in · chỉnh tách rác sai | Keo tràn · ép chưa đủ → bung mép · dính thùng · cột dây lỏng |
| 4. Khâu trước | — (đầu vào là giấy cuộn → NVL) | Tấm sóng cong, bong, sai khổ → **ô Sóng** có sẵn | — (giấy tờ rời → NVL) | Tấm sóng lỗi → ô Sóng, tờ in lỗi → ô In | Tấm bồi lệch, bong bồi · (sóng, in lỗi → ô Sóng / In) | Phôi bồi lệch, bong bồi · hư sẵn không rõ khâu · (sóng, in, bế lỗi → ô Sóng / In / Bế) |
| 5. Kỹ thuật – kế hoạch | Phiếu sai khổ, kết cấu, vị trí lằn · ghép đơn sai khổ | Sai nội dung bản (chữ, mã) · mẫu màu duyệt sai | Sai nội dung bản · sai tờ duyệt màu | Phiếu sai cặp tờ in – tấm sóng, sai chiều bồi | Lắp sai khuôn · phiếu ghi sai mã khuôn | Phiếu sai kiểu dán, sai số thùng mỗi bó |
| 6. Kho – vận chuyển | Tấm móp, gãy khi xếp chồng, xe nâng · tấm hút ẩm khi chờ | Trầy mặt in khi xếp, chở · tấm in để ẩm | Tờ in hút ẩm, cong khi chờ bồi · trầy khi chở | Cong vênh khi để chờ khô · trầy, bẩn khi chở | Gãy góc, móp khi chuyển sang dán | Ướt mưa, móp khi chở · ngã pallet |

## 3. Nối với xương cá (6M)

| 6M quen thuộc | Nhóm Minh Phúc |
|---|---|
| Material — vật liệu | 1. NVL (và 4. Khâu trước cho bán thành phẩm) |
| Machine — máy | 2. Máy móc – khuôn bản |
| Man — con người | 3. Vận hành |
| Method — phương pháp | 5. Kỹ thuật – kế hoạch (phiếu, thông số, mẫu) |
| Measurement — đo lường | chênh đếm (không phải lỗi) / thiết bị đo QC |
| Environment — môi trường | 6. Kho – vận chuyển (ẩm, mưa, chồng cao) |
