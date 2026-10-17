# Danh mục dự án cải tiến ưu tiên cho Minh Phúc (đề xuất, 10/2026)

Xếp theo: tác động × dữ liệu đã có × công sức. Mọi dự án đều cần người phụ trách và chỉ số đo trước – sau. **[Đề xuất — Giám đốc / quản đốc duyệt]**

| # | Dự án | Vì sao (bằng chứng) | Chỉ số | Bắt đầu từ |
|---|---|---|---|---|
| 1 | **Tách "Lỗi khác" thành mã lỗi thật** | "Lỗi khác" là phần dư cho khớp số; 92/127 mã đang rơi vào ô Khác / Lỗi khác [MP] | % "Lỗi khác" không mã; tỷ lệ hư thật | Phiếu đếm 1–2 tuần (`templates/phieu-dem-loi-khac.md`), Pareto, chọn ô mới / 6 nhóm nguyên nhân |
| 2 | **Kiểm đầu đơn bắt buộc** ở mọi máy | Phần lớn phòng ngừa trong danh mục lỗi là "đo/canh tờ đầu" [MP] | Lỗi cấp 2A/1 lọt ra; khiếu nại | `templates/kiem-tra-dau-don.md` |
| 3 | **Khảo sát tem nhãn + sổ lý lịch máy** | Chưa biết hãng/model hầu hết máy → không có sách, phụ tùng, mã lỗi [MP-Web] | % máy có hồ sơ | `templates/khao-sat-tem-nhan-may.md` |
| 4 | **Bảng chuẩn keo và nhiệt tổ sóng** | Chưa có văn bản; cong tấm, phồng, keo chưa chín đứng đầu danh sách 6 lỗi hay gặp của tổ sóng (xếp theo kinh nghiệm ngành) [MP] | Tỷ lệ TS-11/12/14; ECT | Ghi thông số thợ chính đang dùng → thử → chuẩn hoá |
| 5 | **Định mức tốc độ mục tiêu theo máy và loại đơn** | Tốc độ mục tiêu trên MES là số mặc định chưa duyệt [MP-MES] | OEE có nghĩa | Lấy phân vị 75 % tốc độ lúc chạy 1–2 tháng theo nhóm sản phẩm |
| 6 | **SMED máy in và máy bế** | Nhiều đơn nhỏ; báo giá 4 giờ, mẫu 1–3 ngày [MP-Web] | Phút pha mực/chuẩn bị mỗi đơn | Video đổi đơn, tách việc trong/ngoài |
| 7 | **Lắp cảm biến nhíp máy bế** | Máy bế đếm đôi → chênh đếm (BE-17); phần mềm đã làm sẵn [MP-MES] | Chênh đếm máy bế | Lắp cảm biến, bật ô Cài đặt |
| 8 | **Bảng chuẩn tấm (công thức giấy ↔ ECT/BCT)** | Chưa có số ECT/BCT theo công thức tấm; QC đo theo lô | ECT/BCT theo công thức, chi phí giấy | Ghi QC theo phiếu SX, gom theo kết cấu giấy |
| 9 | **COA và đánh giá nhà cung cấp giấy** | Chưa có COA từng nhà cung cấp trong hồ sơ [MP] | % lô có COA; lô không đạt | `templates/phieu-kiem-tra-giay-cuon.md` |
| 10 | **In ép bẹp sóng ở máy in** | Mất BCT âm thầm [KN ngành] | Độ dày trước/sau in; ECT trước/sau | Đo trên 3 đơn mỗi máy |
| 11 | **Hao hụt giấy tổ sóng** | Nguyên liệu ~75 % giá thành [AOPack] | % hao biên, đầu cuộn, chuyển đơn | Ghi khổ giấy SD vs khổ LT; ghép khổ |
| 12 | **5S kho khuôn – bản** | Lỗi lấy nhầm bản/khuôn (FX-13, BE-13) là lỗi cấp 1 | Số lần lấy nhầm; thời gian tìm | Sổ vị trí BI/BK/KB trên MES |
| 13 | **Huấn luyện thợ theo ma trận kỹ năng** | Chưa có ma trận chính thức | % ô kỹ năng đạt | skill `mp-dao-tao` |
| 14 | **An toàn: đánh giá rủi ro từng máy + LOTO viết riêng** | Chưa có đánh giá rủi ro theo máy thật [MP] | % máy có quy trình LOTO | `templates/danh-gia-rui-ro-may.md` |

Cập nhật bảng này khi dự án đóng (kết quả) và khi có dữ liệu mới; ghi ngày.
