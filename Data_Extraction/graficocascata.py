import pandas as pd
import plotly.graph_objects as go

def create_portfolio_returns_plot(df, tickers):
    # Calculate cumulative returns for individual assets
    tickers = ['BTC', 'ETH', 'LDO', 'MATIC', 'ARB', 'LINK', 'SOL', 'OP', 'STX', 'DYDX', 'PRIME']

    for i in tickers: 
        df[i] = df[i].pct_change().add(1).cumprod().sub(1) * 100

    # Create a Plotly scatter plot for the non-empty plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Datetime'], y=df['Total'], line_color='#623AD7', mode='lines'))

    # Configure layout of the non-empty plot
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
            linewidth=2
        ),
        legend=dict(
            orientation='h',
            x=0.01,
            y=1.1,
            bgcolor='white'
        )
    )
    
    fig.update_yaxes(zeroline=True, zerolinecolor='black', zerolinewidth=1)
    return fig
