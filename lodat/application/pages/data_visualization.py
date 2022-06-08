import dash_bootstrap_components as dbc

from ..components.tabs import tab_bar

data_vis_page = dbc.Row(
    children=[
        dbc.Col(
            children=[
                dbc.Row(
                    id='row-1',
                    children=[
                        dbc.Col(
                            id='tab-contents',
                            children=[tab_bar],
                            width=9
                        )
                    ],
                    justify='center'
                ),
                dbc.Row(
                    id='row-2',
                    children=[
                        dbc.Col(
                            id='plot-contents'
                        )
                    ],
                    # align='stretch',
                    # style=dict(flex='1')
                )
            ],
            align='stretch'
        ),
    ],
    # align='center',
    # justify='center',
    style=dict(width='100%')
)