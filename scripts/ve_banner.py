"""Vẽ assets/banner.svg cho README: mặt kraft in mực xanh, mép dưới là mặt cắt tấm 5 lớp sóng BC đúng tỷ lệ.

Chạy từ gốc repo:  python scripts/ve_banner.py
Cần: fontTools (pip install fonttools) và font Bahnschrift của Windows. Chữ được đổi thành đường vẽ để GitHub hiện đúng font.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
FONT = Path(r"C:\Windows\Fonts\bahnschrift.ttf")

W, H = 1280, 400
MAU = {
    "kraft": "#C49B6C",       # mặt giấy kraft
    "muc_xanh": "#184B22",    # mực flexo xanh thương hiệu, in trên kraft
    "muc_nau": "#2B2420",     # mực nâu đen cho dòng phụ
    "hoc_song": "#6E4B2A",    # khoang khí trong sóng (tối)
    "giay_cat": "#E2C69E",    # mép giấy ở mặt cắt
}


def do_sang(hex_: str) -> float:
    r, g, b = (int(hex_[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4  # noqa: E731
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def tuong_phan(a: str, b: str) -> float:
    la, lb = sorted((do_sang(a), do_sang(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def chu_thanh_duong(font: TTFont, text: str, x: float, y: float, co: float, vi_tri: dict, gian: float = 0.0):
    """Trả (đường SVG, bề rộng) của một dòng chữ đặt tại (x, y = đường chân chữ)."""
    gs = font.getGlyphSet(location=vi_tri)
    cmap = font.getBestCmap()
    ti_le = co / font["head"].unitsPerEm
    phan, bx = [], x
    for ch in text:
        ten = cmap.get(ord(ch))
        if ten is None:
            raise ValueError(f"Font thiếu ký tự {ch!r}")
        pen = SVGPathPen(gs)
        gs[ten].draw(TransformPen(pen, (ti_le, 0, 0, -ti_le, bx, y)))
        lenh = pen.getCommands()
        if lenh:
            phan.append(lenh)
        bx += gs[ten].width * ti_le + gian
    return " ".join(phan), bx - x - gian


def song(y_giua: float, bien_do: float, buoc: float, x0: float = -20, x1: float = W + 20, pha: float = 0.0) -> str:
    """Đường giấy sóng (hình sin) — đủ gần biên dạng sóng để nhìn ra mặt cắt."""
    diem = []
    x = x0
    while x <= x1:
        diem.append(f"{x:.1f},{y_giua - bien_do * math.cos(2 * math.pi * (x / buoc) + pha):.1f}")
        x += 3
    return "M" + " L".join(diem)


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    font = TTFont(FONT)

    # Kiểm tương phản chữ trên kraft (tiêu đề chữ lớn ≥ 3:1, dòng phụ ≥ 4,5:1)
    tp_tieu_de = tuong_phan(MAU["muc_xanh"], MAU["kraft"])
    tp_phu = tuong_phan(MAU["muc_nau"], MAU["kraft"])
    print(f"Tương phản: tiêu đề {tp_tieu_de:.2f}:1 · dòng phụ {tp_phu:.2f}:1")
    if tp_tieu_de < 3 or tp_phu < 4.5:
        raise SystemExit("Tương phản không đạt — chỉnh màu")

    trai = 76
    tieu_de, _ = chu_thanh_duong(font, "MinhPhuc Toolkit", trai, 158, 118, {"wght": 650, "wdth": 75}, gian=1.0)
    phu, _ = chu_thanh_duong(font, "Kho kiến thức kỹ thuật của Bao Bì Minh Phúc", trai + 3, 218, 42,
                             {"wght": 400, "wdth": 100}, gian=0.4)

    # Mặt cắt tấm 5 lớp BC — tỷ lệ ~14 px/mm (sóng B cao ~2,7 mm bước ~6,5 mm; sóng C cao ~3,8 mm bước ~7,6 mm)
    lop = 5.0                       # bề dày giấy mặt (phóng đại cho dễ nhìn)
    day = H - 6                     # đáy tấm
    c_cao, b_cao = 54.0, 38.0
    y_mat_day = day - lop / 2
    y_c = day - lop - c_cao / 2
    y_mat_giua = day - lop - c_cao - lop / 2
    y_b = day - 2 * lop - c_cao - b_cao / 2
    y_mat_tren = day - 2 * lop - c_cao - b_cao - lop / 2
    tren_cung = y_mat_tren - lop / 2

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
  <title id="t">MinhPhuc Toolkit</title>
  <desc id="d">Kho kiến thức kỹ thuật của Bao Bì Minh Phúc. Mặt giấy kraft in mực xanh; mép dưới là mặt cắt tấm carton 5 lớp sóng BC.</desc>
  <defs>
    <filter id="soi" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.006 0.55" numOctaves="3" seed="11" result="n"/>
      <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.36  0 0 0 0 0.24  0 0 0 0 0.12  0 0 0 0.55 -0.2"/>
    </filter>
  </defs>
  <rect width="{W}" height="{H}" fill="{MAU['kraft']}"/>
  <rect width="{W}" height="{tren_cung:.1f}" filter="url(#soi)" opacity="0.35"/>
  <path d="{tieu_de}" fill="{MAU['muc_xanh']}"/>
  <path d="{phu}" fill="{MAU['muc_nau']}"/>
  <g>
    <rect x="0" y="{tren_cung:.1f}" width="{W}" height="{H - tren_cung:.1f}" fill="{MAU['hoc_song']}"/>
    <path d="{song(y_b, b_cao / 2, 91)}" fill="none" stroke="{MAU['giay_cat']}" stroke-width="4"/>
    <path d="{song(y_c, c_cao / 2, 106, pha=math.pi / 3)}" fill="none" stroke="{MAU['giay_cat']}" stroke-width="4"/>
    <rect x="0" y="{y_mat_tren - lop / 2:.1f}" width="{W}" height="{lop}" fill="{MAU['giay_cat']}"/>
    <rect x="0" y="{y_mat_giua - lop / 2:.1f}" width="{W}" height="{lop}" fill="{MAU['giay_cat']}"/>
    <rect x="0" y="{y_mat_day - lop / 2:.1f}" width="{W}" height="{lop}" fill="{MAU['giay_cat']}"/>
  </g>
</svg>
"""
    out = ROOT / "assets" / "banner.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf-8", newline="\n")
    print(f"OK  {out.relative_to(ROOT)}  {out.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
