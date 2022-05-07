
# import dash
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv('cleaned_data.csv')
columns=list(df.columns)
county_names = df['county'].unique()

    # # needed only if running this as part of a multipage app
from app import app

colors = {
    #background to rgb(233, 238, 245)
    # 'background': '#bfbfbf',
    # 'text': '#1c1cbd'
}
color_discrete_map = {'Cavan': '#636EFA', 'Armagh': '#EF553B', 'Down': '#00CC96',
    'Dublin': '#AB63FA', 'Kerry': '#FFA15A'}



layout = html.Div(children=[
    html.H1('Gealic Match Analysis',
        style={
            'textAlign': 'center',
            'color': '#fffff',
            }
            ),
            html.Div([
            dbc.Col(children=[
            html.Label('Select Counties'),
            dcc.Dropdown(id='county_drop',
                        options=[{'label': i, 'value': i}
                                for i in county_names],
                        value=['Cavan', 'Armagh', 'Down', 'Dublin', 'Kerry'],
                        multi=True
            )
            ], className='pl-2 pb-4')
        ],style={'width': '49%', 'display': 'inline-block'}),
        html.Div([
        dbc.Col(children=[
        html.Label('Select Build Up Pass Range'),
        dcc.RangeSlider(id='pass_range',
            min=0,
            max=29,
            value=[0,29],
            step= 1,
            marks={
                0: '0',
                10: '10',
                20: '20',
                30: '30',
            },
        )
        ],className='pb-2')
],style={'width': '49%', 'float': 'right', 'display': 'inline-block', 'background':'#fffff',}),
        dcc.Graph(id="distance_graph"),
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

    ]),
    ],className="pt-4")

])


@app.callback(
    Output(component_id='distance_graph', component_property='figure'),
    [Input(component_id='county_drop', component_property='value')]
)
# def update_graph(selected_county) :
#     filtered_county = df[df['county'] == selected_county]
#     line_fig = px.line(filtered_county,
#     X='game', y='build_up_passes',
#     color='type',
#     title=f'Player Status in {selected_county}')
#     return line_fig

def update_line_chart(county_names):
    mask = df.county.isin(county_names)
    fig = px.line(df[mask], 
        x="build_up_passes", y="distance_from_goal", color='county')
    return fig

