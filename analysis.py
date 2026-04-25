import pandas as pd

df = pd.read_csv(r'Walmart_Sales.csv')

store_sales = df.groupby('Store')['Weekly_Sales'].sum()

top_stores = store_sales.sort_values(ascending=False).head(3)
bottom_stores = store_sales.sort_values(ascending=True).head(3)

print('\nTop 3 Stores by Total Sales:')
print(top_stores)

print('\nBottom 3 Stores by Total Sales:')
print(bottom_stores)

def create_pivot_table(data_frame):
    pivot_table = (
        data_frame.groupby(['Store'])
        .agg(
            total_sales=('Weekly_Sales', 'sum'),
            days=('Holiday_Flag', 'count')
        )
        .reset_index()
    )

    pivot_table['total_sales'] = pivot_table['total_sales'].round(1)

    avg = pivot_table['total_sales'].mean()

    pivot_table['deviation_%'] = (
        (pivot_table['total_sales'] - avg) / avg * 100
    ).round(2)

    return pivot_table

print('holidays')
holidays_df = df[df['Holiday_Flag'] == 1]

data_holidays = create_pivot_table(holidays_df)
data_holidays['avg_sales_per_store'] = (
    data_holidays['total_sales'] / data_holidays['days']
).round(2)

data_holidays = data_holidays.sort_values('total_sales', ascending=False)

print(data_holidays.head(3))

print('week_days')
week_days_df = df[df['Holiday_Flag'] == 0]

data_week_day = create_pivot_table(week_days_df)
data_week_day['avg_sales_per_store'] = (
    data_week_day['total_sales'] / data_week_day['days']
).round(2)

data_week_day = data_week_day.sort_values('total_sales', ascending=False)

print(data_week_day.head(3))
