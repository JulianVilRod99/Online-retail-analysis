 Online Retail Data Analysis

1. Project Overview
This project performs data preparation and analysis using the Online Retail II dataset from the UCI Machine Learning Repository (https://archive.ics.uci.edu/dataset/502/online+retail+ii). The dataset contains transactional data from a UK-based online retailer between 2009 and 2011. The goal of this project is to clean, transform, and analyze the data to uncover insights about sales trends, customer behavior, and product performance.

2. Project Structure

Online-retail-analysis/
│
├── data/
│   └── raw/                <- Contains the original downloaded dataset
│   └── cleaned/            <- Contains the final dataset
├── notebooks/
│   ├── data_overview.ipynb   <- First exploration and basic data analysis
│   └── data_cleaning.ipynb   <- Cleaning and transformation steps
│
├── scripts/
│   └── download_data.py         <- Script to download and extract dataset
│
└── README.md

3. Dataset Information

Source: UCI Machine Learning Repository
Dataset: Online Retail II
Format: Excel .xlsx
Files:
online_retail_II.xlsx containing two sheets:
Year 2009-2010
Year 2010-2011

4. Data Preview & Early Exploration

Total rows after merging: 1,067,371
Columns: 8
Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer ID, Country
Duplicate rows: 34,335
Missing values in Customer ID: ~25%

The column Invoice includes transaction IDs and sometimes starts with a letter (e.g., "C") indicating canceled transactions.
These observations set the foundation for the data transformation and cleaning process in the next step.

5. Data cleaning and analysis

In this stage, duplicates were removed, missing values were imputed, and data types were adjusted.
Afterward, several visualizations were created to better understand the behavior of the data.

6. Conclusions

This analysis revealed key patterns and issues within the sales data:
* United Kingdom is by far the leading market in terms of total sales, showing a clear seasonal trend with a peak in the October–November period. This insight is valuable for planning targeted marketing campaigns around that time.

* A closer look at the top customers in the UK revealed irregular purchasing behavior and a high volume of product returns. In some cases, returns exceeded monthly sales, resulting in negative totals. This indicates a potential issue that should be investigated by the sales or customer experience team.

* Returns may be linked to product dissatisfaction, errors in orders, or unclear descriptions. Identifying the cause of these returns could help reduce them and improve customer retention and revenue stability.

Overall, this analysis provides useful insights to support data-driven decision-making in sales and marketing strategy.

The country with the highest sales is United Kingdom, followed by Ireland and Netherlands.
Sales show a clear trend during the October–November period, with the annual peak occurring in those months.
Focusing on the United Kingdom, we can observe similar purchase behaviors across several customers.
Some of them made a significant number of product returns, which even led to negative sales in certain months.
This is an important issue that should be analyzed by the sales or marketing department to understand the reasons behind the returns and find ways to reduce or prevent them in the future.