---
name: mp-ho-tro-kinh-doanh
description: >
  Hỗ trợ kỹ thuật cho kinh doanh, chăm sóc khách hàng và thiết kế ở Minh Phúc: thu đủ thông tin khách (5 thông tin đặt lần đầu), tư vấn kết cấu – sóng – giấy –
  cách in (flexo hay offset), yếu tố làm nên giá thùng, ước diện tích và khối lượng giấy cho báo giá, làm mẫu in kỹ thuật số và duyệt mẫu, chuyển yêu cầu
  khách thành lệnh sản xuất và hồ sơ quy cách mã hàng, trả lời câu hỏi kỹ thuật của khách (BCT, Cobb, FSC, xuất khẩu), xử lý khiếu nại phía khách,
  các sai lầm khách hay gặp. Dùng khi kinh doanh cần trả lời khách nhanh và đúng kỹ thuật, khi lập báo giá, khi chuyển đơn mới vào sản xuất.
---

# mp-ho-tro-kinh-doanh — trả lời khách nhanh mà không hứa sai

Cam kết công khai của Minh Phúc: **báo giá trong 4 giờ làm việc · mẫu 1–3 ngày · hàng loạt 3–5 ngày sau duyệt mẫu** · có hoá đơn VAT. [MP-Web]
Không có bảng giá cố định — giá theo quy cách.

## Bảng tham chiếu

| Cần gì | Đọc |
|---|---|
| Hỏi khách gì; chọn kết cấu, giấy, cách in; câu trả lời mẫu cho câu hỏi hay gặp | [references/tu-van-khach-hang.md](references/tu-van-khach-hang.md) |
| Giá thùng phụ thuộc gì; ước diện tích, khối lượng giấy, số tờ in/khổ để báo giá | [references/bao-gia-ky-thuat.md](references/bao-gia-ky-thuat.md) |
| Mẫu, duyệt mẫu, chuyển đơn mới vào sản xuất, hồ sơ quy cách mã hàng, khiếu nại | [references/mau-va-chuyen-don.md](references/mau-va-chuyen-don.md) |
| Chọn kết cấu chi tiết, BCT | skill `mp-san-pham-ket-cau` |
| Khách theo ngành, 45 mẫu đã làm | skill `mp-cong-ty`, `data/mau-san-pham.json` |

## Năm điều không hứa

1. Không hứa **con số BCT/ECT** từ công thức — chỉ hứa sau khi **đo mẫu thật**.
2. Không nhận **thùng 7 lớp**, túi ESD, túi chắn ẩm, gói hút ẩm (Minh Phúc không làm).
3. Không hứa **màu giống hệt màn hình** — duyệt màu trên mẫu thật; giấy kraft cho màu trầm hơn giấy trắng.
4. Không hứa in **logo FSC** khi đơn không dùng giấy FSC hoặc nhãn chưa được duyệt.
5. Không nhận **hộp tiếp xúc thực phẩm** mà chưa rõ món đựng và chưa có hồ sơ vật tư phù hợp.
