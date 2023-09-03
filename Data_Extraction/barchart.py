import pandas as pd
import plotly.graph_objects as go

def create_barchart(df):
    # Assuming df is passed as a parameter
    # No need to read the CSV again here
    
    df_renamed = df.rename(columns={
        'ARB11841-USD': 'ARB',
        'BTC-USD': 'BTC',
        'DYDX-USD': 'DYDX',
        'ETH-USD': 'ETH',
        'LDO-USD': 'LDO',
        'LINK-USD': 'LINK',
        'MATIC-USD': 'MATIC',
        'OP-USD': 'OP',
        'PRIME23711-USD': 'PRIME',
        'SOL-USD': 'SOL',
        'STX4847-USD': 'STX'
    })
    
    tickers = ['BTC', 'ETH', 'LDO', 'MATIC', 'ARB', 'LINK', 'SOL', 'OP', 'STX', 'DYDX', 'PRIME']
    
    df_filtered = df_renamed[tickers]
    
    for ticker in tickers:
        df_filtered[ticker] = (df_filtered[ticker].pct_change() + 1).cumprod().sub(1) * 100
    
    last_row = df_filtered.iloc[-1]
    text_values = [f'{value:.2f}%' for value in last_row]

    # Create a Plotly bar chart for the last performance
    fig = go.Figure(go.Bar(
        x=last_row.index,
        y=last_row,
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
