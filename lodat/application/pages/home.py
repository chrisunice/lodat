import dash_bootstrap_components as dbc

from ..components.upload import upload


home_page = dbc.Row(
    id='home-contents',
    children=[
        dbc.Col(
            children=[
                upload
            ],
            width=6,
            align='center'
        )
    ],
    justify='center',
    style=dict(width='100%')
)

