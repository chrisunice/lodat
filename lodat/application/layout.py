from dash import html, dcc
import dash_bootstrap_components as dbc

from .components.navbar import navbar
from .components.sidebar import sidebar

layout = html.Div(
    id='dash-layout',
    children=[
        dcc.Location(id='url', refresh=True),
        dcc.Store(id='store', storage_type='session'),
        navbar,
        dbc.Container(
            id='page-container',
            children=[
                sidebar,
                dbc.Row(
                    id='page-contents',
                    justify='center',
                    style=dict(flex='1')
                )
            ],
            fluid=True,
            style=dict(
                display='flex',
                flex='1',
            )
        )
    ],
    style={
        'display': 'flex',
        'flex-flow': 'column',
        'min-height': '100vh'
    }
)
