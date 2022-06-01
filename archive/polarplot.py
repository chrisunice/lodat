from dash import dcc
import plotly.graph_objects as go

polar_plot = dcc.Graph(
    id='polar-plot',
    figure=go.Figure(
        data=go.Scatterpolargl(dict(r=None, theta=None)),
        layout=go.Layout()
    ),
    style=dict(width='90vh', height='90vh')
)
