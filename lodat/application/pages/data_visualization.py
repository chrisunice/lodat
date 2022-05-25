from dash import html, dcc


data_vis_page = html.Div(
    children=[
        dcc.Tabs(
            id='data-vis-tabs',
            children=[
                dcc.Tab(label='Polar'),
                dcc.Tab(label='Linear')
            ]
        )
    ]
)