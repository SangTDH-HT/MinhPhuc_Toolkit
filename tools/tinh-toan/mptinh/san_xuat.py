"""Sản xuất: sản lượng theo luật MP MES, OEE theo định nghĩa Minh Phúc, khổ giấy, Pareto."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class KetQuaSanLuong:
    nhip_thuc_hien: float
    san_luong: float
    thua_thieu: float | None
    dat: float | None


def san_luong(nhip: float, chay_truoc: float = 0.0, so_con: float = 1.0,
              ke_hoach: float | None = None, loi: float = 0.0) -> KetQuaSanLuong:
    """Luật MP MES: số nhịp thực hiện = nhịp máy + chạy trước (đều là NHỊP);
    sản lượng = số nhịp thực hiện × số con — nhân MỘT lần ở bước cuối.
    Thừa/thiếu so với KẾ HOẠCH của máy (số máy sẽ chạy), không so số lượng đơn hàng.
    """
    if so_con <= 0:
        raise ValueError("Số con phải > 0")
    n = nhip + chay_truoc
    sl = n * so_con
    tt = sl - ke_hoach if ke_hoach is not None else None
    return KetQuaSanLuong(n, sl, tt, sl - loi)


@dataclass
class KetQuaOEE:
    san_sang: float
    hieu_nang: float
    chat_luong: float
    oee: float
    toc_do_binh_quan: float
    thoi_gian_lam_chu: float


def oee(chay: float, kokh: float, nhip: float, muc_tieu: float, san_luong_: float, loi: float,
        pha_muc: float = 0.0) -> KetQuaOEE:
    """OEE theo MP MES: Sẵn sàng × Hiệu năng × Chất lượng.

    Thời gian tổ máy làm chủ = pha mực + chạy + ngừng không kế hoạch (máy thành phẩm, sóng: pha_muc = 0).
    Sẵn sàng = chạy ÷ làm chủ; Hiệu năng = (nhịp ÷ chạy) ÷ mục tiêu; Chất lượng = (SL − lỗi) ÷ SL.
    Gộp nhiều đơn: CỘNG các phút, nhịp, sản lượng, lỗi rồi mới gọi hàm (không trung bình tỷ lệ).
    """
    lam_chu = pha_muc + chay + kokh
    if lam_chu <= 0 or chay <= 0 or muc_tieu <= 0 or san_luong_ <= 0:
        raise ValueError("Thời gian, mục tiêu, sản lượng phải > 0")
    a = chay / lam_chu
    p = (nhip / chay) / muc_tieu
    q = (san_luong_ - loi) / san_luong_
    return KetQuaOEE(a, p, q, a * p * q, nhip / lam_chu, lam_chu)


@dataclass
class KetQuaKho:
    kho: float
    so_tam: int
    rong_dung: float
    bien: float
    hao_bien_pct: float
    dat: bool


def kho_giay(rong_tam: float, kho: float, so_tam: int | None = None, bien_toi_thieu: float = 0.0) -> KetQuaKho:
    """Số tấm trên một khổ và hao biên (mm). so_tam None → lấy tối đa vừa khổ.

    Biên xén tối thiểu của dây chuyền Minh Phúc chưa có — truyền vào khi biết.
    """
    if rong_tam <= 0 or kho <= 0:
        raise ValueError("Kích thước phải > 0")
    if so_tam is None:
        so_tam = int((kho - bien_toi_thieu) // rong_tam)
    rong_dung = so_tam * rong_tam
    bien = kho - rong_dung
    return KetQuaKho(kho, so_tam, rong_dung, bien, bien / kho * 100, so_tam > 0 and bien >= bien_toi_thieu)


def pareto(muc: dict[str, float]) -> list[tuple[str, float, float, float]]:
    """[(mục, số, %, % tích luỹ)] xếp giảm dần."""
    tong = sum(muc.values())
    if tong <= 0:
        raise ValueError("Tổng phải > 0")
    out, cong = [], 0.0
    for k, v in sorted(muc.items(), key=lambda kv: kv[1], reverse=True):
        cong += v
        out.append((k, v, v / tong * 100, cong / tong * 100))
    return out


def doc_csv_pareto(duong_dan: str | Path, cot_ma: str = "ma", cot_so: str = "so_luong") -> dict[str, float]:
    """Đọc CSV có cột mã và số lượng (UTF-8), cộng dồn theo mã."""
    gom: dict[str, float] = {}
    with open(duong_dan, encoding="utf-8-sig", newline="") as f:
        for dong in csv.DictReader(f):
            ma = (dong.get(cot_ma) or "").strip()
            so = (dong.get(cot_so) or "0").strip().replace(".", "").replace(",", ".")
            if ma:
                gom[ma] = gom.get(ma, 0.0) + float(so or 0)
    return gom
