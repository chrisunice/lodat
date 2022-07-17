from dash import html, dcc


def sidebar_dropdown_item(label_text: str, options: list = None, multi: bool = False):
    if options is None:
        options = ['No data available']

    dropdown_id = f"{label_text.replace(' ', '-').lower()}-dropdown"

    component_style = {'width': '100%'}

    return html.Div(
        children=[
            html.Label(label_text),
            dcc.Dropdown(id=dropdown_id, options=options, multi=multi)
        ],
        style=component_style
    )
