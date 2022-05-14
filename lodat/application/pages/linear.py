from dash import html, dcc
import plotly.graph_objects as go

linear_page = html.Div(
    children=[
        dcc.Graph(
            id='linear-plot',
            figure=go.Figure(go.Scattergl(dict(x=None, y=None))),
            style=dict(width='90vh', height='90vh')
        )
    ]
)
