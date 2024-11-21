import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd


df=pd.read_csv(r'C:\Users\pooji\Downloads\athlete_events.csv\athlete_events.csv')

# Get the first 10 players from the data
first_10 = df.head(10)

# Create a map showing the players' countries
fig = px.scatter_geo(first_10,
                     locations="City",# This uses the country/team column
                     hover_name="Name",  # Show the player's name when hovering
                     title="Top 10 Olympic Champions on the World Map",
                     projection="natural earth",  # Set the map projection type
                     template="plotly",  # Theme for the map
                     color="Team", ) # Color by country



# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1("Top 10 Olympic Champions Dashboard"),
    html.Div([
        html.Label("First 10 Olympic Champions on the Map:"),
        dcc.Graph(id="country-map", figure=fig)
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

#html.Div: Represents an HTML <div> element.
#children: Holds the components or content that will be inside the <div>. This is how Dash structures the page content.