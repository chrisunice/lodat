from dash import html
import dash_bootstrap_components as dbc

from ..components.tabs import tab_bar

data_vis_page = dbc.Row(
    dbc.Col(
        children=[
            dbc.Row(
                children=[
                    dbc.Col(
                        tab_bar,
                        width=9
                    )
                ],
                justify='center'
            ),
            dbc.Row(id='plot-contents', justify='center')
        ],
        align='stretch'
    )
)
