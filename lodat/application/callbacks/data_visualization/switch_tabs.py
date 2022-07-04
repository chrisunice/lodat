from dash.dependencies import Input, Output

from lodat.application.app import app
from lodat.application.components.plots import polar_plot, linear_plot


@app.callback(
    Output('row-2', 'children'),
    Input('data-vis-tabs', 'active_tab')
)
def switch_tabs(active_tab):
    if active_tab == 'polar':
        return polar_plot
    elif active_tab == 'linear':
        return linear_plot
    else:
        return None
