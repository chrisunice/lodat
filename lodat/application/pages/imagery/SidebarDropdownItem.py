from dash import html, dcc


def sidebar_dropdown_item(label_text: str, options: list[dict] = None, multi: bool = False):
    dropdown_id = f"{label_text.replace(' ', '-').lower()}-dropdown"

    component_style = {'width': '100%'}

    return html.Div(
        children=[
            html.Label(label_text),
            dcc.Dropdown(id=dropdown_id, options=options, multi=multi)
        ],
        style=component_style
    )
