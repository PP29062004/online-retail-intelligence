"""Reproduce the business strategy checks for the Online Retail II case study."""

import argparse
from pathlib import Path

import pandas as pd

from src.pipeline import segment


def seasonal_sales(sales):
    comparable = sales.loc[sales.Date.dt.year.isin([2010, 2011]) & sales.Date.dt.month.le(11)]
    peak = comparable.loc[comparable.Date.dt.month.isin([10, 11])].copy()
    peak["Year"] = peak.Date.dt.year
    peak["Market"] = peak.Country.where(peak.Country.eq("United Kingdom"), "Outside United Kingdom")

    yearly = comparable.groupby(comparable.Date.dt.year).Revenue.sum()
    summary = peak.groupby("Year").agg(Revenue=("Revenue", "sum"), Orders=("InvoiceNo", "nunique"))
    summary["Share of Jan–Nov (%)"] = 100 * summary.Revenue / yearly
    print("\nOctober–November compared with January–November")
    print(summary.round(2).to_string())
    print("\nOctober–November by market")
    print(peak.pivot_table(index="Market", columns="Year", values="Revenue", aggfunc="sum").round(2).to_string())


def stock_code_concentration(sales):
    leading = (
        sales.groupby("StockCode")
        .agg(Revenue=("Revenue", "sum"), Orders=("InvoiceNo", "nunique"), Customers=("CustomerID", "nunique"))
        .sort_values(["Revenue", "StockCode"], ascending=[False, True])
        .head(10)
    )
    leading_rows = sales.loc[sales.StockCode.isin(leading.index)]
    largest_invoice = leading_rows.groupby(["StockCode", "InvoiceNo"]).Revenue.sum().groupby("StockCode").max()
    leading["Largest invoice (%)"] = 100 * largest_invoice / leading.Revenue
    print("\nTop stock codes and their exposure to a single invoice")
    print(leading.round(2).to_string())

    prior = sales.loc[sales.Date.between("2010-12-01", "2010-12-09"), "Revenue"].sum()
    current = sales.loc[sales.Date.between("2011-12-01", "2011-12-09")]
    total = current.Revenue.sum()
    without_code = current.loc[~current.StockCode.eq("23843"), "Revenue"].sum()
    print(f"\nDecember 1–9 year-over-year sales: {(total / prior - 1):+.2%}")
    print(f"December 1–9 comparison excluding 2011 stock code 23843: {(without_code / prior - 1):+.2%}")


def repeat_purchase(sales):
    for year in (2010, 2011):
        start = pd.Timestamp(year, 1, 1)
        cutoff = pd.Timestamp(year, 9, 1)
        stop = pd.Timestamp(year, 12, 1)
        history = sales.loc[sales.Date.ge(start) & sales.Date.lt(cutoff)]
        followup = sales.loc[sales.Date.ge(cutoff) & sales.Date.lt(stop)]
        cohorts = segment(history)
        cohorts["Bought again"] = cohorts.CustomerID.isin(followup.CustomerID)
        summary = cohorts.groupby("Segment")["Bought again"].agg(Customers="size", Returned="sum")
        summary["Returned (%)"] = 100 * summary.Returned / summary.Customers
        print(f"\n{year} RFM using January–August purchases and September–November follow-up")
        print(summary.round(2).to_string())
        medium_repeat = cohorts.loc[cohorts.Segment.eq("Medium Value") & cohorts.Frequency.ge(2), "Bought again"]
        print(f"Medium Value with at least 2 earlier orders: {medium_repeat.sum()}/{len(medium_repeat)} returned")


def cancellation_candidates(workbook):
    raw = pd.read_excel(
        workbook,
        sheet_name="Year 2010-2011",
        usecols=["Invoice", "StockCode", "Quantity", "InvoiceDate", "Price", "Customer ID"],
        dtype={"Invoice": str, "StockCode": str, "Customer ID": str},
    )
    focus = raw.loc[raw.StockCode.eq("23843") & raw["Customer ID"].notna()].copy()
    focus["Day"] = focus.InvoiceDate.dt.normalize()
    focus["Units"] = focus.Quantity.abs()
    is_cancellation = focus.Invoice.str.upper().str.startswith("C", na=False)
    positive = focus.loc[~is_cancellation & focus.Quantity.gt(0)]
    reversals = focus.loc[is_cancellation & focus.Quantity.lt(0)]
    pairs = positive.merge(
        reversals,
        on=["StockCode", "Customer ID", "Day", "Units", "Price"],
        suffixes=("_sale", "_cancel"),
    )
    pairs["Positive line value"] = pairs.Units * pairs.Price
    print("\nPotential pairs for stock code 23843 from the raw workbook")
    columns = ["Invoice_sale", "Invoice_cancel", "InvoiceDate_sale", "InvoiceDate_cancel",
               "Units", "Price", "Positive line value"]
    print(pairs[columns].round({"Price": 2, "Positive line value": 2}).to_string(index=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fact", type=Path, default=Path("data/processed/FactSales.csv"))
    parser.add_argument("--raw-workbook", type=Path, help="Also check the suspected cancellation in UCI Excel.")
    args = parser.parse_args()
    sales = pd.read_csv(
        args.fact,
        usecols=["Date", "Country", "StockCode", "InvoiceNo", "CustomerID", "Revenue"],
        dtype={"Country": str, "StockCode": str, "InvoiceNo": str, "CustomerID": str},
        parse_dates=["Date"],
    )
    seasonal_sales(sales)
    stock_code_concentration(sales)
    repeat_purchase(sales)
    if args.raw_workbook:
        cancellation_candidates(args.raw_workbook)
