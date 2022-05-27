from dash import html
from ..components.tabs import tab_bar

data_vis_page = html.Div(
    children=[
        tab_bar,
        html.Div(
            id='plot-contents',
            style=dict(
                display='flex',
                justifyContent='center',
                padding='5px'
            )
        )
    ],
    style=dict(width='100%')
)
