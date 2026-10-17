# Sản phẩm Minh Phúc

## 1. Dòng sản phẩm [MP-Web][MP-HSNL]

| Sản phẩm | Cấu tạo / mã | Sóng | In | Đường đi qua xưởng | Lưu ý kỹ thuật |
|---|---|---|---|---|---|
| Thùng carton 3 lớp | 0201 chủ yếu | B, C, E | Flexo 1–5 màu | Sóng → in (lằn, xẻ rãnh) → dán | Hàng nhẹ, FMCG |
| Thùng carton 5 lớp | 0201 | BC, BE | Flexo | Sóng → in → dán | Hàng nặng, pallet, xuất khẩu, đông lạnh |
| Thùng nắp gài RSC | 0201 | 3/5 lớp | Flexo | Sóng → in → (bế) → dán | Sản phẩm chủ lực |
| Thùng nắp rời | 03xx | 3/5 lớp | Flexo / offset | Sóng → in → bế → (dán) | Nắp phải bù độ dày để chụp khít |
| Hộp âm dương | 03xx | 3 lớp / bồi / duplex | Offset / flexo | … → bế phẳng | Dung sai bế chặt; thường bế phẳng |
| Vách ngăn, vỉ lót | 09xx | 3 lớp | — | Sóng → xẻ rãnh/bế | Rãnh rộng hơn độ dày tấm |
| Giấy tấm carton | 01 | A, B, C, E, BC | — | Sóng → chặt tấm | Ghi kích thước + hướng sóng; cắt khớp khổ máy |
| Hộp giấy in offset | 04xx / 03xx | E (bồi) hoặc giấy bìa | Offset 5 màu + gia công | Xén → in offset → cán màng → bồi → bế → dán | Một tờ in nhiều hộp (MP-046) |
| Thùng in offset / in process | 0201 | — | Offset bồi hoặc flexo process | Offset → bồi lên tấm sóng → bế/dán | Thùng nhiều màu (nước giải khát) |
| Túi giấy có quai, hộp quà | — | — | Offset | Xưởng offset | Quà Tết, trang sức, gia vị |
| Hộp tiếp xúc thực phẩm | 04xx | — | — | — | Hộp gà rán, burger; skill `mp-fsc-iso-attp` |

Gia công bề mặt xưởng offset [MP-HSNL tr. 26]: UV bóng / mờ / satin / định hình · phủ Varnish, OPV · cán màng OPP/PE 1 hoặc 2 mặt ·
tráng metalize · ép kim · dập nổi · đóng mắt cáo · túi giấy có quai.

**Không làm**: thùng 7 lớp; túi chống tĩnh điện, túi chắn ẩm, gói hút ẩm.

## 2. Bốn nhóm mã MES theo cách đếm (để đọc số sản lượng)

| Đơn vị sản phẩm | Ở đâu |
|---|---|
| **tấm** | tổ sóng, máy in flexo (tấm = nhịp × số con), máy bồi |
| **tờ** | máy in offset |
| **con** | máy bế (con = nhịp × số con) |
| **thùng** | máy dán |

"Số con" = số sản phẩm ra từ một nhịp (một tấm in hai con, khuôn bế 3 con…). [MP-MES]

## 3. 45 mẫu đã sản xuất (catalog web, MP-001 … MP-046, không có MP-005)

Dữ liệu đủ ở `data/mau-san-pham.json` (mã, tên, loại, kiểu in, ngành, ghi chú). Tóm tắt theo loại:

| Loại | Mẫu | Điểm kỹ thuật đáng nhớ |
|---|---|---|
| Thùng carton thường (RSC) | MP-001 … 015, 020, 030, 031, 036, 039, 045 | Kraft in 1–2 màu (MP-001, 008, 012, 013); phủ nền màu kín mặt thùng (MP-003, 004, 006) — in nền đặc dễ lộ sọc, bóng mực, phải canh độ nhớt; in nhiều màu trực tiếp trên kraft (MP-007, 015) — màu trầm hơn trên giấy trắng, duyệt trên mẫu thật; 5 lớp xuất khẩu (MP-031, 039); thùng in offset bồi (MP-036); giao gấp phẳng buộc kiện trên pallet (MP-045) |
| Hộp, thùng nắp gài | MP-025, 027, 038, 042 | Nắp gài không cần băng keo (MP-025); hộp gửi hàng TMĐT (MP-042); có quai (MP-038) |
| Hộp giấy in offset | MP-016 … 018, 021 … 024, 026, 028, 029, 035, 046 | Chữ nước ngoài (Anh, Nhật) cho hàng xuất khẩu — soát nội dung bản kỹ; cán màng (MP-023, 026); cửa sổ/ô khoét (MP-021, 024) |
| Hộp âm dương | MP-032, 041 | Nắp chụp úp lên thân; bản vẽ trải nắp – đáy (MP-041) |
| Thùng nắp rời | MP-034, 040 | Nắp tách rời |
| Hộp quà, túi giấy | MP-019, 033, 037, 043 | Túi quai dây; hộp quà có nơ; hộp có quai xách; hộp nắp rời bồi giấy in có khay (MP-043) |
| Giấy tấm | MP-044 | Tấm 3, 5 lớp cắt theo khổ yêu cầu |

Khách hàng thật gắn với mẫu: skill `mp-cong-ty` → `khach-hang-nganh-hang.md`.
