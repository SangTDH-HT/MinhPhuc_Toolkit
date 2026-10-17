# Kích thước, khoảng cách lằn, phôi và mối nối

## 1. Quy ước kích thước

- Kích thước đặt hàng là **kích thước trong (lọt lòng)**, mm, thứ tự **Dài × Rộng × Cao**: Dài = cạnh dài của miệng thùng,
  Rộng = cạnh ngắn của miệng, Cao = từ miệng xuống đáy. [Chuẩn: FEFCO; IS 2771-1 mục 6.1]
- **Phủ bì (lòng ngoài)** lớn hơn lọt lòng theo độ dày vách; dùng để xếp pallet, container, tính CBM. Khách báo lọt lòng
  theo hàng cần đóng, nhà máy quy ra phủ bì theo kết cấu giấy. [MP-Web]
- Khách đo hàng rồi **cộng dung sai vài mm mỗi chiều** để hàng vào – ra dễ và có chỗ cho lớp lót. [MP-Web]
- Hộp telescope ghi thêm cao nắp sau dấu gạch chéo: **355 × 205 × 120/40 mm**. [Chuẩn: FEFCO]
- Đo ở khí hậu chuẩn, trên phôi phẳng, **từ tâm lằn tới tâm lằn**, có tính độ dày vật liệu. [Chuẩn: FEFCO]
- Kích thước tấm: chiều thứ nhất dọc đường keo (chiều máy), chiều thứ hai ngang đường keo. [Chuẩn: FEFCO]
- **Hướng sóng**: nếu không thoả thuận khác, sóng song song khe xẻ (sóng đứng khi dựng thùng). Giấy tấm: khách phải nói rõ
  cạnh nào song song sóng. [Chuẩn: FEFCO QC; MP-Web]

## 2. Khoảng cách lằn của thùng RSC 0201 [Chuẩn: FEFCO Quality Catalogue]

```
Lằn dọc thân:  (D + t)  ×  (R + t)          t = độ dày tấm
Lằn chiều cao: (C + 2t)
```

Ví dụ sóng B (t ≈ 3 mm), lọt lòng 650 × 400 × 250 → lằn **653 × 403 × 256 mm**; đo được trong ±4 / ±4 / ±3 mm là đạt
(dung sai FEFCO: ≤ 300 mm ±3; 300–700 mm ±4; 700–1.200 mm ±0,6 %).

## 3. Kích thước phôi RSC (tính nhanh) [KN ngành]

Dùng khi ước diện tích giấy, khối lượng thùng, báo giá sơ bộ. Không thay bảng bù kích thước của phòng thiết kế.

```
Chiều dài phôi  ≈ 2·(D + t) + 2·(R + t) + tai dán          tai dán ≈ 30–40 mm (IS 2771: chồng mép ≥ 30 mm)
Chiều rộng phôi ≈ (C + 2t) + 2 × nắp                     nắp ≈ (R + t) / 2   (nắp ngoài gặp nhau giữa miệng)
              ≈  C + R + 3t
Diện tích phôi (m²) = dài × rộng / 10⁶
Khối lượng thùng (g) ≈ diện tích phôi × định lượng tấm (g/m²)
```

Ví dụ: 400 × 300 × 250, sóng C (t = 4), tai dán 35 → dài ≈ 2·404 + 2·304 + 35 = 1.451 mm; rộng ≈ 250 + 300 + 12 = 562 mm;
diện tích ≈ 0,815 m²; tấm 3 lớp ~ 480 g/m² → thùng ≈ 391 g.
Máy tính: `python -m mptinh phoi-rsc --dai 400 --rong 300 --cao 250 --song C`.

Lưu ý khi ra kích thước phôi thật:
- Mỗi lằn ăn một phần vật liệu tuỳ sóng và dụng cụ cán lằn — phòng thiết kế có bảng bù riêng cho từng sóng (chưa có trong repo).
- Thùng nắp rời / âm dương: nắp phải **cộng bù độ dày** để chụp khít thân (nắp lớn hơn thân khoảng 2t mỗi chiều [KN ngành]).
- Vách ngăn: rãnh xẻ rộng hơn độ dày tấm để ghép không bung.
- Giấy tấm: cắt khớp khổ giấy chạy máy để ít hao — đây là chỗ Minh Phúc chủ động tối ưu khi báo giá. [MP-Web]

## 4. Mối nối nhà sản xuất (manufacturer's joint)

- Chỗ hai đầu phôi nối lại bằng keo, ghim hoặc băng. [Chuẩn: IS 2771-1 mục 3.1; FEFCO]
- Chồng mép **≥ 30 mm**; ghim cách nhau **≤ 60 mm**, ghim đầu/cuối cách mép **≤ 25 mm**; mối dán kín toàn diện tích;
  nối giáp mép dán băng rộng **≥ 50 mm**. [Chuẩn: IS 2771-1 mục 5.3]
- Mối nối có thể ở phần nối dài của tấm ngắn hoặc tấm dài — bản vẽ phải thể hiện rõ. [Chuẩn: FEFCO]
- Thử: kéo tay tách mối nối, phải **rách ở tấm** chứ không bung ở keo/ghim [IS 2771]; FEFCO đòi **≥ 80 %** diện tích keo còn xơ giấy.
- Khe hở mối dán (gap) chuẩn **6–8 mm**; sóng đơn −4/+4 mm, sóng đôi −4/+6 mm; lệch mép (đuôi cá) ≤ 0,5 % chiều cao phôi,
  tối thiểu 3 mm. [Chuẩn: FEFCO QC] — chi tiết kiểm ở skill `mp-kcs-chat-luong`.
- Thùng dán keo phẳng, đẹp, phổ biến; ghim kẽm chịu kéo tốt cho thùng cỡ lớn. [MP-Web]

## 5. Bản vẽ kết cấu (dieline)

- Bản vẽ phải có: kiểu hộp, kích thước lọt lòng, độ dày/sóng, vị trí lằn và khe, mối nối, hướng sóng (FD), mặt in.
- Một dieline gọn xếp được nhiều bản trên một tấm khổ lớn → giảm hao giấy; chỉnh vài mm có thể tăng số hộp mỗi tấm. [MP-Web]
- Phần mềm thiết kế đang dùng ở phòng Thiết kế (ArtiosCAD, EngView, Boxplan…?) — **chưa xác nhận**.
- Mẫu kỹ thuật số (máy in KTS) dùng để duyệt kết cấu và màu trước khi làm khuôn, bản. [MP-Web]
