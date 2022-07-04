from dash import html, dcc
import dash_bootstrap_components as dbc


def horizontal_line():
    style = dict(
        width='100%',
        height='1px',
        color='white'
    )
    return html.Hr(style=style)


def menu_item(id_name, icon_name, text):
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
                horizontal_line(),
                dcc.Link(
                    menu_item('menu-data-vis', 'chart-area', 'Data Visualization'),
                    id='data-vis-link',
                    href='/datavis',
                    className='text-decoration-none'
                ),
                horizontal_line()
            ],
            style={
                'display': 'flex',
                'flex-direction': 'column',
                'align-items': 'center',
            }
        )
    ],
    id="sidebar",
    scrollable=True,
    is_open=False,
    close_button=False,
    style=dict(
        display='flex',
        marginTop='50px',
        width='200px',
        padding='0px',
    )
)


# TODO need to figure out how to center and space the sidebar contents
