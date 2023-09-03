import pandas as pd
import plotly.graph_objects as go

def create_waterfall_chart(df1):
    df1.rename(columns={'ARB11841-USD': 'ARB'}, inplace=True)
    df1.rename(columns={'BTC-USD': 'BTC'}, inplace=True)
    df1.rename(columns={'DYDX-USD': 'DYDX'}, inplace=True)
    df1.rename(columns={'ETH-USD': 'ETH'}, inplace=True)
    df1.rename(columns={'LDO-USD': 'LDO'}, inplace=True)
    df1.rename(columns={'LINK-USD': 'LINK'}, inplace=True)
    df1.rename(columns={'MATIC-USD': 'MATIC'}, inplace=True)
    df1.rename(columns={'OP-USD': 'OP'}, inplace=True)
    df1.rename(columns={'PRIME23711-USD': 'PRIME'}, inplace=True)
    df1.rename(columns={'SOL-USD': 'SOL'}, inplace=True)
    df1.rename(columns={'STX4847-USD': 'STX'}, inplace=True)

    df1 = df1.iloc[-1:]
    
    # Convert performance values to numeric
    df1.iloc[0] = pd.to_numeric(df1.iloc[0], errors='coerce')
    
    # Remove the 'Total' column
    df1 = df1.drop(columns=['Datetime'])
    df1 = df1.drop(columns=['Total'])
    
    # Sort columns by their absolute values in descending order
    sorted_columns = df1.iloc[0].abs().sort_values(ascending=False).index
    
    # Sort the dataframe columns based on the sorted order
    df1_sorted = df1[sorted_columns]
    
    # Calculate total performance
    total_performance = df1_sorted.values[0].sum()
    
    # Create the waterfall chart using Plotly
    fig = go.Figure(go.Waterfall(
        orientation="v",
        textposition="outside",
        measure=df1_sorted.columns,
        x=df1_sorted.columns,
        y=df1_sorted.iloc[0],
        text=[f"{val:.2f}%" for val in df1_sorted.iloc[0].round(decimals=2)],
        connector={"line": {"color": "rgb(63, 63, 63)"}},
        decreasing={"marker": {"color": "#8A85A8"}},
        increasing={"marker": {"color": "#623AD7"}},
    ))
    
    # Add a separate bar for total performance
    fig.add_trace(go.Bar(
        x=["Total"],
        y=[total_performance],
        marker=dict(color="#060528"),
        text=[f"{total_performance:.2f}%"],
        textposition="auto",
    ))
    

    
    fig.update_layout(
        title='Performance Agregada por ativos',
        title_x=0.5,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_family='Outfit',
        showlegend=False,
        xaxis_title='',
        yaxis_title='',
        xaxis=dict(
            showline=True,
            linecolor='black',
            showgrid=True,
            linewidth=2
        ),
        yaxis=dict(
            ticksuffix='%',
            showline=True,
            linecolor='black',
            linewidth=2
        ),
    )
    
    return fig
