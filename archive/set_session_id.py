from dash.dependencies import Input, Output

from ..app import app


@app.callback(Output('session-store', 'data'), Input('upload-data', 'upload_id'))
def set_session_id(uid):
    return {'session-id': uid}

