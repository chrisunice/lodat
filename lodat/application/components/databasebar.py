from dash import dcc
import dash_bootstrap_components as dbc

from lodat.application import config

databasebar = dbc.Offcanvas(
    id='databasebar',
    children=[
        dcc.Dropdown()
    ]
)