from dash.dependencies import Input, Output

from lodat.application.app import app
from lodat import ImageryDatabaseManager


@app.callback(
    Output('platform-dropdown', 'options'),
    Output('band-dropdown', 'options'),
    Output('polarization-dropdown', 'options'),
    Input('sql-database-dropdown', 'value'),
    prevent_initial_call=True
)
def populate_sidebar(_):
    dbm = ImageryDatabaseManager()
    platforms = dbm.platforms
    bands = dbm.bands
    pols = dbm.polarizations
    dbm.close()
    return platforms, bands, pols
