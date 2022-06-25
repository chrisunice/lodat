from dash import html
import dash_bootstrap_components as dbc


navbar = dbc.Navbar(
    id='nav-bar',
    children=[
        html.I(
            id='menu-icon',
            className='fa-solid fa-bars fa-2xl',
            style=dict(color='white')
        ),
        html.Div(
            html.H5(
                'Low Observable Data Analysis Toolkit',
                style=dict(margin='0px')
            ),
            style=dict(width='100%', textAlign='center')
        ),
        html.I(
            id='filter-icon',
            className='fa-solid fa-filter fa-2xl',
            style={'color': 'white', 'display': 'none'}
        )
    ],
    style=dict(
        height='50px',
        padding='5px'
    )
)


