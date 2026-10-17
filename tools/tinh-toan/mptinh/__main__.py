"""Dòng lệnh: python -m mptinh <lệnh> [tham số]   (chạy trong thư mục tools/tinh-toan)

Gõ  python -m mptinh -h  để xem danh sách lệnh,  python -m mptinh <lệnh> -h  để xem tham số.
"""

from __future__ import annotations

import argparse
import sys

from . import chat_luong, do_ben, ket_cau, logistics, san_xuat


def so(x: float, nd: int = 1) -> str:
    """Định dạng số kiểu Việt Nam: 1.234,5"""
    s = f"{x:,.{nd}f}"
    return s.replace(",", "_").replace(".", ",").replace("_", ".")


def pct(x: float, nd: int = 1) -> str:
    return so(x * 100, nd) + " %"


def _he_so(chuoi: str | None) -> dict[str, float]:
    if not chuoi:
        return {}
    out = {}
    for cap in chuoi.split(","):
        k, v = cap.split("=")
        out[k.strip().upper()] = float(v.replace(",", "."))
    return out


def lenh_dinh_luong(a):
    kq = ket_cau.dinh_luong_tam(a.cau_truc, a.keo, _he_so(a.he_so))
    print(f"Cấu trúc: {a.cau_truc}")
    for i, g, k, d in kq.chi_tiet:
        loai = "giấy mặt" if k == 1.0 else f"giấy sóng × {so(k, 2)}"
        print(f"  lớp {i}: {so(g, 0)} g/m² ({loai}) → {so(d)} g/m²")
    if kq.keo:
        print(f"  keo khô: {so(kq.keo)} g/m²")
    print(f"Định lượng tấm ≈ {so(kq.tong)} g/m²   [hệ số co là KN ngành — đo thật thì sửa --he-so]")


def lenh_phoi_rsc(a):
    kq = ket_cau.phoi_rsc(a.dai, a.rong, a.cao, a.song, a.t, a.tai_dan, a.dinh_luong)
    print(f"Thùng RSC 0201, lọt lòng {so(a.dai, 0)} × {so(a.rong, 0)} × {so(a.cao, 0)} mm, t = {so(kq.t)} mm")
    print(f"  Khoảng cách lằn (FEFCO): {so(kq.lan_dai)} × {so(kq.lan_rong)} × {so(kq.lan_cao)} mm")
    print(f"  Nắp: {so(kq.nap)} mm · tai dán {so(a.tai_dan, 0)} mm")
    print(f"  Phôi ≈ {so(kq.dai_phoi, 0)} × {so(kq.rong_phoi, 0)} mm = {so(kq.dien_tich_m2, 3)} m²")
    pb = kq.phu_bi
    print(f"  Phủ bì gần đúng: {so(pb[0], 0)} × {so(pb[1], 0)} × {so(pb[2], 0)} mm")
    if kq.khoi_luong_g:
        print(f"  Khối lượng thùng ≈ {so(kq.khoi_luong_g, 0)} g (chưa tính hao hụt)")
    print("  [Ước lượng — bảng bù kích thước của phòng thiết kế thắng]")


def lenh_bct_can(a):
    kgf = do_ben.bct_yeu_cau(a.sf, a.tang, a.kg)
    print(f"BCT yêu cầu = {so(a.sf, 0)} × ({a.tang} − 1) × {so(a.kg)} kg = {so(kgf)} kgf ≈ {so(kgf * do_ben.G / 1000, 2)} kN")
    print(f"  S.F {so(a.sf, 0)}: {do_ben.HE_SO_AN_TOAN.get(int(a.sf), 'tự chọn')}")
    if a.rh:
        h = do_ben.he_so_do_am(a.rh)
        print(f"  Ở {so(a.rh, 0)} % RH thùng còn ~{pct(h, 0)} sức nén → BCT đo ở 50 % RH nên ≥ {so(kgf / h)} kgf")
    print("  [Định hướng — chốt bằng đo mẫu thật]")


def lenh_mckee(a):
    t = a.t if a.t else ket_cau.do_day(a.song)
    if a.ect is not None:
        n = do_ben.mckee_bct_n(a.ect, t, a.dai, a.rong)
        print(f"BCT ≈ 5,87 × {so(a.ect, 2)} kN/m × √({so(t)} mm × chu vi {so(do_ben.chu_vi_m(a.dai, a.rong), 3)} m)"
              f" = {so(n, 0)} N ≈ {so(n / do_ben.G, 0)} kgf")
    if a.bct is not None:
        e = do_ben.ect_can_kn_m(a.bct, t, a.dai, a.rong)
        print(f"Muốn BCT {so(a.bct, 0)} kgf cần ECT ≈ {so(e, 2)} kN/m")
    if a.ect is None and a.bct is None:
        print("Cần --ect (tính BCT) hoặc --bct (tính ECT cần)")
    print("  [McKee rút gọn — định hướng; đo mẫu thật để chốt]")


def lenh_ect(a):
    mat = [float(x.replace(",", ".")) for x in a.mat.split("/")]
    song = []
    for tok in a.song.split("/"):
        s, k = tok.split(":") if ":" in tok else (tok, "1.45")
        song.append((float(s.replace(",", ".")), float(k.replace(",", "."))))
    e = do_ben.ect_maltenfort_seth(mat, song)
    print(f"ECT ≈ 0,7 × ({' + '.join(so(x, 2) for x in mat)} + "
          f"{' + '.join(f'{so(k, 2)} × {so(s, 2)}' for s, k in song)}) = {so(e, 2)} kN/m")
    print("  [Maltenfort–Seth — SCT chiều ngang (CD), kN/m]")


def lenh_do_am(a):
    h = do_ben.he_so_do_am(a.rh, a.rh_chuan)
    print(f"Từ {so(a.rh_chuan, 0)} % RH sang {so(a.rh, 0)} % RH: sức nén còn ~{pct(h, 0)}")
    print(f"Độ ẩm cân bằng kraft nâu ở {so(a.rh, 0)} % RH ≈ {so(do_ben.am_can_bang(a.rh))} %")


def lenh_cbm(a):
    c = logistics.cbm(a.dai, a.rong, a.cao, a.don_vi)
    print(f"CBM một thùng = {so(c, 4)} m³ (kích thước thùng ở trạng thái GIAO)")
    if a.so_thung:
        print(f"  {a.so_thung} thùng = {so(c * a.so_thung, 2)} m³")
    for k, v in logistics.so_thung_container(c, a.he_so).items():
        print(f"  Container {k}: ~{so(v, 0)} thùng (hệ số khai thác {pct(a.he_so, 0)})")
    print("  [Xếp thử một lớp rồi nhân lên để chắc; kiểm cả giới hạn tải trọng]")


def lenh_pallet(a):
    pd, pr = (float(x) for x in a.pallet.lower().split("x"))
    kq = logistics.pallet(a.dai, a.rong, pd, pr, a.cao, a.cao_toi_da, a.cao_pallet)
    print(f"Pallet {so(pd, 0)} × {so(pr, 0)} mm, thùng phủ bì {so(a.dai, 0)} × {so(a.rong, 0)} mm")
    print(f"  {kq.so_thung_lop} thùng/lớp — {kq.cach_xep}; phủ kín {so(kq.phu_kin_pct, 0)} % mặt pallet")
    if kq.so_lop is not None:
        print(f"  {kq.so_lop} lớp (cao tối đa {so(a.cao_toi_da, 0)} mm gồm pallet {so(a.cao_pallet, 0)} mm) → {kq.tong} thùng/pallet")
        print("  Kiểm BCT cho số lớp này: python -m mptinh bct-can --tang <số lớp> ...")


def lenh_aql(a):
    n, ac, re_ = chat_luong.aql(a.lo, a.aql)
    print(f"Lô {so(a.lo, 0)} cái, AQL {so(a.aql, 2)}: lấy {n} mẫu · chấp nhận ≤ {ac} lỗi · loại lô khi ≥ {re_} lỗi")
    print("  Cấp lỗi FEFCO: " + "; ".join(f"{k}: {v}" for k, v in chat_luong.CAP_LOI.items()))


def lenh_oee(a):
    kq = san_xuat.oee(a.chay, a.kokh, a.nhip, a.muc_tieu, a.san_luong, a.loi, a.pha_muc)
    print(f"Thời gian tổ máy làm chủ = {so(kq.thoi_gian_lam_chu)} phút")
    print(f"  Sẵn sàng   = {pct(kq.san_sang)}")
    print(f"  Hiệu năng  = {pct(kq.hieu_nang)}")
    print(f"  Chất lượng = {pct(kq.chat_luong)}")
    print(f"  OEE        = {pct(kq.oee)}")
    print(f"  Tốc độ bình quân = {so(kq.toc_do_binh_quan)} nhịp/phút ({pct(kq.toc_do_binh_quan / a.muc_tieu)} mục tiêu)")


def lenh_san_luong(a):
    kq = san_xuat.san_luong(a.nhip, a.chay_truoc, a.so_con, a.ke_hoach, a.loi)
    print(f"Nhịp thực hiện = {so(a.nhip, 0)} + {so(a.chay_truoc, 0)} = {so(kq.nhip_thuc_hien, 0)} nhịp")
    print(f"Sản lượng = {so(kq.nhip_thuc_hien, 0)} × {so(a.so_con, 0)} con = {so(kq.san_luong, 0)}")
    if kq.thua_thieu is not None:
        dau = "thừa" if kq.thua_thieu > 0 else ("thiếu" if kq.thua_thieu < 0 else "đủ")
        print(f"So kế hoạch {so(a.ke_hoach, 0)}: {dau} {so(abs(kq.thua_thieu), 0)}")
    if a.loi:
        print(f"Đạt = {so(kq.dat, 0)} (trừ {so(a.loi, 0)} lỗi)")


def lenh_kho_giay(a):
    for kho in [float(x) for x in a.kho.split(",")]:
        kq = san_xuat.kho_giay(a.rong_tam, kho, a.so_tam, a.bien)
        trang_thai = "" if kq.dat else "  ⚠ không đủ biên"
        print(f"Khổ {so(kho, 0)} mm: {kq.so_tam} tấm × {so(a.rong_tam, 0)} = {so(kq.rong_dung, 0)} mm,"
              f" biên {so(kq.bien, 0)} mm ({so(kq.hao_bien_pct)} %){trang_thai}")


def lenh_pareto(a):
    du_lieu = san_xuat.doc_csv_pareto(a.file, a.cot_ma, a.cot_so)
    for k, v, p, cong in san_xuat.pareto(du_lieu):
        print(f"{k:<14} {so(v, 0):>10}  {so(p):>6} %  tích luỹ {so(cong):>6} %")


def tao_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mptinh", description="Máy tính kỹ thuật Bao Bì Minh Phúc")
    sub = p.add_subparsers(dest="lenh", required=True)

    s = sub.add_parser("dinh-luong", help="Định lượng tấm từ cấu trúc giấy")
    s.add_argument("--cau-truc", required=True, help="vd 150,120C,150 hoặc 170,120B,140,120C,170")
    s.add_argument("--keo", type=float, default=0.0, help="keo khô mỗi đường keo g/m² (mặc định 0)")
    s.add_argument("--he-so", help="ghi đè hệ số co, vd C=1.43,B=1.36")
    s.set_defaults(ham=lenh_dinh_luong)

    s = sub.add_parser("phoi-rsc", help="Lằn, phôi, diện tích, khối lượng thùng RSC 0201")
    s.add_argument("--dai", type=float, required=True)
    s.add_argument("--rong", type=float, required=True)
    s.add_argument("--cao", type=float, required=True)
    g = s.add_mutually_exclusive_group(required=True)
    g.add_argument("--song", help="E, B, C, A, BE, BC, BA")
    g.add_argument("--t", type=float, help="độ dày tấm đo được (mm)")
    s.add_argument("--tai-dan", type=float, default=35.0)
    s.add_argument("--dinh-luong", type=float, help="g/m² tấm để tính khối lượng")
    s.set_defaults(ham=lenh_phoi_rsc)

    s = sub.add_parser("bct-can", help="BCT yêu cầu = S.F × (n − 1) × W")
    s.add_argument("--sf", type=float, required=True, help="3, 4 hoặc 5")
    s.add_argument("--tang", type=int, required=True, help="số tầng xếp chồng")
    s.add_argument("--kg", type=float, required=True, help="khối lượng một thùng đã đóng hàng")
    s.add_argument("--rh", type=float, help="độ ẩm kho (%) để bù")
    s.set_defaults(ham=lenh_bct_can)

    s = sub.add_parser("mckee", help="BCT từ ECT (McKee) hoặc ECT cần cho một BCT")
    s.add_argument("--dai", type=float, required=True, help="dài thùng mm")
    s.add_argument("--rong", type=float, required=True, help="rộng thùng mm")
    g = s.add_mutually_exclusive_group(required=True)
    g.add_argument("--song")
    g.add_argument("--t", type=float)
    s.add_argument("--ect", type=float, help="kN/m")
    s.add_argument("--bct", type=float, help="kgf cần đạt")
    s.set_defaults(ham=lenh_mckee)

    s = sub.add_parser("ect", help="ECT từ SCT giấy (Maltenfort–Seth)")
    s.add_argument("--mat", required=True, help="SCT các lớp mặt kN/m, vd 3.1/3.1")
    s.add_argument("--song", required=True, help="SCT giấy sóng[:hệ số co], vd 2.2:1.43")
    s.set_defaults(ham=lenh_ect)

    s = sub.add_parser("do-am", help="Ảnh hưởng độ ẩm tới sức nén")
    s.add_argument("--rh", type=float, required=True)
    s.add_argument("--rh-chuan", type=float, default=50.0)
    s.set_defaults(ham=lenh_do_am)

    s = sub.add_parser("cbm", help="CBM và số thùng trong container")
    s.add_argument("--dai", type=float, required=True)
    s.add_argument("--rong", type=float, required=True)
    s.add_argument("--cao", type=float, required=True)
    s.add_argument("--don-vi", default="cm", choices=list(logistics.DON_VI_MET))
    s.add_argument("--he-so", type=float, default=0.85)
    s.add_argument("--so-thung", type=int)
    s.set_defaults(ham=lenh_cbm)

    s = sub.add_parser("pallet", help="Số thùng mỗi lớp pallet")
    s.add_argument("--dai", type=float, required=True, help="phủ bì thùng mm")
    s.add_argument("--rong", type=float, required=True)
    s.add_argument("--pallet", default="1200x800")
    s.add_argument("--cao", type=float, help="cao thùng mm")
    s.add_argument("--cao-toi-da", type=float, help="chiều cao kiện tối đa mm (gồm pallet)")
    s.add_argument("--cao-pallet", type=float, default=150)
    s.set_defaults(ham=lenh_pallet)

    s = sub.add_parser("aql", help="Cỡ mẫu và số chấp nhận (FEFCO / ISO 2859-1)")
    s.add_argument("--lo", type=int, required=True)
    s.add_argument("--aql", type=float, required=True, choices=chat_luong.AQL_COT)
    s.set_defaults(ham=lenh_aql)

    s = sub.add_parser("oee", help="OEE theo định nghĩa Minh Phúc")
    s.add_argument("--chay", type=float, required=True, help="phút chạy máy")
    s.add_argument("--kokh", type=float, required=True, help="phút ngừng không kế hoạch")
    s.add_argument("--pha-muc", type=float, default=0.0, help="phút pha mực (máy in)")
    s.add_argument("--nhip", type=float, required=True)
    s.add_argument("--muc-tieu", type=float, required=True, help="nhịp/phút")
    s.add_argument("--san-luong", type=float, required=True)
    s.add_argument("--loi", type=float, default=0.0)
    s.set_defaults(ham=lenh_oee)

    s = sub.add_parser("san-luong", help="Sản lượng theo luật MES (máy bế: nhịp × số con; máy in: --so-con 1)")
    s.add_argument("--nhip", type=float, required=True)
    s.add_argument("--chay-truoc", type=float, default=0.0)
    s.add_argument("--so-con", type=float, default=1.0)
    s.add_argument("--ke-hoach", type=float)
    s.add_argument("--loi", type=float, default=0.0)
    s.set_defaults(ham=lenh_san_luong)

    s = sub.add_parser("kho-giay", help="Số tấm trên khổ giấy và hao biên")
    s.add_argument("--rong-tam", type=float, required=True, help="tổng rộng một tấm mm")
    s.add_argument("--kho", required=True, help="khổ giấy mm, nhiều khổ cách nhau dấu phẩy")
    s.add_argument("--so-tam", type=int)
    s.add_argument("--bien", type=float, default=0.0, help="biên xén tối thiểu mm")
    s.set_defaults(ham=lenh_kho_giay)

    s = sub.add_parser("pareto", help="Pareto từ CSV (cột ma, so_luong)")
    s.add_argument("--file", required=True)
    s.add_argument("--cot-ma", default="ma")
    s.add_argument("--cot-so", default="so_luong")
    s.set_defaults(ham=lenh_pareto)
    return p


def main(argv: list[str] | None = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    a = tao_parser().parse_args(argv)
    try:
        a.ham(a)
    except ValueError as e:
        print(f"Lỗi: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
