import pandas as pd

df = pd.read_csv(r'Walmart_Sales')

print('DataFrame Overview:\n')
df.info()
print(f'count of nan: {df.isna().sum().sum()}')
df = df.fillna(0)
