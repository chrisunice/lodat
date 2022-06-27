from dash import html
import dash_bootstrap_components as dbc


databar = dbc.Offcanvas(
    id='databar',
    children=[
        dbc.Accordion(
            children=[
                dbc.AccordionItem('No data loaded', id='data-selector-source', title='Data Source'),
                dbc.AccordionItem('No frequencies available', id='data-selector-freq', title='Frequency'),
                dbc.AccordionItem('No polarizations available', id='data-selector-pol', title='Polarization')
            ],
            flush=True,
            start_collapsed=True,
            always_open=True
        ),
        html.Div(
            children=[
                dbc.Button('Submit', id='submit-button', color='primary'),
                dbc.Button('Reset', id='reset-button', color='secondary')
            ],
            style={
                'display': 'flex',
                'justify-content': 'space-evenly',
                'margin': '5px'
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
