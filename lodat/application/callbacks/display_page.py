from dash.dependencies import Output, Input

from .. import pages
from ..app import app


@app.callback(
    Output('page-container', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/home':
        return pages.home_page
    elif pathname == '/data-visualization':
        return pages.data_vis_page
    elif pathname == '/imagery':
        return pages.imagery.layout
    else:
        # todo add an alert here
        return pages.home_page
