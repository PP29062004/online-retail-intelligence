# KPI validation

## Definitions

| KPI | Definition |
| --- | --- |
| Sales revenue | Sum of quantity × unit price for qualifying lines, in GBP |
| Orders | Distinct invoice numbers in the filtered fact |
| Active customers | Distinct customer IDs in the filtered fact |
| Average order value | Sales revenue divided by orders, with a blank result when the denominator is zero |
| Segment sales share | Segment revenue divided by revenue across selected segments, retaining the other filters |

## Workbook and model checks

| Scope | Rows | Sales | Orders | Customers |
| --- | ---: | ---: | ---: | ---: |
| First sheet, supplied Colab rules | 407,695 | £8,832,003.27 | 19,215 | 4,314 |
| First sheet, V2 rules | 400,916 | £8,798,233.74 | 19,213 | 4,312 |
| Both sheets, V2 rules | 779,425 | £17,374,804.27 | 36,969 | 5,878 |

The two sheets contain 525,461 and 541,910 rows. They overlap in December 2010. The cleaned full-period count reflects global deduplication after combining the sheets. The first-sheet replay is consistent with the approximate £8.83M figure in the academic report.

| Sequential rule | Removed | Remaining |
| --- | ---: | ---: |
| Start with both worksheets | 0 | 1,067,371 |
| Exclude cancellation invoices | 19,494 | 1,047,877 |
| Require identifiers, date and description | 242,257 | 805,620 |
| Require positive, finite quantity and price | 71 | 805,549 |
| Remove exact normalized duplicates | 26,124 | 779,425 |

Dimension keys are unique, and every retained line has all four dimension matches. Zero invoice numbers map to multiple customer IDs or multiple countries. The qualifying date range is 1 December 2009 to 9 December 2011. Monthly totals and the RFM monetary totals both reconcile to the fact.

## Power BI checks

Ran the report in Power BI Desktop on the full workbook output. DAX queries against its imported model returned the following values, which match the Python fact calculations to the displayed precision.

| Filter | Revenue | Orders | Active customers | AOV |
| --- | ---: | ---: | ---: | ---: |
| All | £17,374,804.27 | 36,969 | 5,878 | £469.98 |
| 2011 and France | £199,336.00 | 368 | 84 | £541.67 |

| RFM group | Full-period customers | Full-period sales | Active in 2011 and France |
| --- | ---: | ---: | ---: |
| High Value | 1,683 | £13,936,282.28 | 37 |
| Medium Value | 1,860 | £2,538,621.45 | 21 |
| Low Value | 2,335 | £899,900.54 | 26 |

All 5,878 customers have one segment at the 10 December 2011 snapshot. The three groups sum to 84 active customers in the filtered slice. The full-period ranking measures return 10 stock codes, 6 markets and 8 customers.

Re-run the two synthetic tests with `python -m unittest discover -s tests -v`. Run [validate.dax](../powerbi/validate.dax) in Power BI's DAX query view after refresh. The pipeline writes its full sequential audit to `data/processed/audit.json`.
