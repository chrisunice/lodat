import dash_bootstrap_components as dbc

databar = dbc.Offcanvas(
    id='databar',
    children=[dbc.Button('Submit')],
    title='Data Selector',
    scrollable=True,
    is_open=False,
    backdrop=False,
    placement='end',
    close_button=False,
    style=dict(
        display='flex',
        marginTop='50px',
        width='200px'
    )
)

# TODO still need to add all the components of the databar for selecting data
