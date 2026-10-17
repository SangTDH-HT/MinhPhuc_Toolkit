---
name: mp-tinh-toan
description: >
  Máy tính kỹ thuật của repo (Python thuần, tools/tinh-toan, lệnh python -m mptinh): BCT yêu cầu S.F × (n − 1) × W, McKee BCT ↔ ECT,
  ECT từ SCT giấy (Maltenfort–Seth), ảnh hưởng độ ẩm, định lượng tấm theo cấu trúc giấy và hệ số co sóng, khoảng cách lằn và phôi thùng RSC 0201,
  diện tích và khối lượng thùng, CBM và số thùng trong container 20'/40'/40HC, số thùng mỗi lớp pallet, cỡ mẫu AQL, sản lượng theo luật MP MES
  (máy bế: nhịp × số con; máy in: tờ in; chạy trước), OEE theo định nghĩa Minh Phúc, số tấm trên khổ giấy và hao biên, Pareto từ CSV. Dùng khi cần một con số tính
  đúng công thức và đúng đơn vị — thay vì nhẩm.
---

# mp-tinh-toan — tính bằng máy, ghi rõ công thức

Mọi lệnh in kèm công thức và cảnh báo "định hướng"; **con số chốt là đo trên mẫu thật**. Công thức và nguồn: skill `mp-san-pham-ket-cau`
(kết cấu, McKee), `mp-kcs-chat-luong` (AQL), `mp-ke-hoach-san-xuat` (sản lượng, OEE), `mp-kho-giao-hang` (CBM, pallet).

## Chạy

```
cd tools/tinh-toan
python -m mptinh -h                 # danh sách lệnh
python -m mptinh <lệnh> -h          # tham số của lệnh
```
Cần Python ≥ 3.9, không cần cài thư viện. Kiểm tra: `python -m unittest discover -s tools/tinh-toan/tests` (từ gốc repo).

## Lệnh

| Lệnh | Tính gì | Ví dụ |
|---|---|---|
| `bct-can` | BCT yêu cầu (kgf), bù độ ẩm | `--sf 5 --tang 8 --kg 12 --rh 80` → 420 kgf; ở 80 % RH cần đo ≥ 600 kgf ở 50 % RH |
| `mckee` | BCT từ ECT, hoặc ECT cần cho BCT | `--dai 400 --rong 300 --song C --ect 5 --bct 420` → 224 kgf; cần ECT ≈ 9,38 kN/m |
| `ect` | ECT từ SCT giấy | `--mat 3.1/3.1 --song 2.2:1.43` |
| `do-am` | Hệ số sức nén theo RH, ẩm cân bằng giấy | `--rh 80` → ~70 %, ẩm ~11,4 % |
| `dinh-luong` | Định lượng tấm từ cấu trúc | `--cau-truc 150,120C,150` → ~474 g/m² (+ `--keo 10`) |
| `phoi-rsc` | Lằn, phôi, m², phủ bì, khối lượng thùng 0201 | `--dai 400 --rong 300 --cao 250 --song C --dinh-luong 480` → 1.451 × 562 mm, 0,815 m², ~391 g |
| `cbm` | CBM, số thùng container | `--dai 40 --rong 30 --cao 30` → 0,036 m³; 779 / 1.581 / 1.794 thùng |
| `pallet` | Thùng mỗi lớp, số lớp, tổng | `--dai 400 --rong 300 --pallet 1200x800 --cao 250 --cao-toi-da 1650` → 8/lớp, 6 lớp, 48 |
| `aql` | Cỡ mẫu, số chấp nhận | `--lo 20000 --aql 1.5` → 80 mẫu, Ac 3 |
| `san-luong` | Luật MES: nhịp thực hiện, sản lượng, thừa/thiếu (máy in: `--so-con 1`) | Máy bế 2 con: `--nhip 2750 --chay-truoc 250 --so-con 2 --ke-hoach 6000` → 6.000 con, đủ |
| `oee` | OEE Minh Phúc | `--chay 300 --kokh 60 --pha-muc 60 --nhip 18000 --muc-tieu 70 --san-luong 18000 --loi 180` → 60,6 % |
| `kho-giay` | Số tấm/khổ, hao biên | `--rong-tam 520 --kho 1600,1800 --bien 20` |
| `pareto` | Pareto từ CSV (cột `ma`, `so_luong`) | `--file phieu-dem.csv` |

## Khi trả lời người dùng

1. Hỏi đủ đầu vào (đơn vị!): mm hay cm; lọt lòng hay phủ bì; kg thùng đã đóng hàng; số tầng; RH kho.
2. Chạy lệnh, dán kết quả, **ghi công thức** và **giả định** (độ dày theo sóng, hệ số co, hệ số khai thác 85 %…).
3. Nói rõ cái gì là ước lượng; đề nghị đo mẫu (BCT, ECT) hoặc xếp thử một lớp (container).
4. Số liệu thật của xưởng (độ dày đo, hệ số co của trục sóng Minh Phúc, biên xén tối thiểu) có thì truyền vào thay mặc định.
