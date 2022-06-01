from dash import dcc
import plotly.graph_objects as go

linear_plot = dcc.Graph(
    id='linear-plot',
    figure=go.Figure(
        data=go.Scatter(dict(x=None, y=None)),
        layout=go.Layout()
    ),
    style=dict(width='90vh', height='90vh')
)

