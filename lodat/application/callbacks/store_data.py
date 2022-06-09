import io
import json
import base64
import pandas as pd
from dash.dependencies import Input, Output, State

from ..app import app


@app.callback(
    Output('session-store', 'data'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
)
def store_uploaded_data(content_list, name_list):
    if content_list is not None:

        # Data dictionary to fill
        data = dict()

        # Step through all the data loaded
        for content, name in zip(content_list, name_list):

            # Decode the data
            content_type, content_string = content.split(',')
            decoded = base64.b64decode(content_string)

            # Dandle csv data
            if name.endswith('.csv'):
                df = pd.read_csv(io.BytesIO(decoded), index_col=0)
                data[name] = df.to_dict()

        # Convert dictionary to JSON string
        return json.dumps(data)
