from dash import html

from ..components.upload import upload


home_page = html.Div(
    children=[
        upload
    ]
)
