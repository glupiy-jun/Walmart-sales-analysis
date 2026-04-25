import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'Walmart_Sales.csv')

store_sales = df.groupby('Store')['Weekly_Sales'].sum()

top_stores = store_sales.sort_values(ascending=False).head(3)
bottom_stores = store_sales.sort_values(ascending=True).head(3)

top_store_ids = top_stores.index.tolist()
bottom_store_ids = bottom_stores.index.tolist()


def prepare_monthly_data(dataframe, store_ids):
    filtered_df = dataframe[dataframe['Store'].isin(store_ids)]

    monthly_data = (
        filtered_df.groupby(['Year_Month', 'Store'])
        .agg(total_sales=('Weekly_Sales', 'sum'))
        .reset_index()
    )

    pivot_data = monthly_data.pivot_table(
        index='Year_Month',
        columns='Store',
        values='total_sales'
    )

    return pivot_data


data_top = prepare_monthly_data(df, top_store_ids)
data_bottom = prepare_monthly_data(df, bottom_store_ids)


plt.figure(figsize=(14, 8))

for store_id in top_store_ids:
    plt.plot(
        data_top.index.astype(str),
        data_top[store_id],
        label=f'Top Store {store_id}: ${top_stores[store_id]:,.0f}',
        linewidth=3,
        marker='o'
    )

for store_id in bottom_store_ids:
    plt.plot(
        data_bottom.index.astype(str),
        data_bottom[store_id],
        label=f'Bottom Store {store_id}: ${bottom_stores[store_id]:,.0f}',
        linewidth=2,
        linestyle='--',
        marker='o'
    )

plt.title('Monthly Sales Trend', fontsize=16)
plt.xlabel('Year-Month')
plt.ylabel('Total Monthly Sales ($)')
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
