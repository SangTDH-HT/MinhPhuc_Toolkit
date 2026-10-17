# Chỉ số hiệu suất theo định nghĩa Minh Phúc

## 1. OEE (hiệu suất) = Sẵn sàng × Hiệu năng × Chất lượng [MP-MES]

```
SẴN SÀNG    = chạy máy ÷ thời gian tổ máy làm chủ                  (máy có được chạy không)
HIỆU NĂNG   = (số nhịp ÷ chạy máy) ÷ tốc độ mục tiêu               (chạy có nhanh không)
CHẤT LƯỢNG  = (sản lượng − lỗi) ÷ sản lượng                         (ra có dùng được không)

Thời gian tổ máy làm chủ = pha mực + chạy máy + ngừng không kế hoạch   (máy in)
                           chạy máy + ngừng không kế hoạch              (thành phẩm, sóng)
```

- **Sẵn sàng × Hiệu năng = tốc độ bình quân ÷ mục tiêu** — trùng đúng con số "đạt / chưa đạt" trên bảng tốc độ (cố ý, để không có hai thước đo nói ngược nhau).
- Ngừng có kế hoạch, bảo trì, nghỉ ca **đứng ngoài** — tổ máy không quyết được.
- Phải bày **cả ba thành phần**, không chỉ cái tích: tổ chạy nhanh mà hỏng nhiều và tổ chạy chậm mà sạch có thể ra cùng một số.
- **Gộp nhiều đơn/ngày: cộng tử rồi chia** (cộng hết phút, nhịp, lỗi rồi mới chia), không lấy trung bình các tỷ lệ — một đơn 10 phút không được kéo cả tuần.
- Tốc độ mục tiêu đặt trong Cài đặt từng trạm (Quản lý trở lên); số đang cài là **mặc định của phần mềm**, chưa phải định mức đã duyệt — cần chốt định mức
  theo máy và loại đơn (`docs/LO-TRINH.md`).

Ví dụ một ngày Máy In 1: pha mực 60, chạy 300, KOKH 60 phút; 18.000 nhịp; mục tiêu 70 nhịp/phút; sản lượng 18.000 tờ, lỗi 180.
→ Sẵn sàng = 300/420 = 71,4 % · Hiệu năng = (18.000/300)/70 = 85,7 % · Chất lượng = 99,0 % · **OEE ≈ 60,6 %**.
Tốc độ bình quân = 18.000/420 = 42,9 nhịp/phút = 61,2 % mục tiêu (= 71,4 % × 85,7 %). Máy tính: `python -m mptinh oee`.

## 2. Đọc OEE để hành động

| Thành phần thấp | Nhìn vào | Hành động |
|---|---|---|
| Sẵn sàng | KOKH lớn (dừng vặt, chờ giấy, chờ bản, kẹt), pha mực lâu | Pareto lý do dừng; SMED cho đổi đơn; bảo trì phòng ngừa |
| Hiệu năng | Tốc độ lúc chạy thấp so mục tiêu | Tấm cong (phải giảm tốc), giấy dày, thợ mới, máy rung; mục tiêu đặt sai |
| Chất lượng | Tổng lỗi, "Lỗi khác" | Pareto mã lỗi; kiểm đầu đơn |

Cảnh báo sớm trên MES liên quan: **tốc độ đang tụt** (SX-21), **máy dừng vặt liên tục** (SX-22), **máy đứng chưa khai lý do** (SX-01).

## 3. Chỉ số khác nên theo dõi [KN ngành]

| Chỉ số | Công thức | Ghi chú |
|---|---|---|
| Thời gian đổi đơn | Từ lúc máy đứng ở đơn trước tới tấm đạt đầu tiên đơn sau | MES: pha mực/chuẩn bị đầu đơn; mục tiêu giảm bằng SMED |
| Tỷ lệ hư thật | (nhóm 1 + 2 + 3 + 7 của Lỗi khác + các ô lỗi) ÷ sản lượng | Theo máy, theo tuần |
| Hao hụt giấy tổ sóng | (giấy vào − tấm đạt quy ra m²) ÷ giấy vào | Gồm biên xén, đầu cuộn, chuyển đơn, lỗi |
| m² bao bì đạt / ngày | Σ tấm đạt × diện tích tấm | Đơn vị so sánh chung giữa các máy |
| Đúng hạn giao | Đơn giao đúng ngày ÷ tổng đơn | |
| Kế hoạch vs thực | Sản lượng thực ÷ kế hoạch theo máy/ngày | |
| Sức khoẻ dữ liệu | % bản ghi sạch (không thiếu lý do, không sửa tay muộn) | MES có ngăn "Sức khoẻ dữ liệu" ở máy Giám sát |

## 4. Báo cáo định kỳ gợi ý

- **Hằng ngày** (tổ trưởng): sản lượng, tốc độ, KOKH lớn nhất và lý do, lỗi lớn nhất, đơn chuyển ngày.
- **Hằng tuần** (quản đốc): OEE từng máy (ba thành phần), Pareto lỗi, Pareto dừng máy, Lỗi khác theo 7 nhóm.
- **Hằng tháng** (ban giám đốc): xu hướng OEE, m² đạt, hao hụt giấy, khiếu nại, dự án cải tiến (skill `mp-cai-tien`).
