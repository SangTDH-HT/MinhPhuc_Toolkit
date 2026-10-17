"""Kiểm các công thức bằng ví dụ có sẵn trong sổ tay / web Minh Phúc.

Chạy:  python -m unittest discover -s tools/tinh-toan/tests
"""

import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mptinh import chat_luong, do_ben, ket_cau, logistics, san_xuat  # noqa: E402
from mptinh.__main__ import main, so  # noqa: E402


class TestDoBen(unittest.TestCase):
    def test_bct_yeu_cau_vi_du_web(self):
        # Web MP: S.F 5, 8 tầng, 12 kg → 420 kgf
        self.assertEqual(do_ben.bct_yeu_cau(5, 8, 12), 420)

    def test_mckee_vi_du_so_tay(self):
        # Sổ tay chất lượng: ECT 5.000 N/m, t 4 mm, 400 × 300 → ~2.196 N ≈ 224 kgf
        n = do_ben.mckee_bct_n(5.0, 4, 400, 300)
        self.assertAlmostEqual(n, 2196, delta=1)
        self.assertAlmostEqual(n / do_ben.G, 224, delta=0.5)

    def test_ect_can_dao_nguoc(self):
        n = do_ben.mckee_bct_n(5.0, 4, 400, 300)
        self.assertAlmostEqual(do_ben.ect_can_kn_m(n / do_ben.G, 4, 400, 300), 5.0, places=6)

    def test_maltenfort_seth(self):
        # 0,7 × (3 + 3 + 1,43 × 2) = 6,202
        self.assertAlmostEqual(do_ben.ect_maltenfort_seth([3, 3], [(2, 1.43)]), 6.202, places=3)

    def test_do_am(self):
        self.assertAlmostEqual(do_ben.he_so_do_am(80), 0.70, places=6)
        self.assertAlmostEqual(do_ben.am_can_bang(80), 11.39, places=2)

    def test_sai_dau_vao(self):
        with self.assertRaises(ValueError):
            do_ben.bct_yeu_cau(5, 0, 12)


class TestKetCau(unittest.TestCase):
    def test_phoi_vi_du(self):
        kq = ket_cau.phoi_rsc(400, 300, 250, song="C", tai_dan=35, dinh_luong=480)
        self.assertEqual((kq.lan_dai, kq.lan_rong, kq.lan_cao), (404, 304, 258))
        self.assertEqual(kq.dai_phoi, 1451)
        self.assertEqual(kq.rong_phoi, 562)
        self.assertAlmostEqual(kq.dien_tich_m2, 0.815462, places=6)
        self.assertAlmostEqual(kq.khoi_luong_g, 391.4, delta=0.1)

    def test_lan_fefco_song_b(self):
        # FEFCO QC ví dụ: sóng B t ≈ 3, 650 × 400 × 250 → 653 × 403 × 256
        kq = ket_cau.phoi_rsc(650, 400, 250, t=3)
        self.assertEqual((kq.lan_dai, kq.lan_rong, kq.lan_cao), (653, 403, 256))

    def test_dinh_luong(self):
        kq = ket_cau.dinh_luong_tam("150,120C,150")
        self.assertAlmostEqual(kq.tong, 474.0, places=1)
        kq2 = ket_cau.dinh_luong_tam("150/120C/150", keo_moi_duong=10, he_so={"C": 1.43})
        self.assertAlmostEqual(kq2.tong, 150 + 120 * 1.43 + 150 + 20, places=1)

    def test_song_la(self):
        with self.assertRaises(ValueError):
            ket_cau.do_day("Z")


class TestLogistics(unittest.TestCase):
    def test_cbm_va_container_nhu_web(self):
        c = logistics.cbm(40, 30, 30)
        self.assertAlmostEqual(c, 0.036, places=6)
        self.assertEqual(logistics.so_thung_container(c), {"20'": 779, "40'": 1581, "40'HC": 1794})

    def test_pallet_module(self):
        self.assertEqual(logistics.pallet(400, 300, 1200, 800).so_thung_lop, 8)
        self.assertEqual(logistics.pallet(600, 400, 1200, 800).so_thung_lop, 4)
        self.assertEqual(logistics.pallet(550, 366, 1100, 1100).so_thung_lop, 6)
        self.assertEqual(logistics.pallet(366, 275, 1100, 1100).so_thung_lop, 12)

    def test_pallet_so_lop(self):
        kq = logistics.pallet(400, 300, 1200, 800, cao_thung=250, cao_toi_da=1650, cao_pallet=150)
        self.assertEqual((kq.so_lop, kq.tong), (6, 48))


class TestChatLuong(unittest.TestCase):
    def test_aql_vi_du_so_tay(self):
        # Lô 20.000, AQL 1,5 → 80 mẫu, Ac 3
        self.assertEqual(chat_luong.aql(20000, 1.5), (80, 3, 4))
        self.assertEqual(chat_luong.aql(20000, 6.5), (80, 8, 9))
        self.assertEqual(chat_luong.aql(8, 2.5), (8, 1, 2))

    def test_aql_qua_lon(self):
        with self.assertRaises(ValueError):
            chat_luong.aql(200000, 1.5)


class TestSanXuat(unittest.TestCase):
    def test_san_luong_luat_mes(self):
        kq = san_xuat.san_luong(2750, 250, 2, 6000, 60)
        self.assertEqual((kq.nhip_thuc_hien, kq.san_luong, kq.thua_thieu, kq.dat), (3000, 6000, 0, 5940))

    def test_oee_vi_du(self):
        kq = san_xuat.oee(chay=300, kokh=60, nhip=18000, muc_tieu=70, san_luong_=36000, loi=360, pha_muc=60)
        self.assertAlmostEqual(kq.san_sang, 300 / 420)
        self.assertAlmostEqual(kq.hieu_nang, 60 / 70)
        self.assertAlmostEqual(kq.chat_luong, 0.99)
        self.assertAlmostEqual(kq.oee, 0.6061, places=4)
        self.assertAlmostEqual(kq.san_sang * kq.hieu_nang, kq.toc_do_binh_quan / 70)

    def test_kho_giay(self):
        kq = san_xuat.kho_giay(520, 1600)
        self.assertEqual(kq.so_tam, 3)
        self.assertAlmostEqual(kq.bien, 40)

    def test_pareto(self):
        out = san_xuat.pareto({"FX-04": 35, "FX-05": 50, "FX-10": 15})
        self.assertEqual(out[0][0], "FX-05")
        self.assertAlmostEqual(out[-1][3], 100.0)


class TestCLI(unittest.TestCase):
    def chay(self, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            ma = main(list(args))
        return ma, buf.getvalue()

    def test_dinh_dang_so(self):
        self.assertEqual(so(1234.5), "1.234,5")

    def test_cac_lenh(self):
        for args in (
            ("bct-can", "--sf", "5", "--tang", "8", "--kg", "12", "--rh", "80"),
            ("mckee", "--dai", "400", "--rong", "300", "--song", "C", "--ect", "5", "--bct", "300"),
            ("ect", "--mat", "3.1/3.1", "--song", "2.2:1.43"),
            ("dinh-luong", "--cau-truc", "150,120C,150"),
            ("phoi-rsc", "--dai", "400", "--rong", "300", "--cao", "250", "--song", "C", "--dinh-luong", "480"),
            ("cbm", "--dai", "40", "--rong", "30", "--cao", "30"),
            ("pallet", "--dai", "400", "--rong", "300", "--cao", "250", "--cao-toi-da", "1650"),
            ("aql", "--lo", "20000", "--aql", "1.5"),
            ("oee", "--chay", "300", "--kokh", "60", "--pha-muc", "60", "--nhip", "18000", "--muc-tieu", "70",
             "--san-luong", "36000", "--loi", "360"),
            ("san-luong", "--nhip", "2750", "--chay-truoc", "250", "--so-con", "2", "--ke-hoach", "6000"),
            ("kho-giay", "--rong-tam", "520", "--kho", "1600,1800"),
            ("do-am", "--rh", "80"),
        ):
            ma, out = self.chay(*args)
            self.assertEqual(ma, 0, args)
            self.assertTrue(out.strip(), args)


if __name__ == "__main__":
    unittest.main()
