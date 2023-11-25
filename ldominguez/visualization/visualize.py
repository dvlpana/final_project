import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def covid_time_series(df: pd.DataFrame):
    sns.lineplot(
        data=df,#some_latam_countries_df,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series");
    
def covid_time_series_por_pais(df,n):
    top_countries_df =(df
    .select_columns(["country_region", "value"])
    .groupby(["country_region"])
    .aggregate("sum")
    .sort_values("value", ascending=False)
    .reset_index()
    .head(20)
    .transform_column(
        column_name="country_region",
        function=lambda x: "red" if x in countries else "lightblue",
        dest_column_name="color"
    )
    )
    print('hola')
    return top_countries_df.head(n)
   