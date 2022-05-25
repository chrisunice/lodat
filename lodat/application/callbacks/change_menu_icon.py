from dash.dependencies import Output, Input

from ..app import app


@app.callback(Output('menu-icon', 'className'), Input('sidebar', 'is_open'))
def change_menu_icon(is_open):
    if is_open:
        return 'fa-solid fa-xmark fa-2xl'
    else:
        return 'fa-solid fa-bars fa-2xl'
