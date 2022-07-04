"""
TODO fix the carousel that came out at a stupid small size when given images
"""
from dash import html
import dash_bootstrap_components as dbc

imagery_page = html.Div(
    id='imagery-page',
    children=[
        dbc.Carousel(id='imagery-carousel', items=[], style={'max-height': '500px'}),
        html.Img(id='test-image', style={'max-height': '50px'}),
        dbc.Button("Test", id='test-button', color='primary')
    ]
)

