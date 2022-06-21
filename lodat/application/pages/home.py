from dash import html, dcc

from ..components.upload import upload

page_styles = {
    'display': 'flex',
    'flex': '1',
    'flex-direction': 'column',
    'justify-content': 'center',
    'align-items': 'center',
    'width': '100%',
}

home_page = html.Div(
    id='home-page',
    children=[
        upload,
        html.Div(id='upload-data-output')
    ],
    style=page_styles
)

