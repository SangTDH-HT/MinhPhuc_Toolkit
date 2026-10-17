"""Xuất Markdown của repo ra PDF để in (cần Microsoft Edge; PyMuPDF tuỳ chọn).

Ví dụ (chạy từ gốc repo):
  python scripts/xuat_pdf.py skills/mp-to-song          # cả skill: SKILL.md + references → dist/mp-to-song.pdf
  python scripts/xuat_pdf.py templates/kiem-tra-dau-don.md
  python scripts/xuat_pdf.py --tat-ca                     # mọi skill → dist/
PDF ra thư mục dist/ (không đưa lên git).
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from md2pdf import bo_frontmatter, make_pdf  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
BUILD = DIST / "_build"
NOTE = (f"Kho kiến thức nội bộ MinhPhuc Toolkit — xuất ngày {date.today():%d/%m/%Y}. "
        "Dữ kiện có nguồn trong ngoặc vuông; [KN ngành] = kinh nghiệm ngành, cần kiểm chứng tại xưởng.<br>"
        "Biên soạn: Nguyễn Hữu Sáng")


def xuat_skill(thu_muc: Path) -> Path:
    meta, md = bo_frontmatter((thu_muc / "SKILL.md").read_text(encoding="utf-8"))
    sections = [("Tổng quan skill", f"skills/{thu_muc.name}/SKILL.md", md)]
    ref = thu_muc / "references"
    if ref.is_dir():
        for f in sorted(ref.glob("*.md")):
            sections.append((f.stem.replace("-", " "), f"skills/{thu_muc.name}/references/{f.name}",
                             f.read_text(encoding="utf-8")))
    out = DIST / f"{thu_muc.name}.pdf"
    make_pdf(sections, meta.get("name", thu_muc.name), meta.get("description", "")[:300], out, BUILD, NOTE)
    return out


def xuat_file(f: Path) -> Path:
    meta, md = bo_frontmatter(f.read_text(encoding="utf-8"))
    tieu_de = next((ln[2:].strip() for ln in md.splitlines() if ln.startswith("# ")), f.stem)
    out = DIST / f"{f.stem}.pdf"
    make_pdf([(tieu_de, "", md)], tieu_de, str(f.relative_to(ROOT)) if f.is_relative_to(ROOT) else f.name,
             out, BUILD, NOTE)
    return out


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("duong_dan", nargs="*", help="thư mục skill hoặc file .md")
    p.add_argument("--tat-ca", action="store_true", help="xuất mọi skill")
    a = p.parse_args()
    muc = [ROOT / "skills" / d.name for d in sorted((ROOT / "skills").iterdir()) if d.is_dir()] if a.tat_ca else \
        [Path(x).resolve() for x in a.duong_dan]
    if not muc:
        p.print_help()
        return 1
    for m in muc:
        out = xuat_skill(m) if m.is_dir() else xuat_file(m)
        print(f"OK  {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
