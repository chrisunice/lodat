import os
from dash import dcc, html
import dash_bootstrap_components as dbc

from lodat.application import config
from lodat.application.components.HorizontalLine import HorizontalLine
from lodat.application.components.SubmitButtonGroup import submit_button_group

from .SidebarDropdownItem import sidebar_dropdown_item

sidebar_style = {
    'margin-top': '50px',
    'width': '300px'
}

container_style = {
    'display': 'flex',
    'flex-direction': 'column',
    'align-items': 'center'
}

Sidebar = dbc.Offcanvas(
    id='imagery-sidebar',
    children=[
        html.Div(
            children=[
                html.H5('Query Filter'),
                HorizontalLine,
                sidebar_dropdown_item(
                    label_text='SQL Database',
                    options=[{'label': os.path.basename(config.imagery_database_path),
                              'value': config.imagery_database_path}]
                ),
                HorizontalLine,
                sidebar_dropdown_item('Platform', multi=True),
                HorizontalLine,
                sidebar_dropdown_item('Band', multi=True),
                HorizontalLine,
                sidebar_dropdown_item('Polarization', multi=True),
                HorizontalLine,
            ],
            style=container_style
        ),
        submit_button_group('imagery-sidebar')
    ],
    scrollable=False,
    is_open=False,
    backdrop=False,
    placement='end',
    close_button=False,
    style=sidebar_style
)
