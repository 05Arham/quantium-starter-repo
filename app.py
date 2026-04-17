import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('formatted_output.csv')
df = df.sort_values(by='date')

app = dash.Dash(__name__)

app.layout = html.Div(style={'textAlign': 'center', 'fontFamily': 'sans-serif', 'padding': '50px', 'backgroundColor': '#f9f9f9'}, children=[
    
    html.H1("Pink Morsel Sales Visualizer", style={'color': '#2c3e50'}),

    html.Div([
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            inline=True,
            style={'display': 'inline-block'}
        )
    ], style={'marginBottom': '30px'}),

    dcc.Graph(id='sales-chart')
])

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(region):
    if region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region]
    
    fig = px.line(filtered_df, x='date', y='sales', title=f'Sales for {region.capitalize()} Region')
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run(debug=True)