from dash import html, dcc


def sidebar_input_item(label_text: str):
    input_id = label_text.replace(' ', '-').lower()
    component_style = {'display': 'flex', 'justify-content': 'space-between', 'width': '100%'}

    col1_style = {'display': 'flex', 'align-items': 'center'}
    col2_style = {
        'display': 'flex',
        'flex-direction': 'row',
        'justify-content': 'space-evenly',
        'align-items': 'center',
        'width': '70%'
    }
    input_style = {'width': '40%'}

    return html.Div(
        children=[
            html.Div(
                id='col-1',
                children=[html.Span(label_text)],
                style=col1_style
            ),
            html.Div(
                id='col-2',
                children=[
                    dcc.Input(
                        id=f"{input_id}-center-input",
                        type='number',
                        min=0,
                        max=359,
                        step=1,
                        debounce=True,
                        style=input_style
                    ),
                    html.I(className='fa-solid fa-plus-minus'),
                    dcc.Input(
                        id=f"{input_id}-tolerance-input",
                        type='number',
                        min=0,
                        max=10,
                        step=0.1,
                        debounce=True,
                        style=input_style
                    )
                ],
                style=col2_style
            )
        ],
        style=component_style
    )


