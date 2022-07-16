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
def set_band_options(_):
    dbm = ImageryDatabaseManager()
    platforms = dbm.platforms
    bands = dbm.bands
    pols = dbm.polarizations
    dbm.close()
    return platforms, bands, pols


# @app.callback(
#     Output('polarization-dropdown', 'options'),
#     Input('sql-database-dropdown', 'value')
# )
# def set_pol_options(_):
#
#     return ['HH', 'VV']
