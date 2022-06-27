from dash.dependencies import Output, Input

from .. import pages
from ..app import app


@app.callback(
    Output('page-container', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return pages.home_page
    elif pathname == '/datavis':
        return pages.data_vis_page
    else:
        return pages.home_page
