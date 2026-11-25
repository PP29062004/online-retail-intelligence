# Use case báo cáo bán lẻ Power BI

Năm tình huống dưới đây bám theo năm câu hỏi phân tích trong mục 1.4 của báo cáo đồ án. Tên trang, tên bộ lọc và số đối soát lấy từ bản Power BI trong repo. Người dùng trong các tình huống này là người xem báo cáo doanh thu. Báo cáo cần được nạp dữ liệu trước khi thực hiện các bước.

## UC-01 Xem doanh thu và số đơn của một thị trường

Mở **Sales overview**, chọn năm ở **Sales year** và quốc gia ở **Customer market**. Đọc bốn thẻ doanh thu, số đơn, số khách có giao dịch và giá trị trung bình một đơn. Một hóa đơn có nhiều dòng hàng vẫn được đếm là một đơn.

**Kiểm tra.** Chọn năm **2011** và **France**. Bốn thẻ lần lượt cho **£199.336,00**, **368 đơn**, **84 khách** và **£541,67 mỗi đơn**.

## UC-02 Xem doanh thu biến động theo tháng

Báo cáo đồ án minh họa bằng câu hỏi xem doanh thu tháng 10 ở Đức. Trên **Sales overview**, chọn **Germany** và năm cần xem, rồi rê chuột vào điểm tháng 10 trên biểu đồ **Monthly sales revenue**. Có thể xem các điểm liền trước và sau để biết mức doanh thu đó cao hay thấp so với những tháng gần nhất.

**Kiểm tra.** Với năm **2011**, điểm tháng 10 tại Đức là **£31.628,42**. Ở chế độ xem toàn kỳ, tháng 12/2011 chỉ có giao dịch từ ngày 1 đến ngày 9.

## UC-03 Tìm những mã hàng đóng góp nhiều doanh thu

Trên **Sales overview**, giữ bộ lọc của kỳ đang xem và đọc biểu đồ **Top 10 stock codes by revenue**. Rê chuột vào thanh để đọc mô tả và mã hàng. Báo cáo dùng mã để gộp các dòng của cùng mặt hàng khi mô tả có thay đổi. Danh sách cũng có thể xuất hiện các mã thu phí như bưu phí.

**Kiểm tra.** Khi bỏ lọc năm và thị trường, mã **22423** (*Regency Cakestand 3 Tier*) đứng đầu với **£277.656,25**.

## UC-04 Xem doanh thu tập trung ở thị trường nào

Trên **Sales overview**, bỏ lọc quốc gia để xem **Top 6 customer markets by revenue** và so sánh Vương quốc Anh với các thị trường còn lại trong bảng xếp hạng. Khi cần tính tỷ trọng của một thị trường, lấy doanh thu thị trường chia cho tổng doanh thu của tất cả thị trường trong cùng kỳ.

**Kiểm tra.** Với toàn bộ thời gian, **United Kingdom** đứng đầu với **£14.389.234,92**, tương đương **82,8%** doanh thu đủ điều kiện. Trường `Country` ghi quốc gia của khách hàng.

## UC-05 Xem cơ cấu khách hàng theo RFM

Mở **Customer segments** rồi chọn năm và thị trường trên trang này. Đọc **Active customers by RFM group** để biết mỗi nhóm có bao nhiêu khách mua trong kỳ. Xem thêm **Sales revenue by RFM group** để biết doanh thu của từng nhóm. Nhãn High, Medium và Low được chốt ngày **10/12/2011**. Bộ lọc chỉ thay đổi số khách có giao dịch và doanh thu được tính vào mỗi nhóm.

**Kiểm tra.** Với **France** năm **2011**, ba nhóm High, Medium và Low lần lượt có **37**, **21** và **26** khách. Tổng là **84**, khớp thẻ khách hàng trên cùng trang.
