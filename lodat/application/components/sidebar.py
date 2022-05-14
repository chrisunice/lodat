from dash import html, dcc
import dash_bootstrap_components as dbc

sidebar = dbc.Offcanvas(
    children=[
        dcc.Link('Home', id='home-link', href='/'),
        html.Br(),
        dcc.Link('Polar Plot', id='polar-link', href='/polarplot'),
        html.Br(),
        dcc.Link('Linear Plot', id='linear-link', href='/linearplot'),
    ],
    id="sidebar",
    title='Menu',
    scrollable=True,
    is_open=False,
    close_button=False,
    style=dict(
        display='flex',
        marginTop='50px',
        width='200px'
    )
)


