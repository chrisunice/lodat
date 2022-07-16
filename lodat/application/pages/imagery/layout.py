from dash import html
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
        Sidebar,
        dbc.Carousel(
            id='imagery-carousel',
            items=[
                {
                    'key': '1',
                    'src': '../static/black_image.jpg',
                    'caption': 'Select a database to begin'
                }
            ],
            ride=False,
            style=image_style
        )
    ],
    style=page_style
)

