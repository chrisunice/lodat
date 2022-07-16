from dash.dependencies import Input, Output

from lodat.application.app import app


@app.callback(
    Output('band-dropdown', 'options'),
    Input('sql-database-dropdown', 'value')
)
def set_band_options(value):
    return ['C', 'X', 'Ku']


@app.callback(
    Output('polarization-dropdown', 'options'),
    Input('sql-database-dropdown', 'value')
)
def set_band_options(value):
    return ['HH', 'VV']
