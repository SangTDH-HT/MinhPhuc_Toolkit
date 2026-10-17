# mptinh — máy tính kỹ thuật Bao Bì Minh Phúc

Python thuần (≥ 3.9), không cần cài thêm gì.

```
cd tools/tinh-toan
python -m mptinh -h
python -m mptinh phoi-rsc --dai 400 --rong 300 --cao 250 --song C --dinh-luong 480
```

| Mô-đun | Nội dung |
|---|---|
| `mptinh/ket_cau.py` | Độ dày theo sóng, hệ số co, định lượng tấm, phôi RSC 0201 |
| `mptinh/do_ben.py` | BCT yêu cầu, McKee, Maltenfort–Seth, độ ẩm |
| `mptinh/logistics.py` | CBM, container, xe, pallet |
| `mptinh/chat_luong.py` | Bảng AQL (FEFCO / ISO 2859-1) |
| `mptinh/san_xuat.py` | Sản lượng theo luật MES, OEE, khổ giấy, Pareto |
| `mptinh/__main__.py` | Dòng lệnh, in số kiểu Việt Nam (1.234,5) |

Kiểm tra (từ gốc repo): `python -m unittest discover -s tools/tinh-toan/tests` — mọi ví dụ trong sổ tay và web Minh Phúc có test.

Thêm công thức mới: viết hàm có docstring ghi **nguồn**, thêm lệnh vào `__main__.py`, thêm test bằng một ví dụ có số kiểm được, cập nhật bảng lệnh trong
`skills/mp-tinh-toan/SKILL.md`.
