from dash import html
from .components.navbar import navbar
from .components.sidebar import sidebar

LAYOUT = html.Div(
    children=[
        navbar,
        sidebar
    ]
)
