from dash import html, dcc
import dash_bootstrap_components as dbc
from ..components.upload import upload


def horizontal_line():
    """ Creates a horizontal line """
    style = dict(
        width='100%',
        height='1px',
        color='white'
    )
    return html.Hr(style=style)


def menu_item(id_name: str, icon_name: str, text: str, link: bool = True):
    """ Creates a menu row item with icon and text """
    container_style = dict(display='flex', width='100%')
    button_style = dict(alignItems='center')
    icon_style = dict(color='white')
    text_style = dict(color='white', marginLeft='10px', fontSize='1rem')

    button = dbc.Button(
        [
            html.I(className=f"fa-solid fa-{icon_name} fa-xl", style=icon_style),
            html.Span(text, style=text_style)
        ],
        id=id_name,
        color='link',
        className='text-decoration-none',
        style=button_style
    )

    if not link:
        return html.Div(button, style=container_style)
    else:
        page_name = f"/{'-'.join(text.lower().split( ))}"
        return dcc.Link(button, href=page_name, style=container_style, className='text-decoration-none')


sidebar = dbc.Offcanvas(
    children=[
        html.Div(
            children=[
                html.H5('Menu'),
                horizontal_line(),
                menu_item('menu-upload', 'upload', 'Upload', link=False),
                upload,
                horizontal_line(),
                menu_item(id_name='menu-home', icon_name='home', text='Home', link=True),
                horizontal_line(),
                menu_item(id_name='menu-data-vis', icon_name='chart-area', text='Data Visualization', link=True),
                horizontal_line(),
                menu_item(id_name='menu-imagery', icon_name='images', text='Imagery', link=True),
            ],
            style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}
        )
    ],
    id="sidebar",
    scrollable=True,
    is_open=False,
    close_button=False,
    style={'display': 'flex', 'marginTop': '50px', 'width': '200px', 'padding': '0px'}
)
