import os
import uuid
import dash_uploader
import dash_bootstrap_components as dbc

upload_style = {
    'display': 'flex',
    'justify-content': 'center',
    'align-items': 'center',
    'width': '33%',
    'height': '60px',
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
        dbc.ModalHeader(dbc.ModalTitle('Upload Data')),
        dbc.ModalBody(
            dash_uploader.Upload(
                id='upload-data',
                text='Upload Data',
                default_style=upload_style,
                upload_id=f"{os.getlogin()}-{str(uuid.uuid4())}"  # Note this may not work for different users
            )
        ),
        dbc.ModalFooter(
            dbc.Button('Close', className='primary', id='upload-modal-close')
        )
    ],
    is_open=False
)


