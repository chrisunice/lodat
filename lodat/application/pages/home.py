import dash_bootstrap_components as dbc

from ..components.upload import upload


home_page = dbc.Row(
    dbc.Col(
        children=[
            upload
        ],
        width=6
    ),
    class_name='h-100',
    justify='center',
)
