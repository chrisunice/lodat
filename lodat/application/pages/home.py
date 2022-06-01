import dash_bootstrap_components as dbc

from ..components.upload import upload


home_page = dbc.Col(
    children=[
        upload
    ],
    width=6,
    align='center'
)
