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
    State('session-store', 'data')
)
def data_source(filter_click, data):
    if filter_click:
        data = json.loads(data)
        files = [os.path.splitext(file)[0] for file in data.get('files')]
        return dcc.Checklist(
            options=files,
            inline=False,
            style=checklist_style
        )
