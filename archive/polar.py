from dash import html, dcc
import plotly.graph_objects as go

polar_page = html.Div(
    children=[
        dcc.Graph(
            id='polar-plot',
            figure=go.Figure(go.Scatterpolargl(dict(r=None, theta=None))),
            style=dict(width='90vh', height='90vh')
        )
    ]
)
