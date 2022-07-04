"""
Note this may not work for different users because the os.getlogin() may be specific to the server not the client
TODO to figure out how to maintain the same unique session id for a users session, it changes each time
"""
import os
import uuid
import dash_uploader
import dash_bootstrap_components as dbc

upload_style = {
    'display': 'flex',
    'justify-content': 'center',
    'align-items': 'center',
    'width': '100%',
    'lineHeight': '60px',
    'borderWidth': '1px',
    'borderStyle': 'dashed',
    'borderRadius': '5px',
    'textAlign': 'center',
    'margin': '10px'
}

upload = dbc.Modal(
    id='upload-modal',
    children=[
        dbc.ModalBody(
            dash_uploader.Upload(
                id='upload-data',
                text='Drag and Drop or Click to Upload',
                chunk_size=5,
                default_style=upload_style,
                upload_id=f"{os.getlogin()}-{str(uuid.uuid4())}"
            )
        ),
        dbc.ModalFooter(
            dbc.Button('Close', className='primary', id='upload-modal-close')
        )
    ],
    is_open=False
)
