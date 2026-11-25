"""Reconstructed V2 batch pipeline. Outputs local BI-ready CSVs and audit JSON."""
import argparse
import json
from pathlib import Path
import numpy as np
import pandas as pd

SOURCE_COLS = ['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country']
RENAMES = {'Invoice':'InvoiceNo','Price':'UnitPrice','Customer ID':'CustomerID'}

def read_workbook(path):
    sheets = pd.read_excel(path, sheet_name=None, dtype={'Invoice':str,'StockCode':str,'Customer ID':str})
    frames, counts = [], {}
    for name, frame in sheets.items():
        frame = frame.rename(columns=RENAMES)
        missing = set(SOURCE_COLS) - set(frame.columns)
        if missing:
            raise ValueError(f'{name}: missing columns {sorted(missing)}')
        frames.append(frame[SOURCE_COLS].copy())
        counts[name] = len(frame)
    return pd.concat(frames, ignore_index=True), counts

def clean(raw):
    df = raw[SOURCE_COLS].copy()
    audit = {'raw_rows': len(df), 'steps': []}
    for c in ['InvoiceNo','StockCode','Description','CustomerID','Country']:
        df[c] = df[c].astype('string').str.strip().replace('', pd.NA)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
    for c in ['Quantity','UnitPrice']:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    audit['raw_missing_customer_rows'] = int(df.CustomerID.isna().sum())
    audit['raw_cancellation_rows'] = int(df.InvoiceNo.str.upper().str.startswith('C', na=False).sum())
    def keep(label, mask):
        nonlocal df
        before = len(df)
        df = df.loc[mask].copy()
        audit['steps'].append({'rule':label, 'removed':before-len(df), 'remaining':len(df)})
    keep('exclude cancellation invoices', ~df.InvoiceNo.str.upper().str.startswith('C', na=False))
    keep('require identifiers, date and description', df[['InvoiceNo','StockCode','Description','CustomerID','Country','InvoiceDate']].notna().all(axis=1))
    keep('positive finite quantity and unit price', np.isfinite(df.Quantity) & np.isfinite(df.UnitPrice) & (df.Quantity > 0) & (df.UnitPrice > 0))
    keep('remove exact duplicate normalized rows (assumption)', ~df.duplicated(subset=SOURCE_COLS))
    if df.empty:
        raise ValueError('No qualifying sales rows')
    df['Revenue'] = df.Quantity * df.UnitPrice
    df['Date'] = df.InvoiceDate.dt.normalize()
    df['YearMonth'] = df.Date.dt.strftime('%Y-%m')
    audit['clean_rows'] = len(df)
    audit['scope'] = 'Positive, non-cancelled, identified-customer transaction lines; not net revenue or all store sales.'
    assert not df[SOURCE_COLS].isna().any().any()
    assert not df.duplicated(subset=SOURCE_COLS).any()
    return df, audit

def segment(df):
    snapshot = df.Date.max() + pd.Timedelta(days=1)
    rfm = df.groupby('CustomerID', as_index=False).agg(LastPurchase=('Date','max'), Frequency=('InvoiceNo','nunique'), Monetary=('Revenue','sum'))
    rfm['Recency'] = (snapshot-rfm.LastPurchase).dt.days
    # V2 rule, not recovered original scoring. Equal values share scores.
    for c, ascending, out in [('Recency',False,'RScore'),('Frequency',True,'FScore'),('Monetary',True,'MScore')]:
        rfm[out] = np.ceil(rfm[c].rank(method='average', pct=True, ascending=ascending)*5).clip(1,5).astype(int)
    rfm['RFMScore'] = rfm[['RScore','FScore','MScore']].sum(axis=1)
    rfm['Segment'] = np.select([rfm.RFMScore>=12,rfm.RFMScore>=8], ['High Value','Medium Value'], default='Low Value')
    rfm['SnapshotDate'] = snapshot
    return rfm

def build_model(df, rfm):
    date = pd.DataFrame({'Date':pd.date_range(df.Date.min(),df.Date.max())})
    date['Year'] = date.Date.dt.year
    date['MonthNo'] = date.Date.dt.month
    date['YearMonth'] = date.Date.dt.strftime('%Y-%m')
    date['Quarter'] = date.Date.dt.quarter
    # Most recent observed product description; stable tie-breaker.
    product = df.sort_values(['InvoiceDate','Description']).drop_duplicates('StockCode',keep='last')[['StockCode','Description']]
    country = df[['Country']].drop_duplicates()
    fact = df[['InvoiceNo','StockCode','CustomerID','Country','Date','InvoiceDate','Quantity','UnitPrice','Revenue']].copy()
    model = {'FactSales':fact,'DimDate':date,'DimProduct':product,'DimCountry':country,'DimCustomer':rfm}
    for name,key in [('DimDate','Date'),('DimProduct','StockCode'),('DimCountry','Country'),('DimCustomer','CustomerID')]:
        assert model[name][key].is_unique
        assert fact[key].isin(model[name][key]).all()
    return model

def run(path, out):
    raw, sheets = read_workbook(path)
    df, audit = clean(raw)
    rfm = segment(df)
    model = build_model(df,rfm)
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    for name, frame in model.items():
        frame.to_csv(out / f'{name}.csv',index=False,date_format='%Y-%m-%d %H:%M:%S')
    revenue = float(df.Revenue.sum()); orders = int(df.InvoiceNo.nunique())
    audit.update({'sheet_rows':sheets, 'date_min':str(df.Date.min().date()), 'date_max':str(df.Date.max().date()),'total_revenue_gbp':revenue,'orders':orders,'customers':int(df.CustomerID.nunique()),'average_order_value_gbp':revenue/orders,'segments':rfm.Segment.value_counts().to_dict(),'snapshot_date':str(rfm.SnapshotDate.iloc[0].date()),'invoice_multiple_customers':int((df.groupby('InvoiceNo').CustomerID.nunique()>1).sum()),'invoice_multiple_countries':int((df.groupby('InvoiceNo').Country.nunique()>1).sum())})
    (out/'audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
    return audit

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',default='data/raw/online_retail_II.xlsx')
    parser.add_argument('--output',default='data/processed')
    args=parser.parse_args()
    print(json.dumps(run(args.input,args.output),indent=2))
