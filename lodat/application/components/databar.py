from dash import html
import dash_bootstrap_components as dbc


databar = dbc.Offcanvas(
    id='databar',
    children=[
        dbc.Spinner(
            dbc.Accordion(
                children=[
                    dbc.AccordionItem('No data loaded', id='data-selector-source', title='Data Source'),
                    dbc.AccordionItem('No frequencies available', id='data-selector-freq', title='Frequency'),
                    dbc.AccordionItem('No polarizations available', id='data-selector-pol', title='Polarization'),
                    dbc.AccordionItem('No depressions available', id='data-selector-depr', title='Depression')
                ],
                flush=True,
                start_collapsed=True,
                always_open=True
            ),
            color='primary',
            delay_show=10
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbc.Button('Submit', id='submit-button', color='primary', style=dict(width='60%')),
                        dbc.Button('Reset', id='reset-button', color='secondary', style=dict(width='35%'))
                    ],
                    style={
                        'display': 'flex',
                        'justify-content': 'space-between',
                        'margin-top': '10px'
                    }
                )
            ],
            style={
                'display': 'flex',
                'flex-direction': 'column',
                'flex': '1',
                'justify-content': 'flex-end',
                'width': '100%'
            }
        )
    ],
    title='Data Selector',
    scrollable=True,
    is_open=False,
    backdrop=False,
    placement='end',
    close_button=False,
    style={
        'marginTop': '50px',
        'width': '300px',
    }
)

# TODO still need to add all the components of the databar for selecting data
