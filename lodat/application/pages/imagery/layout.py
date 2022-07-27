from dash import html, dcc
import dash_bootstrap_components as dbc

from .Sidebar import Sidebar

page_style = {
    'display': 'flex',
    'flex-direction': 'column',
    'width': '100%',
    'justify-content': 'center',
    'align-items': 'center'
}


image_style = {
    'max-height': '480px',
    'max-width': '640px',
    'box-shadow': '0px 0px 10px #fff'
}

layout = html.Div(
    id='imagery-page',
    children=[
        dcc.Store(id='imagery-store', storage_type='memory'),
        Sidebar,
        dbc.Carousel(
            id='imagery-carousel',
            items=[
                {
                    'key': '1',
                    'src': '../static/black_image.jpg',
                }
            ],
            ride=False,
            style=image_style
        ),
        html.H6(id='carousel-caption', children=['Click the database icon to begin'], style={'margin': '10px'})
    ],
    style=page_style
)

