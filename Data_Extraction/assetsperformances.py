import pandas as pd
import plotly.graph_objects as go

def create_assets_returns(df):
    # Calculate cumulative returns for individual assets
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

    for i in tickers: 
        df[i] = df[i].pct_change().add(1).cumprod().sub(1) * 100
    
    for i in tickers: 
        df[i] = df[i].rolling(7).mean()

    # Create a Plotly scatter plot for the non-empty plot
    fig = go.Figure()

    for i in tickers:
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df[i], mode='lines',name=i))

    # Configure layout of the non-empty plot
    fig.update_layout(
        title='Rentabilidade acumulada ativos',
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
            linewidth=2
        ),
        legend=dict(
            orientation='h',
            x=0.01,
            y=1.15,
            bgcolor='white',
            font=dict(size=8)  # Adjust the font size as needed
        )
    )

    return fig
