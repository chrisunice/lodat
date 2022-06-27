from dash.dependencies import Output, Input, State

from ..app import app


@app.callback(
    Output('filter-icon', 'style'),
    Input('url', 'pathname'),
    State('filter-icon', 'style')
)
def show_filter_icon(pathname: str, style: dict):
    on_data_vis_page = pathname == '/datavis'
    if on_data_vis_page:
        style['display'] = 'inline'
    else:
        style['display'] = 'none'
    return style
