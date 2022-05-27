from dash import dcc


def create_tab(tab_name):
    component = dcc.Tab(
        label=tab_name,
        value=tab_name.lower(),
        style=dict(padding='0'),
        selected_style=dict(padding='0')
    )
    return component


tab_bar = dcc.Tabs(
    id='data-vis-tabs',
    value='polar',
    children=[
        create_tab('Polar'),
        create_tab('Linear'),
        create_tab('SADA')
    ],
    style=dict(display='flex', justifyContent='center', alignItems='center')
)
