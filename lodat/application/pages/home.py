from dash import html, dcc
import dash_bootstrap_components as dbc

from ..components.upload import upload

page_styles = {
    'display': 'flex',
    'flex': '1',
    'flex-direction': 'column',
    'justify-content': 'center',
    'align-items': 'center',
    'width': '100%',
}

home_page = html.Div(
    id='home-page',
    children=[
        upload,
        dbc.Spinner(
            html.Div(
                id='loading-state',
                style=dict(width='50px', height='50px')
            ),
            color='primary',
            delay_hide=100  # in milliseconds
        )
    ],
    style=page_styles
)

