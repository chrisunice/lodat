import dash
import dash_bootstrap_components as dbc

# Application set up
app = dash.Dash(
    name='LODAT',
    external_stylesheets=[
        dbc.themes.CYBORG,
        dbc.icons.FONT_AWESOME,
    ],
    suppress_callback_exceptions=True
)
