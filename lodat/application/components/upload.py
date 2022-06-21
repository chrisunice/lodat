import uuid
import dash_uploader

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

upload = dash_uploader.Upload(
    id='upload-data',
    text='Upload Data',
    default_style=upload_style,
    upload_id=str(uuid.uuid4())
)
