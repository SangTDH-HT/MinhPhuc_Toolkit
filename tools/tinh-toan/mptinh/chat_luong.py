"""Lấy mẫu AQL theo bảng của FEFCO Quality Catalogue 4.4 (dựa ISO 2859-1)."""

from __future__ import annotations

AQL_COT = (0.65, 1.0, 1.5, 2.5, 4.0, 6.5)

# (cỡ lô tối đa, cỡ mẫu, số chấp nhận theo AQL_COT). Lô ≤ 500: mẫu = N hoặc 10.
BANG_AQL = (
    (500, 10, (0, 0, 0, 1, 1, 2)),
    (1200, 20, (0, 1, 1, 1, 2, 3)),
    (3200, 32, (1, 1, 1, 2, 3, 4)),
    (10000, 50, (1, 1, 2, 3, 4, 6)),
    (35000, 80, (1, 2, 3, 4, 6, 8)),
    (150000, 125, (2, 3, 4, 6, 8, 12)),
)

CAP_LOI = {
    "1": "Nghiêm trọng (CD) — không cho phép, có thể trả cả lô",
    "2A": "Nặng — AQL 0,65 hoặc 1,0",
    "2B": "Nặng (ít hơn) — AQL 1,5 hoặc 4,0",
    "3": "Nhẹ — AQL 6,5",
}


def aql(co_lo: int, muc_aql: float) -> tuple[int, int, int]:
    """Trả (cỡ mẫu n, số chấp nhận Ac, số loại bỏ Re = Ac + 1)."""
    if co_lo <= 0:
        raise ValueError("Cỡ lô phải > 0")
    try:
        cot = AQL_COT.index(float(muc_aql))
    except ValueError:
        raise ValueError(f"AQL phải là một trong {AQL_COT}") from None
    for lo_max, n, ac in BANG_AQL:
        if co_lo <= lo_max:
            n_thuc = min(n, co_lo) if lo_max == 500 else n
            return n_thuc, ac[cot], ac[cot] + 1
    raise ValueError("Lô trên 150.000 cái — FEFCO khuyên chia lô (mỗi pallet hoặc mỗi chuyến xe một lô)")
