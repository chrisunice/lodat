import io
import base64
import pandas as pd

from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

from ..app import app


@app.callback(Output('store', 'data'), Input('upload-data', 'contents'))
def do_something_with_data(contents):
    if contents is None:
        raise PreventUpdate

    # Data has been uploaded
    if bool(contents):
        content_type, content_string = contents[0].split(',')
        decoded = base64.b64decode(content_string)
        buffer = io.BytesIO(decoded)
        df = pd.read_csv(buffer, index_col=0)
        return df
    