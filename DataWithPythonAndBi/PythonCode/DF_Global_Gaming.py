import pandas as pd

# ---------------------------
# CARREGAMENTO DO DATASET
# ---------------------------
df = pd.read_csv("./GlobalGaming.csv")

# ---------------------------
# TOP GENRE POR ANO (COUNT)
# ---------------------------
df_top_genre = (
    df.groupby("Year")["Top_Genre"]
      .value_counts()
      .reset_index(name="Count")
)

# ---------------------------
# TOP PLATFORM POR ANO (COUNT)
# ---------------------------
df_top_platform = (
    df.groupby("Year")["Top_Platform"]
      .value_counts()
      .reset_index(name="Count")
)

# ---------------------------
# RECEITA POR PAÍS (ANO A ANO)
# ---------------------------
df_revenue = (
    df.groupby(["Year", "Country"], as_index=False)["Gaming_Revenue_BillionUSD"]
      .sum()
)

# ---------------------------
# RECEITA DO PRIMEIRO ANO (2010)
# ---------------------------
df_first_year = (
    df[df["Year"] == 2010]
      .groupby("Country", as_index=False)["Gaming_Revenue_BillionUSD"]
      .sum()
      .sort_values("Country")
      .reset_index(drop=True)
)

# ---------------------------
# RECEITA DO ÚLTIMO ANO (2025)
# ---------------------------
df_last_year = (
    df[df["Year"] == 2025]
      .groupby("Country", as_index=False)["Gaming_Revenue_BillionUSD"]
      .sum()
      .sort_values("Country")
      .reset_index(drop=True)
)

# ---------------------------
# CRESCIMENTO TOTAL (2010 → 2025)
# ---------------------------
df_total_growth = (
    ((df_last_year["Gaming_Revenue_BillionUSD"] - df_first_year["Gaming_Revenue_BillionUSD"])
     / df_first_year["Gaming_Revenue_BillionUSD"] * 100)
     .round(2)
     .to_frame(name="EarningPercentage")
)

df_total_growth["Country"] = df_first_year["Country"]

# ---------------------------
# RECEITA DO ANO 2024
# ---------------------------
df_2024 = (
    df[df["Year"] == 2024]
      .groupby("Country", as_index=False)["Gaming_Revenue_BillionUSD"]
      .sum()
      .sort_values("Country")
      .reset_index(drop=True)
)

# ---------------------------
# CRESCIMENTO EM DOIS ANOS (2024 → 2025)
# ---------------------------
df_two_years_growth = (
    ((df_last_year["Gaming_Revenue_BillionUSD"] - df_2024["Gaming_Revenue_BillionUSD"])
     / df_2024["Gaming_Revenue_BillionUSD"] * 100)
     .round(2)
     .to_frame(name="Two_Years_Growth")
)

df_two_years_growth["Country"] = df_last_year["Country"]

# ---------------------------
# EXPORTAR ARQUIVOS PARA USAR NO POWER BI
# ---------------------------
df_top_genre.to_csv("TopGenre.csv", index=False)
df_top_platform.to_csv("TopPlatform.csv", index=False)
df_first_year.to_csv("FirstYear.csv", index=False)
df_last_year.to_csv("LastYear.csv", index=False)
df_total_growth.to_csv("TotalGrowthPercentage.csv", index=False)
df_two_years_growth.to_csv("TwoYears.csv", index=False)

# ---------------------------
# DATAFRAME FATO CONSOLIDADO
# ---------------------------
df_fact = df[[
    "Year",
    "Country",
    "Gaming_Revenue_BillionUSD",
    "Top_Platform",
    "Top_Genre"
]].sort_values(["Country", "Year"]).reset_index(drop=True)

df_fact.to_csv("FatoGaming.csv", index=False)