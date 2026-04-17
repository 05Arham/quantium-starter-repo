import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_csv('formatted_output.csv')
df = df.sort_values(by='date')

app = dash.Dash(__name__)

fig = px.line(df, x='date', y='sales', title='Pink Morsel Sales Over Time')
fig.update_layout(xaxis_title='Date', yaxis_title='Sales ($)')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Visualizer', id='header'),
    dcc.Graph(id='sales-chart', figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)