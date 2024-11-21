import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Read the .tsv file using Pandas (with tab delimiter)
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/global_super_store_orders.tsv' , delimiter='\t',on_bad_lines='skip')
#######how do i clean the actual data?
#######wt if the data keeps getting updated?

# Create a bar chart for total sales by region
bar_sales_by_region = px.bar(df,
                             x='Region',
                             y='Sales',
                             title='Total Sales by Region',
                             labels={'Sales': 'Total Sales', 'Region': 'Region'},
                             color='Region')

#piechart
pie_sales_by_Categories=px.pie(df, names='Category', values='Sales', title='Sales by Category',
                               labels={'Sales': 'Total Sales', 'Category': 'Category'},
                               color='Category')

#Linechart  # need to covert to datetime format
# Convert 'Ship Date' to datetime
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%y', errors='coerce')

# Extract Year from 'Ship Date'
df['Year'] = df['Ship Date'].dt.year

# Group by Year and sum Sales
annual_sales = df.groupby(['Year']).agg({'Sales': 'sum'}).reset_index()
df['Sales'] = df['Sales'].str.replace(',', '').astype(int)
#df['annual sales']=df.groupby(['Year'])['Sales'].sum()
df['annual sales'] = df.groupby('Year')['Sales'].transform('sum')


# Sort the data by Year
annual_sales.sort_values(by=['Year'], inplace=True)

# Plot the line chart: Sales vs Year
line_sales_over_year = px.line(df,
                               x='Year',
                               y='annual sales',
                               title='Sales Over Time (Annual)',
                               labels={'Year': 'Year', 'annual sales': 'Total Sales'})


# Display the figure in Dash layout
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Graph(figure=bar_sales_by_region),
    dcc.Graph(figure=pie_sales_by_Categories),
    dcc.Graph(figure=line_sales_over_year)
])

if __name__ == '__main__':
    app.run_server(debug=True)
