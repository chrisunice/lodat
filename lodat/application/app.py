import dash
import requests
import dash_uploader
import dash_bootstrap_components as dbc
from configparser import ConfigParser


# Stylesheets
try:
    request = requests.get("http://www.google.com", timeout=1)
    sheets = [
        dbc.themes.CYBORG,
        dbc.icons.FONT_AWESOME
    ]
except (requests.exceptions.ConnectionError, requests.Timeout):
    sheets = [
        './assets/cyborg/bootstrap.min.css'
        './assets/fontawesome/all.css'
    ]

# Application set up
app = dash.Dash(
    name='LODAT',
    external_stylesheets=sheets,
    suppress_callback_exceptions=True
)

# Configure upload to server
config = ConfigParser()
config.read('./config.ini')
dash_uploader.configure_upload(
    app=app,
    folder=config['DEFAULT']['upload_folder'],
    use_upload_id=True
)
