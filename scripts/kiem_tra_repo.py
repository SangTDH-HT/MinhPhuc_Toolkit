"""Kiểm tra toàn repo MinhPhuc Toolkit. Chạy từ bất kỳ đâu:  python scripts/kiem_tra_repo.py

Kiểm:
  1. Manifest plugin/marketplace hợp lệ, đường dẫn tồn tại.
  2. Mọi skills/*/SKILL.md có frontmatter: name trùng tên thư mục, description không rỗng.
  3. Router skills/minhphuc/SKILL.md trỏ tới mọi skill; mọi đường dẫn trong router tồn tại.
  4. Liên kết Markdown tương đối và đường dẫn `templates/…`, `data/…`, `docs/…`, `sources/…`, `scripts/…`, `tools/…` trong mọi .md tồn tại.
  5. Không lộ bí mật (địa chỉ IPv4, mật khẩu, token) và không có từ khoá ngoài phạm vi (lập trình PLC/HMI/MES, TIA).
  6. CSV đều số cột; JSON đọc được.
Thoát mã 1 nếu có lỗi.
"""
from __future__ import annotations

import csv
import ipaddress
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BO_QUA_THU_MUC = {".git", "thu-vien", "library", "dist", "out", "__pycache__", ".venv"}
TIEN_TO_DUONG_DAN = ("templates/", "data/", "docs/", "sources/", "scripts/", "tools/", "skills/")

# Từ khoá ngoài phạm vi (repo không chứa lập trình PLC/HMI/MES hay TIA). File được phép NHẮC tên để nói "không có".
NGOAI_PHAM_VI = [
    r"\bOpenness\b", r"TIA\s*Portal", r"\bTiaHost\b", r"\bWinCC\b", r"\bSIMATIC\b", r"\bWeintek\b", r"\bsnap7\b",
    r"S7\.Net", r"\bMachineCatalog\b", r"\bSqlConnection\b", r"\bSX_KeHoach", r"\bSX_NhatKy", r"%[IQM]\d+\.\d",
    r"\bDB\d+\.DB[XWDB]", r"\bMW20\b", r"\bconfig\.json\b",
]
DUOC_NHAC_PHAM_VI = {
    "CLAUDE.md", "AGENTS.md", "CONTRIBUTING.md", "README.md", "docs/KIEN-TRUC.md", "docs/HUONG-DAN-SU-DUNG.md",
    "skills/minhphuc/SKILL.md", "skills/mp-mes-su-dung/SKILL.md", "scripts/kiem_tra_repo.py", "CHANGELOG.md",
}
BI_MAT = [
    (re.compile(r"(?i)\b(mật\s*khẩu|password|passwd|pwd)\s*[:=]\s*\S+"), "mật khẩu"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"), "token GitHub"),
    (re.compile(r"\bsk-[A-Za-z0-9]{20,}"), "khoá API"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "khoá AWS"),
    (re.compile(r"(?i)\bpin\s*[:=]\s*\d{4,}"), "mã PIN"),
]
IPV4 = re.compile(r"(?<![\d.])(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})(?![\d.])")

loi: list[str] = []


def bao(msg: str) -> None:
    loi.append(msg)


def cac_file(duoi: tuple[str, ...]) -> list[Path]:
    out = []
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in duoi and not (set(p.relative_to(ROOT).parts) & BO_QUA_THU_MUC):
            out.append(p)
    return sorted(out)


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def doc_json(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        bao(f"{rel(p)}: JSON hỏng — {e}")
        return None


def kiem_manifest() -> None:
    plugin = doc_json(ROOT / ".claude-plugin" / "plugin.json")
    if plugin:
        for k in ("name", "version", "description", "skills"):
            if not plugin.get(k):
                bao(f".claude-plugin/plugin.json thiếu '{k}'")
        if plugin.get("skills") and not (ROOT / plugin["skills"]).exists():
            bao(f".claude-plugin/plugin.json: đường dẫn skills '{plugin['skills']}' không có")
    mk = doc_json(ROOT / ".claude-plugin" / "marketplace.json")
    if mk:
        for k in ("name", "owner", "plugins"):
            if not mk.get(k):
                bao(f".claude-plugin/marketplace.json thiếu '{k}'")
        for pl in mk.get("plugins", []):
            if not (ROOT / pl.get("source", "")).exists():
                bao(f"marketplace.json: source '{pl.get('source')}' không có")
            if plugin and pl.get("name") != plugin.get("name"):
                bao("marketplace.json: tên plugin khác plugin.json")


def doc_frontmatter(p: Path) -> dict | None:
    t = p.read_text(encoding="utf-8")
    if not t.startswith("---\n"):
        return None
    end = t.find("\n---", 4)
    if end < 0:
        return None
    khoi = t[4:end]
    meta = {}
    m = re.search(r"^name:\s*(\S.*)$", khoi, re.M)
    if m:
        meta["name"] = m.group(1).strip()
    m = re.search(r"^description:\s*(.*)$", khoi, re.M)
    if m:
        dau = m.group(1).strip()
        if dau in (">", "|", ">-", "|-"):
            sau = khoi[m.end():].splitlines()
            dong = [s.strip() for s in sau if s.startswith("  ")]
            meta["description"] = " ".join(dong)
        else:
            meta["description"] = dau
    return meta


def kiem_skill() -> list[str]:
    ten = []
    for d in sorted((ROOT / "skills").iterdir()):
        if not d.is_dir():
            continue
        f = d / "SKILL.md"
        if not f.exists():
            bao(f"skills/{d.name}: thiếu SKILL.md")
            continue
        meta = doc_frontmatter(f)
        if meta is None:
            bao(f"skills/{d.name}/SKILL.md: thiếu hoặc hỏng frontmatter YAML")
            continue
        if meta.get("name") != d.name:
            bao(f"skills/{d.name}/SKILL.md: name '{meta.get('name')}' khác tên thư mục")
        if len(meta.get("description", "")) < 40:
            bao(f"skills/{d.name}/SKILL.md: description quá ngắn hoặc thiếu")
        if len(meta.get("description", "")) > 1024:
            bao(f"skills/{d.name}/SKILL.md: description dài quá 1024 ký tự")
        ref = d / "references"
        if ref.is_dir():
            noi_dung = f.read_text(encoding="utf-8")
            for r in sorted(ref.glob("*.md")):
                if f"references/{r.name}" not in noi_dung:
                    bao(f"skills/{d.name}: reference '{r.name}' không được SKILL.md nhắc tới (mồ côi)")
        ten.append(d.name)
    return ten


def kiem_router(ten_skill: list[str]) -> None:
    f = ROOT / "skills" / "minhphuc" / "SKILL.md"
    if not f.exists():
        bao("Thiếu router skills/minhphuc/SKILL.md")
        return
    t = f.read_text(encoding="utf-8")
    for s in ten_skill:
        if s != "minhphuc" and f"skills/{s}/SKILL.md" not in t:
            bao(f"Router không trỏ tới skill '{s}'")
    for m in re.findall(r"skills/[A-Za-z0-9._/-]+\.md", t):
        if not (ROOT / m).exists():
            bao(f"Router trỏ tới '{m}' không có")


def kiem_lien_ket(md_files: list[Path]) -> None:
    for p in md_files:
        t = p.read_text(encoding="utf-8")
        for m in re.finditer(r"\]\(([^)\s]+)\)", t):
            dich = m.group(1).split("#")[0]
            if not dich or dich.startswith(("http://", "https://", "mailto:")) or "<" in dich:
                continue
            if not (p.parent / dich).resolve().exists():
                bao(f"{rel(p)}: liên kết hỏng → {dich}")
        for m in re.finditer(r"`([^`\s]+)`", t):
            s = m.group(1).rstrip(".,;:")
            if not s.startswith(TIEN_TO_DUONG_DAN) or any(c in s for c in "<>*{}") or "…" in s:
                continue
            if not (ROOT / s).exists():
                bao(f"{rel(p)}: đường dẫn `{s}` không có")


def kiem_bi_mat_va_pham_vi(files: list[Path]) -> None:
    for p in files:
        r = rel(p)
        try:
            t = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for i, dong in enumerate(t.splitlines(), 1):
            for m in IPV4.finditer(dong):
                so = [int(x) for x in m.groups()]
                if all(0 <= x <= 255 for x in so):
                    try:
                        ipaddress.IPv4Address(".".join(map(str, so)))
                        bao(f"{r}:{i}: có địa chỉ IPv4 '{m.group(0)}' — không đưa địa chỉ mạng vào repo")
                    except ValueError:
                        pass
            for rx, ten in BI_MAT:
                if rx.search(dong):
                    bao(f"{r}:{i}: nghi lộ {ten}")
            if r not in DUOC_NHAC_PHAM_VI:
                for pat in NGOAI_PHAM_VI:
                    if re.search(pat, dong):
                        bao(f"{r}:{i}: từ khoá ngoài phạm vi '{pat}' (repo không chứa lập trình PLC/HMI/MES, TIA)")


def kiem_du_lieu() -> None:
    for p in cac_file((".csv",)):
        with open(p, encoding="utf-8", newline="") as f:
            rows = list(csv.reader(f))
        if not rows:
            bao(f"{rel(p)}: rỗng")
            continue
        n = len(rows[0])
        for i, r in enumerate(rows[1:], 2):
            if len(r) != n:
                bao(f"{rel(p)}:{i}: {len(r)} cột, tiêu đề có {n}")
    for p in cac_file((".json",)):
        doc_json(p)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    kiem_manifest()
    ten = kiem_skill()
    kiem_router(ten)
    md = cac_file((".md",))
    kiem_lien_ket(md)
    kiem_bi_mat_va_pham_vi(cac_file((".md", ".py", ".csv", ".json", ".yaml", ".yml", ".tsv", ".ps1", ".txt")))
    kiem_du_lieu()
    print(f"Skill: {len(ten)} · file Markdown: {len(md)}")
    if loi:
        print(f"\n{len(loi)} LỖI:")
        for x in loi:
            print("  -", x)
        return 1
    print("Repo hợp lệ.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
