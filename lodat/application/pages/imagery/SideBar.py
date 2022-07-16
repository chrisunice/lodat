import os
from dash import dcc, html
import dash_bootstrap_components as dbc

from lodat.application import config
from lodat.application.components.HorizontalLine import HorizontalLine

sidebar_style = {
    'margin-top': '50px',
    'width': '300px'
}

container_style = {
    'display': 'flex',
    'flex-direction': 'column',
    'align-items': 'center'
}

SideBar = dbc.Offcanvas(
    id='imagery-sidebar',
    children=[
        html.Div(
            children=[
                html.H5('Query Filter'),
                HorizontalLine,
                html.Div(
                    children=[
                        html.Label('SQL Database'),
                        dcc.Dropdown(
                            id='sql-database-dropdown',
                            options=[
                                {
                                    'label': os.path.basename(config.imagery_database_path),
                                    'value': config.imagery_database_path
                                }
                            ]
                        )
                    ],
                    style={'width': '100%'},
                ),
                HorizontalLine,
                html.Div(
                    children=[
                        html.Label('Band'),
                        dcc.Dropdown(id='band-dropdown', multi=True)
                    ],
                    style={'width': '100%'},
                ),
                HorizontalLine,
                html.Div(
                    children=[
                        html.Label('Polarization'),
                        dcc.Dropdown(id='polarization-dropdown', multi=True)
                    ],
                    style={'width': '100%'},
                ),
                HorizontalLine
            ],
            style=container_style
        )
    ],
    scrollable=False,
    is_open=False,
    backdrop=False,
    placement='end',
    close_button=False,
    style=sidebar_style
)
