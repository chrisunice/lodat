from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

from ..app import app
from lodat.domain.data import DataObject


@app.callback(
    Output('polar-plot', 'figure'),
    Input('submit-button', 'n_clicks'),
    State('file-checklist', 'value'),
    State('freq-checklist', 'value'),
    State('pol-checklist', 'value')
)
def render_plot(submit_click: int, files: list, freqs: list, pols: list):
    if submit_click is None:
        raise PreventUpdate

    for file, freq, pol in zip(files, freqs, pols):
        obj = DataObject(file)
        # todo need to be able to get bin data from merge data
