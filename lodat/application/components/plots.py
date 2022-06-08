from dash import dcc
import plotly.graph_objects as go

graph_style = dict()
graph_config = dict()

polar_plot = dcc.Graph(
    id='polar-plot',
    figure=go.Figure(
        data=go.Scatterpolargl(dict(r=None, theta=None)),
        layout=go.Layout()
    ),
    responsive=True,
    config=graph_config,
    style=graph_style
)

linear_plot = dcc.Graph(
    id='linear-plot',
    figure=go.Figure(
        data=go.Scatter(dict(x=None, y=None)),
        layout=go.Layout()
    ),
    responsive=True,
    style=graph_style
)

