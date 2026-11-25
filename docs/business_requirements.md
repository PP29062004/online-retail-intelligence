# Business questions and rules

This academic case study uses the public transactions of a UK-based online retailer. It explores when and where sales are concentrated, which stock codes drive sales, and how purchase behaviour differs across customers.

| Question | Report feature |
| --- | --- |
| What is the scale of sales in the selected period and market? | Four KPI cards recalculate from eligible transaction lines. |
| How do sales change month to month? | A chronological trend highlights December 2011 as a partial month. |
| Which markets contribute the most revenue? | A ranked chart uses customer country of residence. |
| Which stock codes drive revenue? | A ranked chart retains the stock code even when descriptions change. |
| How are customers distributed across RFM groups? | Customer segments compares active customer counts and revenue by fixed RFM classification. |
| How much data is retained at each cleaning step? | The pipeline produces sequential row counts and validates dimension keys. |

## Sales eligibility

- Count a source row as a transaction line. Count an order as a distinct invoice number.
- Remove cancellations identified by an invoice prefix of `C`, missing required identifiers, dates or descriptions, and lines with non-positive or non-finite quantity or price.
- Remove exact duplicate rows after normalization. Identical repeated entries could represent legitimate lines. The audit reports how many this rule removes.
- Compute sales revenue as quantity × unit price in GBP. The scope covers qualifying positive sales to identified customers. Returns, margin and unidentified-customer sales are outside the report scope.

## RFM classification

- Set the snapshot to one day after the last qualifying transaction.
- Measure recency in days since last purchase, frequency in distinct invoices, and monetary value in total qualifying sales.
- Use average ranks for ties and scale percentile ranks to scores from 1 to 5. More recent, more frequent and higher monetary customers get higher scores.
- Classify summed scores 12–15 as High Value, 8–11 as Medium Value and 3–7 as Low Value.
- Keep the snapshot classification fixed. Report filters change the population of active customers and the sales attributed to each group.
