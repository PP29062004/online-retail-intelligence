# Yêu cầu nghiệp vụ và đặc tả báo cáo bán lẻ

**Phạm Thanh Phúc** · Đồ án chuyên ngành Hệ thống thông tin, HUTECH

## BRD · Nhu cầu của bộ phận bán hàng

Bộ dữ liệu Online Retail II lưu mỗi mặt hàng trên một dòng hóa đơn. Một đơn có thể xuất hiện ở nhiều dòng, hóa đơn hủy có ký hiệu riêng và một số giao dịch thiếu mã khách. Khi đọc trực tiếp từ Excel, việc tổng hợp doanh thu theo tháng khá dễ, nhưng sẽ khó trả lời ngay nên chuẩn bị hàng ở đâu, mã nào bán đều và khách nào đã quay lại mua.

Tôi đặt bài toán vào một kỳ họp bán hàng trước mùa cao điểm. Quản lý bán hàng cần nhìn chênh lệch giữa các kỳ và giữa các thị trường. Người phụ trách khách hàng cần biết doanh thu đến từ người mới hay người đã từng mua. Bộ phận vận hành cần xem số đơn và số khách đứng sau doanh thu của một mã hàng trước khi đưa mã đó vào danh sách chuẩn bị hàng. Đây là các vai trò giả định cho đồ án trên dữ liệu công khai.

| Mã | Yêu cầu nghiệp vụ | Quyết định cần hỗ trợ |
| --- | --- | --- |
| BR-01 | Theo dõi doanh thu, đơn hàng, khách và giá trị đơn theo kỳ. So sánh cùng số ngày khi kỳ báo cáo chưa đủ. | Chọn kỳ và thị trường cần xem kỹ trước khi chuẩn bị cao điểm. |
| BR-02 | Phân biệt khách mua lần đầu và khách đã từng mua trong lịch sử quan sát. Xem thêm phân khúc RFM. | Chọn nhóm khách để ưu tiên giữ chân hoặc thử nhắc mua lại. |
| BR-03 | Xem doanh thu theo quốc gia và đánh giá mức độ tập trung theo hóa đơn của từng mã hàng. | Chọn thị trường cần rà soát và mã hàng cần kiểm tra trước khi đề xuất nhập. |

## SRS · Ba trang báo cáo

| Yêu cầu | Trang và cách hoạt động | Tiêu chí kiểm tra |
| --- | --- | --- |
| FR-01 · BR-01 | **Tổng quan bán hàng.** Lọc theo năm, tháng, thị trường. Hiển thị doanh thu, số đơn, số khách và giá trị đơn trung bình. | Chọn 2011 và Pháp. Các thẻ lần lượt hiện **£199.336,00**, **368 đơn**, **84 khách** và **£541,67/đơn**. |
| FR-02 · BR-01 | **Tổng quan bán hàng.** So sánh doanh thu tháng với cùng ngày lịch năm trước. Biểu đồ ngày giới hạn ở 31 ngày cuối của kỳ đã chọn, với số đơn khi rê chuột. | Chọn tháng 12/2011, mọi thị trường. Kỳ 1–9/12 có **£517.208,44**, đối chiếu với **£310.656,37** của ngày 1–9/12/2010. |
| FR-03 · BR-02 | **Khách hàng.** So sánh số khách và doanh thu theo tháng của hai nhóm mua lần đầu và quay lại. | Tháng 11/2011 có **191** khách mua lần đầu trong dữ liệu và **1.473** khách quay lại. |
| FR-04 · BR-02 | **Khách hàng.** Hiển thị số khách, doanh thu theo RFM và bảng Top 8 khách theo doanh thu. | Chọn 2011 và Pháp. Ba nhóm giá trị cao, trung bình và thấp lần lượt có **37**, **21** và **26** khách. Tổng khớp **84** khách. |
| FR-05 · BR-03 | **Thị trường và mã hàng.** Hiển thị doanh thu trên bản đồ quốc gia và bảng thị trường. Chọn một vùng trên bản đồ để lọc các visual cùng trang. | Chọn Úc trên bản đồ. Bảng thị trường thu về Úc và bảng mã hàng đổi theo phạm vi đã chọn. Bỏ chọn để quay lại toàn bộ thị trường. |
| FR-06 · BR-03 | **Thị trường và mã hàng.** Xếp hạng 10 mã theo doanh thu, kèm số đơn, số khách và tỷ trọng doanh thu của hóa đơn lớn nhất của từng mã. | Toàn kỳ, mã `22423` đạt **£277.656,25** từ **3.317 đơn**. Mã `23843` có **100% doanh thu** từ một hóa đơn. |

Ba trang dùng bộ lọc năm, tháng và thị trường, nhãn tiếng Việt và đơn vị tiền GBP. Mỗi chỉ số cần truy về được cột dữ liệu và quy tắc tính. Các bước lọc phải có số dòng trước và sau để chạy lại và đối soát.

## Quy tắc tính và giới hạn dữ liệu

- Một dòng là một mặt hàng trên hóa đơn. Số đơn đếm mã hóa đơn khác nhau, số khách đếm mã khách khác nhau trong phạm vi lọc. Giá trị đơn trung bình bằng doanh thu chia số đơn và để trống khi không có đơn.
- Loại hóa đơn có mã bắt đầu bằng `C`, dòng thiếu trường bắt buộc, số lượng hoặc đơn giá không dương hay không hữu hạn. Loại dòng trùng hoàn toàn sau khi chuẩn hóa. Hai dòng có cùng giá trị vẫn có thể là hai lần nhập hợp lệ, nên pipeline lưu số lượng loại để kiểm tra.
- Doanh thu bằng số lượng nhân đơn giá của các dòng hợp lệ. Để tính doanh thu sau hoàn hủy hoặc biên lợi nhuận cần thêm thông tin đối soát và giá vốn. Các mã như `POST` và `M` có thể xuất hiện trong bảng xếp hạng.
- Khách mua lần đầu là khách có giao dịch hợp lệ đầu tiên trong tháng trên toàn bộ lịch sử quan sát. Ví dụ, “lần đầu” trong tháng 12/2009 chỉ cho biết giao dịch đầu tiên có mặt trong bộ dữ liệu.
- RFM dùng số ngày từ lần mua gần nhất, số hóa đơn riêng biệt và tổng giá trị mua, tính tại ngày **10/12/2011**. Chấm 1–5 điểm theo thứ hạng phân vị mỗi chỉ tiêu, gán nhóm cao từ 12–15, trung bình từ 8–11 và thấp từ 3–7 điểm. Khi lọc kỳ, số khách và doanh thu thay đổi theo giao dịch, còn nhãn RFM giữ theo ngày chốt.
- Quốc gia lấy từ trường `Country` của khách hàng. Bảng vẫn giữ đủ giá trị địa lý trong dữ liệu, kể cả nhãn tổng hợp hoặc nhãn chưa ghép được với hình trên bản đồ.

Nội dung dựa trên câu hỏi phân tích ở mục 1.4, xử lý dữ liệu ở mục 5.2–5.3 và phần dashboard ở mục 6.2–6.6 của báo cáo đồ án. Bản đặc tả bổ sung so sánh cùng kỳ, phân biệt khách mới và quay lại, bản đồ và tiêu chí kiểm tra cho bản tiếng Việt ba trang. [Tóm tắt đồ án ban đầu](case_study.md) · [Tình huống kiểm thử](use_cases.md)
