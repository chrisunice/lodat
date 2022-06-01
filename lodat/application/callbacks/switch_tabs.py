from dash.dependencies import Input, Output

from ..app import app
from ..components.plots import polar_plot, linear_plot


@app.callback(Output('plot-contents', 'children'), Input('data-vis-tabs', 'active_tab'))
def switch_tabs(active_tab):
    if active_tab == 'polar':
        return polar_plot
    elif active_tab == 'linear':
        return linear_plot
    else:
        return None
