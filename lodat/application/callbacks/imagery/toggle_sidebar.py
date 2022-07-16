from dash.dependencies import Input, Output, State

from lodat.application.app import app


@app.callback(
    Output('imagery-sidebar', 'is_open'),
    [
        Input('database-icon', 'n_clicks'),
        # todo this is where the submit button would go
    ],
    State('imagery-sidebar', 'is_open')
)
def toggle_sidebar(database_click, is_open):
    if database_click:
        return not is_open
