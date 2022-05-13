from dash import html
import dash_bootstrap_components as dbc

sidebar = dbc.Offcanvas(
    children=[
        # todo add links to pages
    ],
    id="sidebar",
    title='Menu',
    scrollable=True,
    is_open=False,
    close_button=False,
    style=dict(
        display='flex',
        marginTop='50px'
    )
)


