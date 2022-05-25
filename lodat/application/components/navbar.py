from dash import html
import dash_bootstrap_components as dbc


navbar = dbc.Navbar(
    children=[
        html.I(
            id='menu-icon',
            className='fa-solid fa-bars fa-2xl',
            style=dict(
                color='white'
            )
        ),
        html.Div(
            html.H5(
                'Low Observable Data Analysis Toolkit',
                style=dict(margin='0px')
            ),
            style=dict(width='100%', textAlign='center')
        )
    ],
    style=dict(
        display='flex',
        height='50px',
        padding='5px'
    )
)
