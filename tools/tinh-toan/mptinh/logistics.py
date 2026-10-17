"""Logistics: CBM, số thùng trong container / xe, số thùng mỗi lớp pallet."""

from __future__ import annotations

from dataclasses import dataclass

# Thể tích lòng trong tham khảo (m³) — như công cụ trên web Minh Phúc (Maersk: 33,2 / 67,7 / 76,4).
CONTAINER_M3 = {"20'": 33.0, "40'": 67.0, "40'HC": 76.0}

DON_VI_MET = {"mm": 0.001, "cm": 0.01, "m": 1.0, "inch": 0.0254}


def cbm(dai: float, rong: float, cao: float, don_vi: str = "cm") -> float:
    """CBM (m³) = D × R × C quy về mét. Dùng kích thước PHỦ BÌ của thùng ở trạng thái GIAO."""
    k = DON_VI_MET.get(don_vi)
    if k is None:
        raise ValueError(f"Đơn vị '{don_vi}' không hỗ trợ ({', '.join(DON_VI_MET)})")
    if min(dai, rong, cao) <= 0:
        raise ValueError("Kích thước phải > 0")
    return (dai * k) * (rong * k) * (cao * k)


def so_thung_container(cbm_mot_thung: float, he_so_khai_thac: float = 0.85) -> dict[str, int]:
    """Số thùng ước tính = thể tích × hệ số khai thác ÷ CBM một thùng (làm tròn xuống)."""
    if cbm_mot_thung <= 0:
        raise ValueError("CBM phải > 0")
    return {k: int(v * he_so_khai_thac / cbm_mot_thung) for k, v in CONTAINER_M3.items()}


def so_thung_xe(long_dai_m: float, long_rong_m: float, long_cao_m: float, cbm_mot_thung: float,
                he_so_khai_thac: float = 0.85) -> int:
    return int(long_dai_m * long_rong_m * long_cao_m * he_so_khai_thac / cbm_mot_thung)


@dataclass
class KetQuaPallet:
    so_thung_lop: int
    cach_xep: str
    so_lop: int | None
    tong: int | None
    phu_kin_pct: float


def _luoi(pd: float, pr: float, a: float, b: float) -> int:
    return int(pd // a) * int(pr // b)


def thung_moi_lop(dai: float, rong: float, pallet_dai: float, pallet_rong: float) -> tuple[int, str]:
    """Số thùng mỗi lớp (mm, phủ bì thùng) — thử xếp lưới hai chiều và xếp chia hai khối.

    Không cho thùng chìa ra mép pallet (chìa mép làm mất BCT).
    """
    best = (_luoi(pallet_dai, pallet_rong, dai, rong), "lưới, cạnh dài thùng theo cạnh dài pallet")
    alt = _luoi(pallet_dai, pallet_rong, rong, dai)
    if alt > best[0]:
        best = (alt, "lưới, xoay thùng 90°")
    # Chia hai khối theo chiều dài pallet: k cột hướng A + phần còn lại hướng B
    for (a, b, ten_a, ten_b) in ((dai, rong, "dọc", "ngang"), (rong, dai, "ngang", "dọc")):
        cot_a = int(pallet_dai // a)
        for k in range(1, cot_a + 1):
            phan_a = k * a
            n = int(pallet_rong // b) * k + _luoi(pallet_dai - phan_a, pallet_rong, b, a)
            if n > best[0]:
                best = (n, f"hai khối theo chiều dài pallet: {k} cột thùng {ten_a} + phần còn lại thùng {ten_b}")
        hang_a = int(pallet_rong // b)
        for k in range(1, hang_a + 1):
            phan_b = k * b
            n = int(pallet_dai // a) * k + _luoi(pallet_dai, pallet_rong - phan_b, b, a)
            if n > best[0]:
                best = (n, f"hai khối theo chiều rộng pallet: {k} hàng thùng {ten_a} + phần còn lại thùng {ten_b}")
    return best


def pallet(dai: float, rong: float, pallet_dai: float = 1200, pallet_rong: float = 800,
           cao_thung: float | None = None, cao_toi_da: float | None = None,
           cao_pallet: float = 150) -> KetQuaPallet:
    """Thùng mỗi lớp, số lớp theo chiều cao tối đa (gồm pallet), tổng thùng (mm)."""
    if min(dai, rong, pallet_dai, pallet_rong) <= 0:
        raise ValueError("Kích thước phải > 0")
    n, cach = thung_moi_lop(dai, rong, pallet_dai, pallet_rong)
    phu = n * dai * rong / (pallet_dai * pallet_rong) * 100
    so_lop = tong = None
    if cao_thung and cao_toi_da:
        so_lop = int((cao_toi_da - cao_pallet) // cao_thung)
        tong = so_lop * n
    return KetQuaPallet(n, cach, so_lop, tong, phu)
