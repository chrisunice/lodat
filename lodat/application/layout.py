from dash import html, dcc
import dash_bootstrap_components as dbc

from .components.navbar import navbar
from .components.sidebar import sidebar


# layout = dbc.Container(
#     id='dash-container',
#     children=[
#         dcc.Location(id='url', refresh=True),
#         dcc.Store(id='store', storage_type='session'),
#         dbc.Row(
#             dbc.Col(navbar),
#         ),
#         sidebar,
#         dbc.Row(
#             id='page-contents',
#         )
#     ],
#     fluid=True,
#     style={
#         # 'min-height': '100vh',
#         # 'padding': '0px'
#     }
# )

layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=True),
        dcc.Store(id='store', storage_type='session'),
        navbar,
        html.Div(
            children=['My Test Text'],
            style={
                'flex': '1',
                'overflow': 'auto',
                'background': 'red'
            }
        ),
        dbc.Container(
            id='dash-container',
            children=[
                sidebar,
                dbc.Row(id='page-contents')
            ],
            fluid=True,
        )
    ],
    style={
        'flex-flow': 'column',
        'min-height': '100vh'
    }
)
