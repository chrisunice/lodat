from dash.dependencies import Input, Output, State

from ..app import app


@app.callback(
    Output("sidebar", "is_open"),
    [
        Input("menu-icon", "n_clicks"),
        Input("url", "pathname")
    ],
    State("sidebar", "is_open")
)
def toggle_sidebar(menu_click, link_click, is_open):
    # If menu button is clicked open or close the sidebar
    if menu_click:
        return not is_open

    # If sidebar is already open and link is clicked
    if is_open and link_click:
        return False
