import os
import json
from dash import dcc
from ..app import app
from dash.dependencies import Input, Output, State

checklist_style = {
    'display': 'flex',
    'flex-direction': 'column'
}


@app.callback(
    Output('data-selector-source', 'children'),
    Input('filter-icon', 'n_clicks'),
    State('session-store', 'data'),
    State('data-selector-source', 'children')
)
def data_source(filter_click, data, original_content):
    databar_is_open = (filter_click % 2 != 0)
    if databar_is_open and data is not None:
        data = json.loads(data)
        files = [os.path.splitext(file)[0] for file in data.get('files')]
        return dcc.Checklist(
            options=files,
            inline=False,
            style=checklist_style
        )
    else:
        return original_content
