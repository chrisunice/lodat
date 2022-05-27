from dash.dependencies import Input, Output

from ..app import app
from ..components.polarplot import polar_plot
from ..components.linearplot import linear_plot


@app.callback(Output('plot-contents', 'children'), Input('data-vis-tabs', 'value'))
def display_plot(value):
    if value == 'polar':
        return polar_plot
    elif value == 'linear':
        return linear_plot
    else:
        return None
