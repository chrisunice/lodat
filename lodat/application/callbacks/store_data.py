# TODO still a lot of work to be done here
# NOTE dash-resumable-upload may be worth exploring
import io
import json
import base64
import pandas as pd
from dash.exceptions import PreventUpdate
# from dash.dependencies import Input, Output, State
from dash_extensions.enrich import ServersideOutput, Input, Output, State

from ..app import app

import time
import plotly.express as px


@app.callback(
    ServersideOutput('cache-store', 'data'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    prevent_initial_call=True
)
def store_uploaded_data(content_list, name_list):
    if content_list is None:
        raise PreventUpdate

    # Step through all the data loaded
    for content, name in zip(content_list, name_list):

        # Decode the data
        content_type, content_string = content.split(',')
        decoded = base64.b64decode(content_string)

        # Dandle csv data
        if name.endswith('.csv'):
            df = pd.read_csv(io.BytesIO(decoded), index_col=0)

    return df

# @app.callback(
#     [ServersideOutput('cache-store', 'data'),
#      Output('loading-state', 'children')],
#     Input('upload-data', 'contents'),
#     State('upload-data', 'filename'),
#     State('cache-store', 'data'),
#     prevent_initial_call=True
# )
# def store_uploaded_data(content_list, name_list, existing_data):
#     if content_list is None:
#         raise PreventUpdate
#     else:
#         # Check to see if data already exists in the session
#         if existing_data is not None:
#             data = json.loads(existing_data)
#         else:
#             data = dict()
#
#         # Step through all the data loaded
#         for content, name in zip(content_list, name_list):
#
#             # Decode the data
#             content_type, content_string = content.split(',')
#             decoded = base64.b64decode(content_string)
#
#             # Dandle csv data
#             if name.endswith('.csv'):
#                 df = pd.read_csv(io.BytesIO(decoded), index_col=0)
#                 data[name] = df.to_dict()
#
#         # Convert dictionary to JSON string
#         return json.dumps(data), ""
