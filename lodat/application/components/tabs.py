import dash_bootstrap_components as dbc


def create_tab(tab_name):
    tab = dbc.Tab(
        label=tab_name,
        tab_id=tab_name.lower(),
        tab_style=dict(padding='0'),
        active_tab_style=dict(padding='0')
    )
    return tab


tab_bar = dbc.Tabs(
    id='data-vis-tabs',
    class_name='nav nav-tabs',
    children=[
        create_tab('Polar'),
        create_tab('Linear'),
        create_tab('SADA')
    ],
    active_tab='polar',
    style=dict(display='flex', justifyContent='center', alignItems='center')
)


