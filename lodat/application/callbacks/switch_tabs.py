from dash import callback_context
from dash.dependencies import Input, Output

from ..app import app
from ..components.plots import polar_plot, linear_plot


@app.callback(
    Output('row-2', 'children'),
    [
        Input('data-vis-tabs', 'active_tab'),
        Input('url', 'pathname')
    ]
)
def switch_tabs(active_tab, pathname):
    input_fired = callback_context.triggered_id

    print(input_fired, pathname)
    if input_fired == 'url':
        if pathname == '/datavis':
            return polar_plot

    if input_fired == 'data-vis-tabs':
        if active_tab == 'polar':
            return polar_plot
        elif active_tab == 'linear':
            return linear_plot
        else:
            return None

# TODO need to figure out how to an active tab to show a plot on page load. pathname isnt working for /datavis
