from dash import html
import dash_bootstrap_components as dbc
from app import app



layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H2("Privacy Policy", className="text-center")
                    , className="mb-2 mt-2 text-center",style={'justifyContent': 'center'})            
        ]),
        dbc.Row([
            dbc.Col(html.H5("The data I have used in this project is completely confidential add no one is allowed to use any of the content published in this website dot space in case somebody received the data which is provided by did Katie dot they will have all the ethical responsibilities dot no one is allowed to use any information provided in the website without taking any consent from dickaty management dot in case of any data misuse or breach here's what the particular person who is responsible for the misuse of data dot the data is completely confidential and it is collected from that particular source there dignity has to keep or consider all the ethical considerations for publishing this data online as part of the project we will make sure there is no data bridge dot please make sure to take consent before getting any source of information from the website this website is created only four akademik purposes add there is no that about pleasure or that security threat made by the project if you have any queries regarding this project please contact d00242726@student.dkit.ie for any support or queries regarding this work", className="text-center")
                    , className="mb-5 mt-5 text-center",style={'justifyContent': 'center'})            
        ]),
                 dbc.Row([
            # 2 columns of width 6 with a border
            dbc.Col(children=[
                    dbc.Col(html.H5(children='Copyright © 2022, Dundalk Institute of Technology. All Rights Reserved',
                    className="text-center pt-2 pb-2"),
                                        
            ),
            dbc.Col(children=[
                    dbc.Col(
                    html.H5(children='Mob : +353 89 273 817',
                    className="text-center pb-2"),
                                  
                )

            ]),
            dbc.Col(children=[
                    dbc.Col(
                    html.H5(children='Email : d00242726@student.dkit.ie',
                    className="text-center pb-2"),
                                  
                )

            ])

    ])
    ])
        
    ])
])