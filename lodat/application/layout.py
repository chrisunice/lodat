from dash import html, dcc

from .components.navbar import navbar
from .components.sidebar import sidebar

app_styles = {
    'display': 'flex',
    'flex-direction': 'column',
    'min-height': '100vh'
}

container_styles = {
    'display': 'flex',
    'flex': '1',
}

layout = html.Div(
    id='dash-layout',
    children=[
        dcc.Location(id='url', refresh=True),
        # dcc.Store(id='session-store', storage_type='session'),
        dcc.Loading(dcc.Store(id="cache-store"), fullscreen=True, type="dot"),  # todo still work to be done here
        navbar,
        sidebar,
        html.Div(id='page-container', style=container_styles)
    ],
    style=app_styles
)
