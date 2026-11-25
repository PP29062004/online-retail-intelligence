# Online Retail Intelligence

## Tiếng Việt

**Tóm tắt dùng cho thẻ dự án.** Tái dựng đồ án phân tích bán lẻ thời đại học bằng Python và Power BI. Xử lý 1,07 triệu dòng giao dịch, xây mô hình sao và trực quan hóa doanh thu, thị trường khách hàng và phân khúc RFM.

**Bối cảnh.** Đồ án nhóm tại HUTECH dùng Google Colab và Power BI để phân tích giao dịch của một nhà bán lẻ trực tuyến tại Anh. Khi làm lại dự án, tôi tập trung vào khả năng tái lập số liệu và định nghĩa rõ phạm vi của từng KPI.

**Cách thực hiện.** Tôi dùng Python để gộp hai sheet dữ liệu UCI, ghi lại số dòng bị loại ở từng bước và xuất một bảng giao dịch cùng bốn bảng chiều. Tôi xây báo cáo Power BI hai trang với bộ lọc theo năm và thị trường, DAX cho bốn KPI và bảng xếp hạng, cùng phân khúc RFM tại ngày 10/12/2011.

**Kết quả.** Sau làm sạch, 779.425 dòng đủ điều kiện ghi nhận £17,37 triệu doanh thu, 36.969 đơn và 5.878 khách hàng. Vương quốc Anh chiếm 82,8% doanh thu. Nhóm High Value chiếm 28,6% khách hàng và 80,2% doanh thu. Do chi tiêu là một thành phần của RFM, tỷ trọng này mô tả cơ cấu phân khúc trong dữ liệu.

**Công cụ.** Python · pandas · Power BI · Power Query · DAX · Mô hình sao

![Trang tổng quan doanh thu trong Power BI](../assets/sales-overview.png)

## English

**Portfolio card.** Rebuilt a university retail analytics project with Python and Power BI. Processed 1.07M transaction lines, designed a star schema, and reported sales trends, customer markets and RFM segments.

**Context.** The original HUTECH team project used Google Colab and Power BI to explore a UK online retailer's transactions. For the rebuild, I focused on making the figures reproducible and defining what each KPI covers.

**Approach.** I combined both UCI worksheets in Python, logged row exclusions and exported a transaction fact with four dimensions. I built a two-page Power BI report with year and market filters, DAX measures for KPIs and rankings, and a fixed customer RFM snapshot dated 10 December 2011.

**Results.** The 779,425 qualifying lines represent £17.37M in sales, 36,969 orders and 5,878 customers. The UK accounted for 82.8% of revenue. The High Value segment accounted for 28.6% of customers and 80.2% of revenue, a descriptive result given that spend plays a role in segment scoring.

**Tools.** Python · pandas · Power BI · Power Query · DAX · Star schema
