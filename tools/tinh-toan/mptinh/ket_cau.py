"""Kết cấu: độ dày theo sóng, hệ số co sóng, định lượng tấm, phôi thùng RSC (FEFCO 0201)."""

from __future__ import annotations

import re
from dataclasses import dataclass

# Độ dày tấm gần đúng (mm) — [Kinh nghiệm ngành]; đo thật theo ISO 3034 khi có mẫu.
DO_DAY_SONG = {"E": 1.5, "B": 3.0, "C": 4.0, "A": 5.0, "BE": 4.5, "BC": 7.0, "BA": 8.0}

# Hệ số co sóng (take-up) gần đúng — giữa khoảng trong sổ tay [Kinh nghiệm ngành].
HE_SO_CO = {"A": 1.52, "C": 1.45, "B": 1.35, "E": 1.26, "F": 1.22}


def do_day(song: str) -> float:
    """Độ dày tấm gần đúng theo loại sóng (mm)."""
    key = song.strip().upper()
    if key not in DO_DAY_SONG:
        raise ValueError(f"Không biết sóng '{song}'. Dùng một trong: {', '.join(DO_DAY_SONG)}")
    return DO_DAY_SONG[key]


@dataclass
class KetQuaDinhLuong:
    tong: float          # g/m² tấm (chưa kể keo nếu keo = 0)
    giay_mat: float      # tổng giấy mặt
    giay_song: float     # tổng giấy sóng đã nhân hệ số co
    keo: float           # keo khô cộng thêm
    chi_tiet: list       # [(lớp, định lượng, hệ số, đóng góp)]


def phan_tich_cau_truc(cau_truc: str) -> list[tuple[float, str | None]]:
    """'150,120C,150' -> [(150, None), (120, 'C'), (150, None)].

    Số đứng một mình = giấy mặt; số kèm chữ sóng (A, B, C, E, F) = giấy sóng của sóng đó.
    Chấp nhận dấu phân cách ',', '/', '-' hoặc khoảng trắng.
    """
    lop = []
    for tok in re.split(r"[,/\s\-]+", cau_truc.strip()):
        if not tok:
            continue
        m = re.fullmatch(r"(\d+(?:[.,]\d+)?)([A-Fa-f])?", tok)
        if not m:
            raise ValueError(f"Không hiểu lớp '{tok}' (ví dụ đúng: 150 hoặc 120C)")
        lop.append((float(m.group(1).replace(",", ".")), m.group(2).upper() if m.group(2) else None))
    if len(lop) < 2:
        raise ValueError("Cấu trúc cần ít nhất 2 lớp")
    return lop


def dinh_luong_tam(cau_truc: str, keo_moi_duong: float = 0.0,
                   he_so: dict[str, float] | None = None) -> KetQuaDinhLuong:
    """Định lượng tấm ≈ Σ giấy mặt + Σ giấy sóng × hệ số co + keo.

    keo_moi_duong: keo khô mỗi đường keo (g/m²); mỗi lớp sóng có 2 đường keo.
    [Kinh nghiệm ngành] keo khô thường ~8–15 g/m² mỗi lớp keo.
    """
    hs = dict(HE_SO_CO)
    if he_so:
        hs.update({k.upper(): v for k, v in he_so.items()})
    chi_tiet = []
    mat = song = 0.0
    so_lop_song = 0
    for i, (g, s) in enumerate(phan_tich_cau_truc(cau_truc), start=1):
        if s is None:
            mat += g
            chi_tiet.append((i, g, 1.0, g))
        else:
            if s not in hs:
                raise ValueError(f"Chưa có hệ số co cho sóng {s}")
            dong_gop = g * hs[s]
            song += dong_gop
            so_lop_song += 1
            chi_tiet.append((i, g, hs[s], dong_gop))
    keo = keo_moi_duong * 2 * so_lop_song
    return KetQuaDinhLuong(round(mat + song + keo, 1), mat, round(song, 1), keo, chi_tiet)


@dataclass
class KetQuaPhoi:
    t: float
    lan_dai: float
    lan_rong: float
    lan_cao: float
    nap: float
    dai_phoi: float
    rong_phoi: float
    dien_tich_m2: float
    phu_bi: tuple[float, float, float]
    khoi_luong_g: float | None


def phoi_rsc(dai: float, rong: float, cao: float, song: str | None = None, t: float | None = None,
             tai_dan: float = 35.0, dinh_luong: float | None = None) -> KetQuaPhoi:
    """Phôi thùng nắp gài RSC (FEFCO 0201) từ kích thước LỌT LÒNG (mm).

    Khoảng cách lằn theo FEFCO Quality Catalogue: (D + t) × (R + t) × (C + 2t).
    Phôi [Kinh nghiệm ngành]: dài = 2(D+t) + 2(R+t) + tai dán; nắp = (R+t)/2; rộng = (C+2t) + 2 × nắp.
    Phủ bì gần đúng [Kinh nghiệm ngành]: (D+2t) × (R+2t) × (C+4t).
    Không thay bảng bù kích thước của phòng thiết kế.
    """
    if t is None:
        if song is None:
            raise ValueError("Cần sóng hoặc độ dày t")
        t = do_day(song)
    for ten, v in (("dài", dai), ("rộng", rong), ("cao", cao)):
        if v <= 0:
            raise ValueError(f"Kích thước {ten} phải > 0")
    lan_dai, lan_rong, lan_cao = dai + t, rong + t, cao + 2 * t
    nap = lan_rong / 2
    dai_phoi = 2 * lan_dai + 2 * lan_rong + tai_dan
    rong_phoi = lan_cao + 2 * nap
    dt = dai_phoi * rong_phoi / 1e6
    kl = dt * dinh_luong if dinh_luong else None
    return KetQuaPhoi(t, lan_dai, lan_rong, lan_cao, nap, dai_phoi, rong_phoi, dt,
                      (dai + 2 * t, rong + 2 * t, cao + 4 * t), kl)
