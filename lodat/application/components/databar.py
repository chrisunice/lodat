from dash import html
import dash_bootstrap_components as dbc

from lodat.application.components.SubmitButtonGroup import submit_button_group

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
        submit_button_group('data-vis-sidebar')
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
