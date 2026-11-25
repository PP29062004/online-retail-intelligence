# Dùng dashboard để ra quyết định bán lẻ

**Sinh viên thực hiện** Phạm Thanh Phúc

Khi làm đồ án, tôi dùng dashboard để trả lời câu hỏi tháng nào bán tốt, mã hàng nào đứng đầu và khách hàng mua như thế nào. Khi đọc lại dữ liệu, tôi muốn đi thêm một bước. Nếu nhìn thấy doanh thu tăng, tôi sẽ chuẩn bị thêm hàng, rà lại một đơn lớn hay thử một cách chăm sóc khách hàng khác? Ba tình huống dưới đây dùng số liệu từ bản Power BI dựng lại. Doanh thu ở đây là giá trị giao dịch dương đủ điều kiện của khách có mã định danh.

## Chuẩn bị trước tháng 10

Tôi mở **Sales overview** để đọc doanh thu theo tháng và so lại các kỳ có đủ dữ liệu. Tháng 10 và 11 đóng góp hơn 28% doanh thu từ tháng 1 đến tháng 11 ở cả hai năm.

| Năm | Doanh thu tháng 10–11 | Số đơn tháng 10–11 | Tỷ trọng trong tháng 1–11 |
| --- | ---: | ---: | ---: |
| 2010 | £2.199.572,03 | 4.720 | 28,18% |
| 2011 | £2.191.848,06 | 4.586 | 28,10% |

Tổng doanh thu hai tháng gần như đi ngang. Riêng tại Anh, doanh thu giảm 3,1%, trong khi các thị trường ngoài Anh cộng lại tăng 14,3%. Nếu dùng báo cáo để lập kế hoạch, tôi sẽ rà soát nhóm hàng bán nhiều và công suất đóng gói từ tháng 9, rồi xem nhu cầu theo từng thị trường. Để chốt lượng nhập, bộ phận vận hành còn cần số tồn hiện tại, thời gian nhập hàng và giá vốn. Ngày 9/12/2011 là ngày cuối có dữ liệu, nên tháng 12 cần so theo cùng số ngày.

## Xem một mã hàng bán đều hay chỉ có một đơn lớn

Hai mã có doanh thu cao có thể cần hai cách xử lý. Tôi đối chiếu bảng Top mã hàng với số đơn, số khách và tỷ trọng doanh thu đến từ hóa đơn lớn nhất của mỗi mã.

| Mã hàng | Doanh thu | Số đơn có mã hàng | Số khách | Tỷ trọng của hóa đơn lớn nhất |
| --- | ---: | ---: | ---: | ---: |
| `22423` · Regency Cakestand 3 Tier | £277.656,25 | 3.317 | 1.314 | 1,42% |
| `23843` · Paper Craft, Little Birdie | £168.469,60 | 1 | 1 | 100% |

Trong Excel gốc, sau dòng bán 80.995 sản phẩm mã `23843` có một dòng hủy sau 12 phút, cùng ngày, cùng mã khách và đơn giá, số lượng đối dấu. Nguồn có ký hiệu hóa đơn hủy, còn phép đối chiếu này dựa trên các trường khớp nhau. Nếu tạm bỏ riêng dòng bán đó để kiểm tra độ nhạy, mức tăng doanh thu ngày 1–9/12/2011 so với cùng kỳ giảm từ **66,5% xuống 12,3%**. Muốn xác định doanh thu sau hủy cần đối soát đầy đủ. [Mô tả dữ liệu Online Retail II của UCI](https://archive.ics.uci.edu/dataset/502/online+retail+ii)

Tôi sẽ đưa `22423` vào danh sách theo dõi để chuẩn bị hàng vì có nhiều khách cùng mua. Với `23843`, việc đầu tiên là kiểm tra trạng thái đơn trước khi quyết định nhập thêm. Khi xem Top mã hàng, tôi cũng đọc riêng các dòng như `POST` (bưu phí) và `M` (Manual).

## Chọn khách để thử chăm sóc lại

Tôi chấm RFM riêng cho từng năm bằng lịch sử mua từ tháng 1 đến tháng 8, rồi xem mỗi khách đã chấm điểm có phát sinh ít nhất một đơn đủ điều kiện từ tháng 9 đến hết tháng 11 hay không. Mẫu số là số khách có giao dịch trong giai đoạn chấm điểm. Cách này giữ phần giao dịch dùng để kiểm tra ở sau thời điểm chấm điểm. [Fader, Hardie và Lee về kiểm tra trên dữ liệu giữ lại](https://doi.org/10.1509/jmkr.2005.42.4.415)

| Nhóm RFM lúc chấm điểm | Mua lại tháng 9–11/2010 | Mua lại tháng 9–11/2011 |
| --- | ---: | ---: |
| High Value | 754/908 · 83,0% | 763/896 · 85,2% |
| Medium Value | 642/1.055 · 60,9% | 612/1.048 · 58,4% |
| Low Value | 479/1.177 · 40,7% | 425/1.178 · 36,1% |

Nhóm High Value có tỷ lệ mua lại cao nhất trong hai kỳ quan sát. Tôi sẽ ưu tiên giữ chất lượng phục vụ cho nhóm này. Nếu muốn thử nhắc mua lại, tôi sẽ bắt đầu với nhóm Medium Value từng mua từ hai đơn trở lên trong giai đoạn chấm điểm. Năm 2011, 474 trong 765 khách thuộc nhóm này mua lại trong ba tháng tiếp theo. Khi có dữ liệu chiến dịch, có thể chia ngẫu nhiên một phần khách vào nhóm nhận lời nhắc và phần còn lại vào nhóm đối chứng, rồi so tỷ lệ mua lại và chi phí trên mỗi đơn tăng thêm. Các tỷ lệ trong bảng là kết quả quan sát từ giao dịch lịch sử.

## Chạy lại các phép kiểm tra

Sau khi tạo CSV bằng pipeline, chạy hai lệnh dưới đây từ thư mục gốc. Lệnh thứ hai đọc thêm Excel để đối chiếu dòng hủy của mã `23843`.

```sh
python -m src.strategy
python -m src.strategy --raw-workbook data/raw/online_retail_II.xlsx
```

Bản Power BI trong repo có bộ lọc năm và thị trường, biểu đồ doanh thu tháng, bảng Top mã hàng và các nhóm RFM tại ngày 10/12/2011. Số đơn, số khách theo mã hàng và tỷ lệ mua lại theo hai kỳ chấm điểm được tính riêng trong phần nghiên cứu này. [Xem mã tính toán](../src/strategy.py)
