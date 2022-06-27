from dash import html

from ..components.tabs import tab_bar
from ..components.databar import databar
from ..components.plots import polar_plot

page_styles = {
    'display': 'flex',
    'flex-direction': 'column',
    'align-items': 'center',
    'width': '100%',
    'padding': '10px',
}

row1_styles = {
    'width': '75%'
}

row2_styles = {
    'display': 'flex',
    'flex': '1',
    'align-items': 'center',
    'justify-content': 'center',
    'width': '90%',
    'margin': '10px',
}

data_vis_page = html.Div(
    id='data-vis-page',
    children=[
        databar,
        html.Div(id='row-1', children=[tab_bar], style=row1_styles),
        html.Div(id='row-2', children=[polar_plot], style=row2_styles)
    ],
    style=page_styles
)
