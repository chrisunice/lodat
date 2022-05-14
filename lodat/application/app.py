import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from lodat.application.layout import layout
from lodat.application.pages.home import home_page
from lodat.application.pages.polar import polar_page
from lodat.application.pages.linear import linear_page

# Application set up
external_stylesheets = [dbc.themes.CYBORG, dbc.icons.FONT_AWESOME]
app = dash.Dash(name='LODAT', external_stylesheets=external_stylesheets)
app.layout = layout


# Connecting callbacks
@app.callback(Output("sidebar", "is_open"),
              [Input("menu-icon", "n_clicks"),
               Input("url", "pathname")],
              State("sidebar", "is_open"))
def toggle_sidebar(menu_click, link_click, is_open):
    # If menu button is clicked open or close the sidebar
    if menu_click:
        return not is_open

    # If sidebar is already open and link is clicked
    if is_open and link_click:
        return False


@app.callback(Output('menu-icon', 'className'), Input('sidebar', 'is_open'))
def change_menu_icon(is_open):
    if is_open:
        return 'fa-solid fa-xmark fa-2xl'
    else:
        return 'fa-solid fa-bars fa-2xl'


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home_page
    elif pathname == '/polarplot':
        return polar_page
    elif pathname == '/linearplot':
        return linear_page
    else:
        # TODO add 404 error page not found
        return


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
