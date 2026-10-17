"""Tải lại thư viện tài liệu gốc (bên thứ ba) theo sources/nguon.tsv vào thu-vien/ (không đưa lên git).

Chạy từ gốc repo:  python scripts/tai_thu_vien.py [--chi 05_In_flexo] [--dich thu-vien]
Chỉ dùng thư viện chuẩn Python. Ghi thu-vien/_nguon.json (url, kích thước, lỗi).
Trang web cần in ra PDF (sources/trang-web.tsv) phải in bằng trình duyệt — xem skill mp-thu-vien.
Tài liệu tải về để học tập nội bộ; giữ nguồn, không phát tán lại.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"


def doc_danh_sach(f: Path) -> list[tuple[str, str, str, str]]:
    out = []
    for line in f.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        folder, name, url, note = (line.split("\t") + [""] * 4)[:4]
        out.append((folder, name, url, note))
    return out


def tai(url: str) -> tuple[int, bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:  # noqa: S310 (URL từ danh sách nguồn của repo)
        return r.status, r.read(), r.headers.get("content-type", "")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser()
    p.add_argument("--danh-sach", default=str(ROOT / "sources" / "nguon.tsv"))
    p.add_argument("--dich", default=str(ROOT / "thu-vien"))
    p.add_argument("--chi", help="chỉ tải một thư mục chủ đề, vd 05_In_flexo")
    a = p.parse_args()
    dich = Path(a.dich)
    log_f = dich / "_nguon.json"
    log = json.loads(log_f.read_text(encoding="utf-8")) if log_f.exists() else {}
    ok = loi = 0
    for folder, name, url, note in doc_danh_sach(Path(a.danh_sach)):
        if a.chi and folder != a.chi:
            continue
        dest = dich / folder / name
        rec = {"thu_muc": folder, "file": name, "url": url, "ghi_chu": note}
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            try:
                status, body, ctype = tai(url)
                if name.lower().endswith(".pdf") and not body.startswith(b"%PDF"):
                    rec["loi"] = f"không phải PDF ({ctype})"
                else:
                    dest.write_bytes(body)
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                rec["loi"] = str(e)[:200]
            time.sleep(0.5)
        if dest.exists():
            rec["kb"] = dest.stat().st_size // 1024
            ok += 1
            print(f"OK   {folder}/{name}  {rec['kb']} KB")
        else:
            loi += 1
            print(f"LỖI  {folder}/{name}: {rec.get('loi')}")
        log[f"{folder}/{name}"] = rec
    dich.mkdir(parents=True, exist_ok=True)
    log_f.write_text(json.dumps(log, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{ok} file có, {loi} lỗi")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
