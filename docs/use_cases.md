# Use case báo cáo bán lẻ

Các tình huống dùng bản Power BI tiếng Việt ba trang đã nạp dữ liệu. Xóa các bộ lọc của tình huống trước khi bắt đầu tình huống mới.

## UC-01 · Kiểm tra doanh thu của một thị trường

**Người dùng** Quản lý bán hàng · **Yêu cầu** FR-01

Trên **Tổng quan bán hàng**, chọn **Năm 2011** và **Thị trường Pháp**, giữ tất cả tháng. Đọc bốn thẻ KPI. Kết quả lần lượt là **£199.336,00**, **368 đơn**, **84 khách** và **£541,67/đơn**. Cách kiểm tra số đơn là đếm mã hóa đơn khác nhau trong kỳ đã lọc.

## UC-02 · So sánh một tháng chưa đủ dữ liệu

**Người dùng** Quản lý bán hàng · **Yêu cầu** FR-02

Trên **Tổng quan bán hàng**, chọn **Tháng 12/2011** và giữ mọi thị trường. Đọc hai cột so sánh cùng kỳ. Doanh thu ngày **1–9/12/2011** là **£517.208,44**, cùng chín ngày năm 2010 là **£310.656,37**. Rê chuột vào biểu đồ theo ngày để kiểm tra số đơn của ngày cần tìm hiểu.

## UC-03 · Đọc bản đồ trước khi xem cơ cấu mã hàng

**Người dùng** Quản lý bán hàng · **Yêu cầu** FR-05

Trên **Thị trường và mã hàng**, chọn Úc trên bản đồ. Bảng thị trường còn Úc và Top mã hàng được tính lại theo các giao dịch của thị trường này. Bỏ chọn vùng để xem lại toàn bộ. Khi một nhãn quốc gia không xuất hiện trên bản đồ, tra trong bảng cạnh bản đồ.

## UC-04 · Kiểm tra một mã đứng đầu có bán đều không

**Người dùng** Bộ phận vận hành · **Yêu cầu** FR-06

Trên **Thị trường và mã hàng**, giữ toàn kỳ và mọi thị trường. Đọc bảng Top 10. Mã `22423` có **3.317 đơn**, còn doanh thu mã `23843` đến từ **một đơn**. Với mã `23843`, mở dữ liệu nguồn và đối chiếu dòng hủy trước khi dùng doanh thu làm căn cứ cho kế hoạch hàng. [Kết quả đối chiếu](business_strategy.md)

## UC-05 · Chọn nhóm khách để xem lại

**Người dùng** Người phụ trách khách hàng · **Yêu cầu** FR-03 và FR-04

Trên **Khách hàng**, xem **tháng 11/2011** trên biểu đồ theo tháng. Kết quả là **191** khách mua lần đầu trong dữ liệu và **1.473** khách quay lại. Sau đó giữ năm 2011, xóa lọc tháng và chọn Pháp. Bảng RFM cho thấy **37** khách nhóm cao, **21** khách nhóm trung bình và **26** khách nhóm thấp. Tổng là **84** khách có mua trong phạm vi lọc. Mốc gán nhóm vẫn là ngày **10/12/2011**.
