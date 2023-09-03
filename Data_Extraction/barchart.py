import pandas as pd
import plotly.graph_objects as go

def create_barchart(df):
    df = pd.read_csv('prices.csv')

    df.rename(columns={'ARB11841-USD': 'ARB'}, inplace=True)
    df.rename(columns={'BTC-USD': 'BTC'}, inplace=True)
    df.rename(columns={'DYDX-USD': 'DYDX'}, inplace=True)
    df.rename(columns={'ETH-USD': 'ETH'}, inplace=True)
    df.rename(columns={'LDO-USD': 'LDO'}, inplace=True)
    df.rename(columns={'LINK-USD': 'LINK'}, inplace=True)
    df.rename(columns={'MATIC-USD': 'MATIC'}, inplace=True)
    df.rename(columns={'OP-USD': 'OP'}, inplace=True)
    df.rename(columns={'PRIME23711-USD': 'PRIME'}, inplace=True)
    df.rename(columns={'SOL-USD': 'SOL'}, inplace=True)
    df.rename(columns={'STX4847-USD': 'STX'}, inplace=True)

    tickers = ['BTC', 'ETH', 'LDO', 'MATIC', 'ARB', 'LINK', 'SOL', 'OP', 'STX', 'DYDX', 'PRIME']

    df = df.drop('Datetime', axis=1)

    for i in tickers: 
        df[i] = df[i].pct_change().add(1).cumprod().sub(1) * 100

    df = df.iloc[-1]
    text_values = [f'{value:.2f}%' for value in df.round(2)]

    # Create a Plotly bar chart for the last performance
    fig = go.Figure(go.Bar(
        x=df.index,
        y=df,
        marker_color='#623AD7',
        text=text_values,
        textposition='outside'
    ))

    # Configure layout of the plot
    fig.update_layout(
        title='Rentabilidade Acumulada',
        title_x=0.5,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_family='Outfit',
        xaxis_title='',
        yaxis_title='',
        xaxis=dict(
            showline=True,
            linecolor='black',
            linewidth=2
        ),
        yaxis=dict(
            ticksuffix='%',
            showline=True,
            linecolor='black',
            linewidth=2,
            zeroline=True,
            zerolinecolor='black',
            zerolinewidth=1
        ),
    )

    return fig
