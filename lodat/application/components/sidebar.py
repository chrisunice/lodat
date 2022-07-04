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


def menu_item(id_name, icon_name, text):
    """ Creates a menu row item with icon and text """
    button_style = dict(display='flex', alignItems='center')
    icon_style = dict(color='white')
    text_style = dict(color='white', marginLeft='10px', fontSize='1rem')
    return html.Div(
        dbc.Button(
            id=id_name,
            children=[
                html.I(className=f"fa-solid fa-{icon_name} fa-xl", style=icon_style),
                html.Span(text, style=text_style)
            ],
            color='link',
            className='text-decoration-none',
            style=button_style
        ),
        style=dict(display='flex')
    )


sidebar = dbc.Offcanvas(
    children=[
        html.Div(
            children=[
                html.H5('Menu'),
                horizontal_line(),
                menu_item('menu-upload', 'upload', 'Upload'),
                upload,
                horizontal_line(),
                dcc.Link(menu_item('menu-home', 'home', 'Home'), href='/', className='text-decoration-none'),
                horizontal_line(),
                dcc.Link(
                    menu_item('menu-data-vis', 'chart-area', 'Data Visualization'),
                    href='/datavis',
                    className='text-decoration-none'
                ),
                horizontal_line()
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
