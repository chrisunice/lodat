from dash import html, dcc
from .components.navbar import navbar
from .components.sidebar import sidebar

layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=True),
        navbar,
        sidebar,
        html.Div(
            id='page-content',
            style=dict(display='flex', padding='10px', justifyContent='center')
        )
    ]
)
