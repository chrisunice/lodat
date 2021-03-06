"""
Author:         Chris Unice
Description:    This script is to define all the layouts (pages) that will
                be used by the application.
"""
# --- Imports ---
import dash_core_components as dcc
import dash_html_components as html


# --- Functions (layouts) ---
def left_column():
    container = html.Div(
        className='left-column',
        children=[
            # CAPITAL SECTION #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Capital']
                    ),
                    dcc.Input(
                        id='capital',
                        className='input',
                        type='text',
                    )
                ]
            ),
            html.Hr(),
            # LOAN APR SECTION #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Loan APR']
                    ),
                    html.Div(
                        className='input-container',
                        children=[
                            dcc.Input(
                                id='loan-apr',
                                className='percent',
                                type='number',
                                min=0, max=100, step=0.025,
                            ),
                            html.Label(
                                className='percent-symbol',
                                children=['%']
                            )
                        ]
                    )
                ]
            ),
            html.Hr(),
            # HOME OWNERS ASSOCIATION SECTION #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['HOA']
                    ),
                    dcc.Input(
                        id='hoa-input',
                        className='input',
                        type='text',
                    )
                ]
            ),
            html.Hr(),
            # REAL ESTATE TAX RATE SECTION #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['RE Tax Rate']
                    ),
                    html.Div(
                        className='input-container',
                        children=[
                            dcc.Input(
                                id='property-tax-rate',
                                className='percent',
                                type='number',
                                min=0, max=100, step=0.01,
                            ),
                            html.Label(
                                className='percent-symbol',
                                children=['%']
                            )
                        ]
                    )
                ]
            ),
            html.Hr(),
            # CAPITAL EXPENDITURE #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Cap Ex Rate']
                    ),
                    html.Div(
                        className='input-container',
                        children=[
                            dcc.Input(
                                id='cap-ex-rate',
                                className='percent',
                                type='number',
                                min=0, max=100, step=0.1,
                            ),
                            html.Label(
                                className='percent-symbol',
                                children=['%']
                            )
                        ]
                    )
                ]
            ),
            html.Hr(),
            # VACANCY RATE #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Vacancy Rate'],
                    ),
                    html.Div(
                        className='input-container',
                        children=[
                            dcc.Input(
                                id='vacancy-rate',
                                className='percent',
                                type='number',
                                min=0, max=100, step=0.1,
                            ),
                            html.Label(
                                className='percent-symbol',
                                children=['%']
                            )
                        ]
                    )
                ]
            ),
            html.Hr(),
            # PROPERTY MANAGEMENT RATE #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Property Mgt Rate']
                    ),
                    html.Div(
                        className='input-container',
                        children=[
                            dcc.Input(
                                id='property-mgt-rate',
                                className='percent',
                                type='number',
                                min=0, max=100, step=0.1,
                            ),
                            html.Label(
                                className='percent-symbol',
                                children=['%']
                            )
                        ]
                    )
                ]
            ),
            html.Hr(),
            # DESIRED PROFIT MARGIN #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Desired Profit'],
                    ),
                    html.Div(
                        className='input-container',
                        children=[
                            dcc.Input(
                                id='desired-profit',
                                type='number',
                                min=0, step=1,
                            ),
                            dcc.RadioItems(
                                id='desired-profit-radio-items',
                                options=[{'label': x, 'value': x} for x in ['$', '%']],
                                value='$'
                            )
                        ]
                    )
                ],
            )
        ]
    )
    return container


def right_column():
    container = html.Div(
        className='right-column',
        children=[
            # PURCHASE PRICE #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Purchase Price:'],
                    ),
                    html.Label(
                        id='purchase-price',
                        className='output',
                        children=['_'*10]
                    )
                ]
            ),
            # DOWN PAYMENT #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Down Payment:'],
                    ),
                    html.Label(
                        id='down-payment',
                        className='output',
                        children=['_'*10]
                    )
                ]
            ),
            # PRINCIPLE AND INTEREST #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Principle & Interest:'],
                    ),
                    html.Label(
                        id='principle-interest',
                        className='output',
                        children=['_'*10]
                    )
                ]
            ),
            # HOME OWNERS ASSOCIATION #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['HOA:'],
                    ),
                    html.Label(
                        id='hoa-output',
                        className='output',
                        children=['_' * 10]
                    )
                ]
            ),
            # HOME INSURANCE #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Home Insurance:'],
                    ),
                    html.Label(
                        id='home-insurance',
                        className='output',
                        children=['_'*10]
                    )
                ]
            ),
            # PROPERTY TAX #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Property Tax:'],
                    ),
                    html.Label(
                        id='property-tax',
                        className='output',
                        children=['_'*10]
                    )
                ]
            ),
            # MORTGAGE #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Mortgage:'],
                    ),
                    html.Label(
                        id='mortgage',
                        className='output',
                        children=['_'*10]
                    )
                ]
            ),
            # CAPITAL EXPENDITURES #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Capital Expenditure:'],
                    ),
                    html.Label(
                        id='cap-ex',
                        className='output',
                        children=['_'*10]
                    )
                ]
            ),
            # VACANCY #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Vacancy:'],
                    ),
                    html.Label(
                        id='vacancy',
                        className='output',
                        children=['_'*10]
                    )
                ]
            ),
            # PROPERTY MANAGEMENT #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Property Management:'],
                    ),
                    html.Label(
                        id='property-mgt',
                        className='output',
                        children=['_'*10]
                    )
                ]
            ),
            # PROFIT MARGIN #
            html.Div(
                className='row',
                children=[
                    html.Label(
                        className='label',
                        children=['Profit Margin:'],
                    ),
                    html.Label(
                        id='profit-margin',
                        className='output',
                        children=['_'*10]
                    )
                ]
            )
        ],
    )
    return container


def main_layout():
    layout = html.Div(
        children=[
            html.Div(
                id='calculator',
                children=[
                    # APP TITLE #
                    html.Div(
                        className='title',
                        children=[
                            html.Label(
                                className='title-text',
                                children=['Investment Calculator']
                            )
                        ]
                    ),
                    # COLUMNS #
                    html.Div(
                        className='two-columns',
                        children=[
                            # LEFT - INPUTS #
                            left_column(),
                            # RIGHT - OUTPUTS #
                            right_column()
                        ]
                    ),
                    # Buttons & Output #
                    html.Div(
                        className='footer',
                        children=[
                            html.Button(
                                id='calculate-button',
                                className='button',
                                children=['Calculate']
                            ),
                            html.Button(
                                id='reset-button',
                                className='button',
                                children=['Reset']
                            ),
                            html.Label(
                                id='required-rent-label',
                                children=['Required Rent']
                            ),
                            html.Label(
                                id='required-rent-amount',
                                children=['_'*10]
                            )
                        ]
                    )

                ]
            )
        ]
    )
    return layout
# end file
