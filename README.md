# DataAnalitics

Global Gaming Market Analysis (2010–2025)

This project analyzes the global gaming market from 2010 to 2025 using Python for data preparation and Power BI for visualization.
The final dashboard highlights revenue trends, country performance, and the popularity of gaming genres over time.

Dashboard Overview

(Insert your dashboard screenshot here)

![Dashboard](dashboard/dashboard_screenshot.png)

 Project Objective

Identify the countries with the highest gaming revenue.

Calculate total growth (2010 → 2025) and recent growth (2024 → 2025).

Track the most popular game genres across the years.

Build a clean, interactive dashboard for insights.

 Dataset

File: GlobalGaming.csv

Column	Description
Year	Measurement year
Country	Country name
Gaming_Revenue_BillionUSD	Revenue in billions of USD
Top_Genre	Most played genre in that year/country
Top_Platform	Most used platform in that year/country
 Data Processing (Python)

Data was cleaned and transformed using Python, generating the tables required for the Power BI dashboard.

 Generated Data Tables

TopGenre.csv — Genre popularity by year

TopPlatform.csv — Platform usage by year

FirstYear.csv — Revenue by country in 2010

LastYear.csv — Revenue by country in 2025

TotalGrowthPercentage.csv — Growth from 2010 to 2025

TwoYears.csv — Growth from 2024 to 2025

FatoGaming.csv — Fact table for the entire dataset

 Dashboard Visuals (Power BI)
 
Two-Year Growth (2024 → 2025) — Horizontal Bar Chart

Shows the revenue growth percentage for each country.

Top Countries by Gaming Revenue — Horizontal Bar Chart

Displays the countries with the highest total gaming revenue.

Most Popular Game Genre (2010–2025) — Line Chart

Highlights trends in genre popularity over time.

 Key Insights

🇧🇷 Brazil shows one of the highest overall growth rates.

🇺🇸 United States leads in total revenue but with moderate recent growth.

RPG, FPS, and Sports remain dominant genres.

 Emerging markets demonstrate strong acceleration in the last few years.

 Next Steps

Add platform trends to the Power BI dashboard.

Create a world map visualization.

Apply forecasting models for future revenue predictions.

🧑‍💻 Technologies Used

Python (Pandas)

Power BI

Git & GitHub

VSCode / Jupyter Notebook
