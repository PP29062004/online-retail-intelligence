import tempfile
import unittest
from pathlib import Path
import pandas as pd
from src.pipeline import run, clean, segment, SOURCE_COLS

class PipelineTest(unittest.TestCase):
    def test_full_workbook(self):
        cols=['Invoice','StockCode','Description','Quantity','InvoiceDate','Price','Customer ID','Country']
        rows=[['001','A','Item A',2,'2010-01-01',5,'100','UK'],['001','B','Item B',1,'2010-01-01',7,'100','UK'],['002','A','Item A',1,'2011-01-02',5,'200','France'],['C003','A','Item A',-1,'2011-01-03',5,'100','UK'],['004','A','Item A',1,'2011-01-03',5,None,'UK'],['005','A','Item A',0,'2011-01-03',5,'100','UK']]
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'sample.xlsx'; out=Path(tmp)/'out'
            with pd.ExcelWriter(p) as w:
                pd.DataFrame(rows[:2],columns=cols).to_excel(w,sheet_name='Year 2009-2010',index=False)
                pd.DataFrame(rows[2:]+[rows[0]],columns=cols).to_excel(w,sheet_name='Year 2010-2011',index=False)
            a=run(p,out)
            self.assertEqual(a['raw_rows'],7)
            self.assertEqual(a['clean_rows'],3)
            self.assertEqual(a['orders'],2)
            self.assertEqual(a['customers'],2)
            self.assertEqual(a['total_revenue_gbp'],22)
            self.assertEqual(a['average_order_value_gbp'],11)
            self.assertEqual(sum(a['segments'].values()),2)
            self.assertEqual(a['invoice_multiple_customers'],0)
            self.assertEqual(len(pd.read_csv(out/'DimCustomer.csv')),2)
    def test_rfm_direction(self):
        df=pd.DataFrame([['1','A','A',1,'2020-01-01',1,'old','UK'],['2','A','A',1,'2020-02-01',5,'new','UK']],columns=SOURCE_COLS)
        clean_df,_=clean(df); r=segment(clean_df).set_index('CustomerID')
        self.assertGreater(r.loc['new','RScore'],r.loc['old','RScore'])
        self.assertEqual(r.loc['new','Recency'],1)

if __name__=='__main__': unittest.main()
