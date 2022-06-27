import dash_bootstrap_components as dbc

databar = dbc.Offcanvas(
    id='databar',
    children=[
        dbc.Accordion(
            children=[
                dbc.AccordionItem(id='data-selector-source', title='Data Source'),
                dbc.AccordionItem(title='Frequency'),
                dbc.AccordionItem(title='Polarization')
            ],
            flush=True,
            start_collapsed=True,
            always_open=True
        ),
        dbc.Button('Submit', id='submit-button')
    ],
    title='Data Selector',
    scrollable=True,
    is_open=False,
    backdrop=False,
    placement='end',
    close_button=False,
    style=dict(
        display='flex',
        marginTop='50px',
        width='300px'
    )
)

# TODO still need to add all the components of the databar for selecting data
