import pandas as pd

df = pd.read_csv(r'Walmart_Sales.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df = df.sort_values('Date')

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.strftime('%B')
df['Year_Month'] = df['Date'].dt.to_period('M')
