from dash import html

from ..components.upload import upload

page_styles = {
    'display': 'flex',
    'justify-content': 'center',
    'align-items': 'center',
    'width': '100%'
}

home_page = html.Div(
    id='home-page',
    children=[upload],
    style=page_styles
)

