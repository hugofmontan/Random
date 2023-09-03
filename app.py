import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Container
import plotly.graph_objects as go
import pandas as pd
from Data_Extraction.returnbyasset import create_portfolio_returns_plot
from Data_Extraction.graficocascata import create_waterfall_chart
from Data_Extraction.dadosgerais import calculate_cumulative_returns
from Data_Extraction.dadosgerais import assets_prices
from Data_Extraction.assetsperformances import create_assets_returns
from Data_Extraction.barchart import create_barchart

# Read CSV files and define tickers
calculate_cumulative_returns()
dx = assets_prices()
dx = pd.read_csv('prices.csv')
df = pd.read_csv('dadosgerais.csv')
waterfall_chart = create_waterfall_chart(df)
tickers = ['BTC-USD', 'ETH-USD', 'LDO-USD', 'MATIC-USD', 'ARB11841-USD', 'LINK-USD', 'SOL-USD', 'OP-USD', 'STX4847-USD', 'DYDX-USD', 'PRIME23711-USD']

portfolio_returns_plot = create_portfolio_returns_plot(df, tickers)
assets_returns_plot = create_assets_returns(dx)
barchart = create_barchart(dx)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the dashboard
app.layout = dbc.Container([
    html.Br(),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=portfolio_returns_plot), width=6),
        dbc.Col(dcc.Graph(figure=waterfall_chart), width=6),
    ], className='dash-row'),  # Add custom class for styling
    html.Br(),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=assets_returns_plot), width=6),
        dbc.Col(dcc.Graph(figure=barchart), width=6),
    ], className='dash-row'),  # Add custom class for styling
])

server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
    time.sleep(60)
