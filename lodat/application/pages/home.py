from dash import html

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
        html.H6('Select an option in the menu'),
    ],
    style=page_styles
)

