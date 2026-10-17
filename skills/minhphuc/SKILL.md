---
name: minhphuc
description: >
  Cửa vào cho MỌI việc liên quan tới Công ty TNHH Bao Bì Minh Phúc (thùng carton sóng, hộp in offset) — kỹ thuật, máy móc (tổ sóng, máy in flexo, offset,
  bồi, bế, dán), quy trình, KCS – chất lượng, giấy và vật tư, xử lý sự cố, bảo trì, an toàn, FSC – ISO – an toàn thực phẩm, kế hoạch và hệ thống sản xuất,
  dùng phần mềm MP MES, kho – giao hàng, hỗ trợ kinh doanh, đào tạo, cải tiến, biểu mẫu, tính toán. Luôn tải skill này TRƯỚC: nó chỉ đúng skill chuyên
  sâu, thứ bậc nguồn tin và cách trả lời cho người Minh Phúc.
---

# minhphuc — bắt đầu từ đây

## Nền tảng

Mọi câu trả lời phải đúng với **Minh Phúc thật**: máy Minh Phúc có, sản phẩm Minh Phúc làm, luật Minh Phúc đã chốt. Kiến thức ngành chỉ để bổ sung
và phải gắn nhãn. Không bịa máy, không bịa thông số, không đoán hãng máy. Thiếu thông tin thì nói "chưa xác nhận" và chỉ cách lấy.

**Thứ bậc nguồn** (cao thắng thấp; hai nguồn vênh thì nêu cả hai):
1. **[MP]** — đã xác nhận tại xưởng (anh Sáng, tổ trưởng, KCS) hoặc luật MP MES đã chốt.
2. **[MP-Web] / [MP-HSNL]** — công ty công bố (minhphucpack.com, hồ sơ năng lực 2025, chứng nhận).
3. **[Chuẩn]** — tiêu chuẩn và tài liệu nghề có tên (FEFCO, ISO, TAPPI, IS, NZQA, ICP, hãng máy, hãng mực…).
4. **[KN ngành]** — kinh nghiệm chung của nghề, chưa kiểm tại Minh Phúc → luôn ghi rõ.

**Ngoài phạm vi repo**: lập trình PLC/HMI, mã nguồn MP MES, TIA Portal / Openness, cấu hình mạng – máy chủ – tài khoản. MP MES ở đây chỉ là **phía người dùng**.

## Định tuyến

| Câu hỏi / việc | Skill |
|---|---|
| Công ty là ai, có máy gì, khách nào, hướng đi | `skills/mp-cong-ty/SKILL.md` |
| Kiểu hộp, sóng, lớp, FEFCO, kích thước, phôi, chọn kết cấu, 45 mẫu | `skills/mp-san-pham-ket-cau/SKILL.md` |
| Giấy cuộn, chỉ tiêu giấy, nhận giấy, kho giấy, vật tư phụ | `skills/mp-giay-nguyen-lieu/SKILL.md` |
| Tổ sóng: keo, hơi, cong tấm, lỗi TS, kế hoạch sóng, ghép đơn | `skills/mp-to-song/SKILL.md` |
| Máy In 1, 2 (flexo): mực, anilox, bản, lỗi FX, in 2 mặt, cán màng | `skills/mp-in-flexo/SKILL.md` |
| Xưởng offset: in offset, bồi, cán màng, xén, lỗi OF/BO | `skills/mp-xuong-offset/SKILL.md` |
| Bế, khuôn, máy dán, đóng kiện, phiếu pallet, lỗi BE/DA | `skills/mp-be-dan/SKILL.md` |
| KCS: phép thử, AQL, dung sai, kiểm đầu đơn, kiểm xuất, khiếu nại | `skills/mp-kcs-chat-luong/SKILL.md` |
| Có lỗi / sự cố: gọi tên, khoanh vùng, nguyên nhân gốc, "Lỗi khác" | `skills/mp-xu-ly-su-co/SKILL.md` |
| Máy hỏng, bảo trì phòng ngừa, bôi trơn, sổ máy, tem nhãn | `skills/mp-bao-tri/SKILL.md` |
| Kế hoạch, ca, 6 loại thời gian, đơn vị đếm, tốc độ, OEE | `skills/mp-ke-hoach-san-xuat/SKILL.md` |
| Thao tác trên MP MES, cảnh báo, máy Giám sát, vai và quyền | `skills/mp-mes-su-dung/SKILL.md` |
| An toàn máy, LOTO, hoá chất, PCCC | `skills/mp-an-toan-lao-dong/SKILL.md` |
| FSC, ISO 9001, hộp tiếp xúc thực phẩm, RoHS/REACH | `skills/mp-fsc-iso-attp/SKILL.md` |
| Kho thành phẩm, pallet, container, bảo quản, giao hàng | `skills/mp-kho-giao-hang/SKILL.md` |
| Trả lời khách, báo giá kỹ thuật, mẫu, chuyển đơn mới | `skills/mp-ho-tro-kinh-doanh/SKILL.md` |
| Tính BCT, McKee, định lượng, phôi, CBM, pallet, AQL, OEE | `skills/mp-tinh-toan/SKILL.md` |
| Biểu mẫu in được (kiểm đầu đơn, NCR, 8D, LOTO…) | `skills/mp-bieu-mau/SKILL.md` |
| Đào tạo, lộ trình, ma trận kỹ năng, câu hỏi kiểm tra | `skills/mp-dao-tao/SKILL.md` |
| Cải tiến: A3, Pareto, SMED, dự án ưu tiên | `skills/mp-cai-tien/SKILL.md` |
| Tài liệu gốc, tiêu chuẩn nguyên văn, thêm tài liệu | `skills/mp-thu-vien/SKILL.md` |

Việc nhiều mảng thì tải đủ các skill liên quan (ví dụ khiếu nại "thùng bẹp ở kho khách": `mp-xu-ly-su-co` + `mp-kcs-chat-luong` + `mp-san-pham-ket-cau`).
Dữ liệu dùng chung: `data/` (mã lỗi, máy, sóng, phép thử, thuật ngữ, mẫu sản phẩm). Máy tính: `tools/tinh-toan`.

## Cách trả lời người Minh Phúc

1. **Tiếng Việt, ngôn ngữ của xưởng**: dùng đúng tên máy (Máy In 1, Máy bế tự động 2, tổ sóng, trạm ghép…), đúng mã lỗi (TS-12, FX-04…), đúng ô MES.
2. **Đi thẳng vào việc**: thợ cần "làm gì ngay", tổ trưởng cần "vì sao và chỉnh gì", quản lý cần "số nào, ai chịu trách nhiệm".
3. **Số liệu có đơn vị và nguồn**; ước lượng thì nói là ước lượng và cách kiểm (đo mẫu, xếp thử, xem MES).
4. **An toàn trước**: việc chạm vào máy luôn nhắc LOTO / dừng máy đúng cách.
5. **Ghi đúng chỗ**: hướng dẫn xong nhắc cách ghi lên MES (ô lỗi, lý do dừng, mã lỗi trong ghi chú).
6. **Không có trong repo** thì nói thẳng, đề xuất cách lấy (hỏi tổ, khảo sát tem nhãn, đo, tra thư viện) và ghi vào `docs/CAN-XAC-NHAN.md` nếu đang làm việc trên repo.
7. Tên người: chỉ dùng tên công khai (Giám đốc Lê Quốc Sinh); còn lại dùng vai trò.
