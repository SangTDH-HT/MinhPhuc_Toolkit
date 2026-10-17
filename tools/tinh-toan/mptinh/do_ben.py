"""Độ bền: McKee, ECT từ giấy (Maltenfort–Seth), BCT yêu cầu, ảnh hưởng độ ẩm."""

from __future__ import annotations

import math

G = 9.80665  # N/kgf

HE_SO_AN_TOAN = {
    3: "Hàng tự đỡ tải (~100 %): chai thuỷ tinh, lon nhôm",
    4: "Hàng đỡ một phần (~50 %): quạt, đồ điện tử",
    5: "Hàng không đỡ tải: thực phẩm, hàng rời",
}


def bct_yeu_cau(sf: float, so_tang: int, kg_moi_thung: float) -> float:
    """BCT yêu cầu (kgf) = S.F × (n − 1) × W  [web Minh Phúc, bài cách tính BCT]."""
    if so_tang < 1:
        raise ValueError("Số tầng phải ≥ 1")
    if sf <= 0 or kg_moi_thung <= 0:
        raise ValueError("S.F và khối lượng phải > 0")
    return sf * (so_tang - 1) * kg_moi_thung


def chu_vi_m(dai_mm: float, rong_mm: float) -> float:
    return 2 * (dai_mm + rong_mm) / 1000.0


def mckee_bct_n(ect_kn_m: float, t_mm: float, dai_mm: float, rong_mm: float) -> float:
    """BCT (N) = 5,87 × ECT × √(t × Z)  — McKee rút gọn [Georgia Tech].

    ECT đổi ra N/m, t ra m, Z = 2(D+R) ra m.
    """
    if min(ect_kn_m, t_mm, dai_mm, rong_mm) <= 0:
        raise ValueError("Mọi đại lượng phải > 0")
    return 5.87 * (ect_kn_m * 1000.0) * math.sqrt((t_mm / 1000.0) * chu_vi_m(dai_mm, rong_mm))


def ect_can_kn_m(bct_kgf: float, t_mm: float, dai_mm: float, rong_mm: float) -> float:
    """ECT cần (kN/m) để đạt BCT (kgf) — đảo công thức McKee."""
    bct_n = bct_kgf * G
    return bct_n / (5.87 * math.sqrt((t_mm / 1000.0) * chu_vi_m(dai_mm, rong_mm))) / 1000.0


def ect_maltenfort_seth(sct_mat: list[float], sct_song: list[tuple[float, float]]) -> float:
    """ECT (kN/m) ≈ 0,7 × (Σ SCT giấy mặt + Σ hệ số co × SCT giấy sóng)  [Georgia Tech].

    sct_mat: SCT (kN/m, chiều ngang CD) từng lớp giấy mặt.
    sct_song: [(SCT giấy sóng kN/m, hệ số co)] từng lớp sóng.
    """
    return 0.7 * (sum(sct_mat) + sum(s * k for s, k in sct_song))


def am_can_bang(rh: float) -> float:
    """Độ ẩm cân bằng gần đúng của kraft nâu (%): M ≈ 0,135 × RH + 0,59  [Georgia Tech]."""
    return 0.135 * rh + 0.59


def he_so_do_am(rh: float, rh_chuan: float = 50.0) -> float:
    """Hệ số BCT/ECT ở độ ẩm rh so với rh_chuan.

    Quy tắc: +10 điểm % RH → −~10 % (tuyến tính quanh 50 %): ở 80 % RH còn ~0,70
    (Georgia Tech đo giảm 27–32 %). Dùng cho 20–95 % RH; ngoài khoảng là ngoại suy.
    """
    def f(x: float) -> float:
        return 1.0 - 0.01 * (x - 50.0)
    return f(rh) / f(rh_chuan)
