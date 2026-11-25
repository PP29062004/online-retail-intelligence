# Open the Power BI report

[Online Retail Intelligence.pbip](Online%20Retail%20Intelligence.pbip) opens the report and its import-mode semantic model. The project uses PBIR for report definitions and TMDL for the semantic model.

1. Run the Python pipeline as described in the [README](../README.md). It creates five CSVs under `data/processed`.
2. Open the PBIP in a current version of Power BI Desktop. On builds that list **Power BI Project** and **PBIR** under preview features, enable them.
3. In **Home > Transform data > Edit parameters**, set `pDataFolder` to the absolute path of `data/processed`. For example, `C:\Projects\online-retail-intelligence\data\processed`. The project starts with the example value `C:\OnlineRetail\data\processed`.
4. Apply the parameter change and select **Refresh**. The initial open may display notices to refresh relationships and load tables. Confirm the four overview cards show £17,374,804.27, 36,969, 5,878 and £469.98 with the filters cleared.
5. Set **Sales year** to 2011 and **Customer market** to France. Confirm £199,336.00, 368, 84 and £541.67. Clear the filters and open **Customer segments** to inspect the snapshot groups.
6. To create a self-contained file with imported data, use **File > Save as** and select **Power BI Desktop files (.pbix)**.

The PBIP includes the report layout, relationships, import queries and DAX measures. Keep the generated CSVs and `.pbi` working state local. When preparing changes for Git, restore `pDataFolder` to the example path in [expressions.tmdl](Online%20Retail%20Intelligence.SemanticModel/definition/expressions.tmdl). Linked [Microsoft project documentation](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview) covers the Desktop save formats.
