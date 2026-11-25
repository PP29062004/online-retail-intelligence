# Reconstruction notes

The original HUTECH project report described a Colab workflow, a Power BI Service dashboard, and three RFM groups. The available Colab export contains the initial cleaning and exploratory charts. V2 reconstructs the report and semantic model in Power BI Desktop from the public UCI workbook.

| Evidence | What it supports |
| --- | --- |
| Academic report | Original questions, dashboard topics and historical figures of about £8.83M, 19K orders and £460 AOV |
| Colab export | A single-sheet read by default, cancellation exclusion, removal of missing customer IDs and descriptions, and the quantity × price calculation |
| UCI workbook | Two worksheets and a reproducible full-period basis for the V2 metrics |
| Starter project | A proposed two-sheet pipeline, dimensional model, RFM percentile rules and a validation plan |

V2 adds explicit rule-by-rule cleaning counts, one star schema, a dated RFM snapshot and source-controlled Power BI files. The supplied Colab export ends without a complete RFM implementation. V2 uses the scoring documented in [business rules](business_requirements.md). Historical KPI definitions and filters remain partially documented, so the verified V2 results use the new dataset scope consistently.

UCI defines `Country` as the customer's country of residence. The rebuilt charts present customer markets. Individual stock codes can represent fees or adjustments, and the report calls this out beside the ranking.

The historical Word report and Colab export were reference material during reconstruction. Repository assets use V2 output and the public dataset attribution.
