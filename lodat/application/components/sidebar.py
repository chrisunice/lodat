from dash import html, dcc
import dash_bootstrap_components as dbc


sidebar = dbc.Offcanvas(
    children=[
        dcc.Link('Home', id='home-link', href='/'),
        html.Br(),
        dcc.Link('Data Visualization', id='data-vis-link', href='/datavis'),
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


# TODO need to figure out how to center and space the sidebar contents