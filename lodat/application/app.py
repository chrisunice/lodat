import dash
import dash_bootstrap_components as dbc

import requests

# Stylesheets
try:
    request = requests.get("http://www.google.com", timeout=1)
    sheets = [
        dbc.themes.CYBORG,
        dbc.icons.FONT_AWESOME
    ]
except (requests.exceptions.ConnectionError, requests.Timeout):
    print('Offline, using offline sheets')
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
