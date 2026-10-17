"""Markdown -> PDF A4 qua Microsoft Edge headless (Windows).

Dùng:  from md2pdf import make_pdf
       make_pdf(sections, title, subtitle, out_pdf, build_dir, meta_note)
       sections: list[(tiêu_đề_mục, nguồn, markdown)]

PyMuPDF (pip install pymupdf) là TUỲ CHỌN: có thì thêm chân trang số trang và nén ảnh; không có vẫn ra PDF.
"""
from __future__ import annotations

import html
import os
import re
import shutil
import subprocess
from pathlib import Path

EDGE_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

CSS = """
@page { size: A4; margin: 16mm 15mm 18mm 15mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10.3pt; line-height: 1.5; color: #1d2520; margin: 0; }
.cover { height: 255mm; display: flex; flex-direction: column; justify-content: space-between; page-break-after: always; }
.cover .brand { font-size: 10pt; letter-spacing: .08em; text-transform: uppercase; color: #1f7a3d; font-weight: 700; }
.cover h1 { font-size: 28pt; line-height: 1.15; margin: 50mm 0 6mm; color: #12351f; }
.cover .sub { font-size: 13pt; color: #44524a; max-width: 155mm; }
.cover .meta { font-size: 9.5pt; color: #5b675f; border-top: 2px solid #1f7a3d; padding-top: 4mm; }
.toc ol { padding-left: 6mm; } .toc li { margin: 1mm 0; } .toc .u { color: #6b766f; font-size: 8.3pt; }
.page { page-break-before: always; }
.src { font-size: 8.3pt; color: #6b766f; border-bottom: 1px solid #d5ddd7; padding-bottom: 1.5mm; margin-bottom: 3mm; word-break: break-all; }
h1 { font-size: 17pt; color: #12351f; margin: 0 0 3mm; line-height: 1.25; }
h2 { font-size: 13pt; color: #1f7a3d; margin: 5mm 0 2mm; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 4mm 0 1.5mm; page-break-after: avoid; }
h4, h5 { font-size: 10.3pt; margin: 3mm 0 1mm; }
p { margin: 0 0 2mm; }
ul, ol { margin: 0 0 2.5mm; padding-left: 6mm; } li { margin: 0.6mm 0; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0 3.5mm; font-size: 9pt; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #c9d3cc; padding: 1.2mm 1.8mm; vertical-align: top; text-align: left; }
th { background: #e6efe8; }
blockquote { margin: 2mm 0 3mm; padding: 2mm 3.5mm; background: #f6f8f6; border-left: 3px solid #9fb8a7; }
pre { background: #f1f4f2; padding: 2mm 3mm; font-size: 8.6pt; white-space: pre-wrap; page-break-inside: avoid; }
b { font-weight: 650; }
code { font-family: Consolas, monospace; font-size: 9pt; background: #f1f4f2; padding: 0 1mm; }
"""


def tim_edge() -> str:
    for p in EDGE_CANDIDATES:
        if os.path.exists(p):
            return p
    p = shutil.which("msedge")
    if p:
        return p
    raise FileNotFoundError("Không tìm thấy Microsoft Edge (msedge.exe)")


def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", s)  # liên kết nội bộ: giữ chữ
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def bo_frontmatter(md: str) -> tuple[dict, str]:
    """Tách khối YAML đầu file SKILL.md (chỉ lấy name/description dạng đơn giản)."""
    meta: dict = {}
    if md.startswith("---"):
        end = md.find("\n---", 3)
        if end > 0:
            khoi = md[3:end]
            m = re.search(r"^name:\s*(.+)$", khoi, re.M)
            if m:
                meta["name"] = m.group(1).strip()
            m = re.search(r"^description:\s*>?\s*\n?((?:\s{2,}.+\n?)+|.+)", khoi, re.M)
            if m:
                meta["description"] = " ".join(m.group(1).split())
            md = md[end + 4:]
    return meta, md


def md_to_html(md: str) -> str:
    lines = md.split("\n")
    h, i, n = [], 0, len(lines)
    while i < n:
        s = lines[i].strip()
        if not s or s.startswith("<!--"):
            i += 1
            continue
        if s.startswith("```"):
            i += 1
            khoi = []
            while i < n and not lines[i].strip().startswith("```"):
                khoi.append(lines[i])
                i += 1
            i += 1
            h.append("<pre>" + html.escape("\n".join(khoi)) + "</pre>")
            continue
        m = re.match(r"^(#{1,6}) (.*)$", s)
        if m:
            lv = len(m.group(1))
            h.append(f"<h{lv}>{inline(m.group(2))}</h{lv}>")
            i += 1
            continue
        if s.startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows
                     if not re.match(r"^\|(\s*:?-+:?\s*\|)+$", r)]
            if cells:
                t = ["<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells[0]) + "</tr></thead><tbody>"]
                t += ["<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in cells[1:]]
                h.append("".join(t) + "</tbody></table>")
            continue
        if re.match(r"^\s*(-|\d+\.) ", lines[i]):
            tag = "ol" if re.match(r"^\s*\d+\. ", lines[i]) else "ul"
            h.append(f"<{tag}>")
            while i < n and re.match(r"^\s*(-|\d+\.) ", lines[i]):
                depth = (len(lines[i]) - len(lines[i].lstrip())) // 2
                noi_dung = re.sub(r"^\s*(-|\d+\.) ", "", lines[i])
                i += 1
                # dòng tiếp nối (thụt lề, không phải mục mới) gộp vào mục hiện tại
                while (i < n and lines[i].startswith("  ") and lines[i].strip()
                       and not re.match(r"^\s*(-|\d+\.) ", lines[i])):
                    noi_dung += " " + lines[i].strip()
                    i += 1
                h.append(f'<li style="margin-left:{depth * 5}mm">{inline(noi_dung)}</li>')
            h.append(f"</{tag}>")
            continue
        if s.startswith(">"):
            h.append(f"<blockquote>{inline(s.lstrip('>').strip())}</blockquote>")
            i += 1
            continue
        h.append(f"<p>{inline(s)}</p>")
        i += 1
    return "\n".join(h)


def make_pdf(sections, title, subtitle, out_pdf, build_dir, meta_note, footer=None) -> int:
    build_dir = Path(build_dir)
    build_dir.mkdir(parents=True, exist_ok=True)
    out_pdf = Path(out_pdf)
    toc = "".join(f"<li>{html.escape(t)}" + (f"<br><span class='u'>{html.escape(u)}</span>" if u else "") + "</li>"
                  for t, u, _ in sections)
    parts = [f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<style>{CSS}</style></head><body>
<section class="cover"><div class="brand">Bao Bì Minh Phúc · MinhPhuc Toolkit</div>
<div><h1>{html.escape(title)}</h1><div class="sub">{html.escape(subtitle)}</div></div>
<div class="meta">{meta_note}</div></section>"""]
    if len(sections) > 1:
        parts.append(f'<section class="toc"><h2>Nội dung ({len(sections)} mục)</h2><ol>{toc}</ol></section>')
    for k, (t, u, md) in enumerate(sections):
        cls = "page" if (k > 0 or len(sections) > 1) else ""
        src = f'<div class="src">{html.escape(u)}</div>' if u else ""
        parts.append(f'<section class="{cls}">{src}{md_to_html(md)}</section>')
    parts.append("</body></html>")
    hf = build_dir / (out_pdf.stem + ".html")
    hf.write_text("\n".join(parts), encoding="utf-8")
    raw = build_dir / (out_pdf.stem + ".raw.pdf")
    if raw.exists():
        raw.unlink()
    subprocess.run([tim_edge(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--generate-pdf-document-outline", "--allow-file-access-from-files", "--virtual-time-budget=20000",
                    f"--user-data-dir={build_dir / 'edge-profile'}", f"--print-to-pdf={raw}", hf.as_uri()],
                   check=True, timeout=600, capture_output=True)
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    try:
        import pymupdf  # tuỳ chọn
    except ImportError:
        shutil.move(str(raw), out_pdf)
        return -1
    doc = pymupdf.open(raw)
    total = doc.page_count
    font_path = r"C:\Windows\Fonts\segoeui.ttf"
    font = pymupdf.Font(fontfile=font_path) if os.path.exists(font_path) else pymupdf.Font("helv")
    left = footer or f"Bao Bì Minh Phúc · {title}"
    for i, page in enumerate(doc):
        if i == 0:
            continue
        if not page.is_wrapped:
            page.wrap_contents()
        r = page.rect
        tw = pymupdf.TextWriter(r, color=(0.42, 0.46, 0.44))
        right = f"{i + 1} / {total}"
        tw.append((42, r.height - 24), left, font=font, fontsize=7.5)
        tw.append((r.width - 42 - font.text_length(right, 7.5), r.height - 24), right, font=font, fontsize=7.5)
        tw.write_text(page)
    doc.set_metadata({"title": title, "subject": subtitle, "author": "Nguyễn Hữu Sáng", "creator": "MinhPhuc Toolkit"})
    doc.save(out_pdf, garbage=3, deflate=True)
    doc.close()
    raw.unlink()
    return total
