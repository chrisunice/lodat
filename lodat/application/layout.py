from dash import html, dcc

from .components.navbar import navbar
from .components.sidebar import sidebar


def serve_layout():

    app_styles = {
        'display': 'flex',
        'flex-direction': 'column',
        'min-height': '100vh'
    }

    container_styles = {
        'display': 'flex',
        'flex': '1',
    }
    return html.Div(
        id='dash-layout',
        children=[
            dcc.Location(id='url', refresh=True),
            dcc.Store(
                id='session-store',
                storage_type='session',
            ),
            html.Div(id='upload-data-output'),
            navbar,
            sidebar,
            html.Div(id='page-container', style=container_styles),
        ],
        style=app_styles
    )
