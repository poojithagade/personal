import requests

url = 'https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/global_super_store_orders.tsv'
response = requests.get(url)

# Print the first few lines of the response content to inspect
print(response.text.splitlines()[:10])

import pandas as pd

# Use 'on_bad_lines' to skip lines with too many columns
df = pd.read_csv(r'https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/global_super_store_orders.tsv', delimiter='\t', on_bad_lines='skip')

# Now, inspect the data
#print(df.head())

#Ship = print(df['Ship Date'])
#print(df['Ship Date'].min())
#print(df['Ship Date'].max())
import pandas as pd

# Load the data and convert 'Ship Date' to datetime
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/global_super_store_orders.tsv', delimiter='\t')

df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%y', errors='coerce')

# Extract Year and Quarter
df['Year'] = df['Ship Date'].dt.year
df['Quarter'] = df['Ship Date'].dt.to_period('Q').astype(str)

# Group by Year and Quarter and sum Sales
quarterly_sales = df.groupby(['Year', 'Quarter']).agg({'Sales': 'sum'}).reset_index()

# Print the grouped data
print(quarterly_sales)


