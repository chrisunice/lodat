from dash import dcc
import plotly.graph_objects as go

graph_style = {
    'height': '100%',
    'width': '100%'
}

polar_plot = dcc.Graph(
    id='polar-plot',
    figure=go.Figure(
        data=go.Scatterpolargl(dict(r=None, theta=None)),
        layout=go.Layout(autosize=True)
    ),
    responsive=True,
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
