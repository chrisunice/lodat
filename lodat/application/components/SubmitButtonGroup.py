from dash import html
import dash_bootstrap_components as dbc


def submit_button_group(uid: str):
    """
    :param uid: unique identifier for the component
    :return: submit/reset button group div
    """
    return html.Div(
        id=f'{uid}-button-container',
        children=[
            html.Div(
                children=[
                    dbc.Button('Submit', id=f'{uid}-submit-button', color='primary', style={'width': '60%'}),
                    dbc.Button('Reset', id=f'{uid}-reset-button', color='secondary', style={'width': '35%'})
                ],
                style={
                    'display': 'flex',
                    'justify-content': 'space-between',
                    'margin-top': '10px'
                }
            ),
        ],
        style={
            'display': 'flex',
            'flex-direction': 'column',
            'flex': '1',
            'justify-content': 'flex-end',
            'width': '100%'
        }
    )
