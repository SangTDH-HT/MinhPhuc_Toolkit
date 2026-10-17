# Nhận giấy cuộn và lưu kho

## 1. Nhận hàng

| Bước | Làm gì | Nguồn |
|---|---|---|
| 1 | Đối chiếu nhãn cuộn với phiếu giao: loại, định lượng, khổ, chiều máy, số lô, khối lượng | Chuẩn: IS 1397 |
| 2 | Kiểm ngoại quan từng cuộn: dập, ướt, méo, lõi bẹp, rách mép | Chuẩn: NZQA 40325 |
| 3 | Đơn FSC: kiểm khai báo FSC (loại tuyên bố, mã chứng nhận) trên **hoá đơn/phiếu giao**; dán nhãn lô FSC | Chuẩn: FSC-STD-40-004 |
| 4 | Lấy mẫu mỗi lô: định lượng, độ ẩm, RCT hoặc SCT, Cobb (và bục nếu khách đặt theo bục); so COA | KN ngành |
| 5 | Ghi kết quả theo số lô; lô không đạt → lập phiếu NCR, cách ly, báo mua hàng | KN ngành |

Biểu mẫu: `templates/phieu-kiem-tra-giay-cuon.md`. Bảng lấy mẫu theo lô (gợi ý): mỗi lô giao, mỗi nhà cung cấp, mỗi loại/định lượng
lấy tối thiểu 1 cuộn đầu, 1 cuộn giữa; cắt bỏ 3–5 vòng ngoài trước khi lấy mẫu. **[KN ngành]**

## 2. Lưu kho

- Cuộn để trên pallet hoặc sàn khô, **kê cao, bọc kín, che bạt**; không để sát nền ướt, không dưới mái dột (mã lỗi TS-01 "giấy cuộn ướt,
  ẩm": kê pallet, che bạt; đo ẩm trước khi lên máy). [MP — file mổ xẻ Lỗi khác]
- **Kẹp cuộn đúng lực, xếp cuộn đứng** (mã TS-02 "rách mép, móp cuộn" do kẹp mạnh, va đập khi vận chuyển). [MP]
- **Dán nhãn cuộn rõ** và soát kết cấu trước khi chạy (TS-03 "sai loại giấy / định lượng" do lấy nhầm cuộn). [MP]
- **Nhập trước xuất trước (FIFO)**. Cuộn mới nhập từ xe nóng ẩm nên để "nghỉ" cho cân bằng nhiệt – ẩm trước khi lên máy sóng; không để cuộn
  dưới mái tôn nóng. **[KN ngành]**
- Lô FSC để khu riêng hoặc dán nhãn phân biệt; không trộn với lô không FSC khi đơn yêu cầu FSC.
- Giấy offset (tờ rời): **ủ giấy trong xưởng** trước khi in để tránh cong, co giãn (OF-01, OF-02); giữ ẩm xưởng ổn định. [MP]

## 3. Trước khi lên máy

- Kiểm cuộn lần nữa: dập, ướt, méo, lõi bẹp, rách. [NZQA 40325]
- Soát **màu cuộn** khi nối (TS-05 "lẫn giấy khác màu" do nối nhầm cuộn khác màu). [MP]
- Đánh dấu và **cắt bỏ tấm có mối nối** (TS-04). [MP]
- Đo ẩm hai cuộn giấy mặt sẽ ghép với nhau; lệch nhiều thì báo trưởng ca để chỉnh nhiệt trước (chống cong). **[KN ngành]**

## 4. Khiếu nại nhà cung cấp

Gửi kèm: số lô/cuộn, ảnh nhãn cuộn, ảnh lỗi, số đo so với COA, số lượng ảnh hưởng (tấm hư theo phiếu MES), đề nghị (đổi, trừ tiền,
cải tiến). Theo dõi theo mẫu `templates/phieu-ncr.md`; lỗi lặp lại thì yêu cầu 8D từ nhà cung cấp.

## 5. Đánh giá nhà cung cấp (gợi ý chỉ số) [KN ngành]

Tỷ lệ lô đạt khi nhận · độ lệch định lượng trung bình · độ ổn định độ ẩm · số khiếu nại · giao đúng hạn · có COA mỗi lô · có FSC.
Đánh giá theo quý; đưa vào hồ sơ ISO 9001 (đánh giá nhà cung cấp — skill `mp-fsc-iso-attp`).
