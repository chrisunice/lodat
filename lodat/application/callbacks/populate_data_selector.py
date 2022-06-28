import os
import json
from dash import dcc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

from ..app import app
from lodat.domain.data import DataObject


checklist_style = {
    'display': 'flex',
    'flex-direction': 'column',
}

input_style = {
    'margin-right': '10px'
}


@app.callback(
    Output('data-selector-source', 'children'),
    Input('filter-icon', 'n_clicks'),
    State('session-store', 'data'),
    State('data-selector-source', 'children')
)
def data_source(filter_click, data, original_content):
    # Modular to see if databar has been opened
    databar_is_open = (filter_click % 2 != 0)

    # Databar is open and data has been uploaded
    if databar_is_open and data is not None:
        data = json.loads(data)

        # Build options for checklist
        options = []
        for file in data.get('files'):
            full_path = f"{data.get('upload_dir')}\\{file}"
            file_name = os.path.splitext(file)[0]
            options.append(dict(label=file_name, value=full_path))

        # Return a checklist component
        return dcc.Checklist(id='file-checklist',
                             options=options,
                             inline=False,
                             style=checklist_style,
                             inputStyle=input_style,
                             persistence=True,
                             persistence_type='session')
    else:
        # Otherwise return the default component
        return original_content


@app.callback(
    Output('data-selector-freq', 'children'),
    Output('data-selector-pol', 'children'),
    Input('file-checklist', 'value')
)
def vector_group(sources):
    # Once a data source has been checked
    if sources is None:
        raise PreventUpdate

    freqs = []
    pols = []
    for source in sources:
        obj = DataObject(source)
        freqs += obj.frequencies
        pols += obj.polarizations

    freq_checklist = dcc.Checklist(
        id='freq-checklist',
        options=list(map(lambda x: f"{x} MHz", set(freqs))),
        style=checklist_style,
        inputStyle=input_style,
        persistence=True,
        persistence_type='session'
    )

    pol_checklist = dcc.Checklist(
        id='pol-checklist',
        options=list(set(pols)),
        style=checklist_style,
        inputStyle=input_style
    )
    return freq_checklist, pol_checklist
