# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:58:50 2020

@author: kgale
"""



import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output
import re
import datetime

app = dash.Dash(__name__)


html.Label('Choose a continent'),
dcc.Dropdown(id='selection',
        options=[
            {'label': 'Africa', 'value': 'Africa'},
            {'label': 'Antarctica', 'value': 'Antarctica'},
            {'label': 'Asia', 'value': 'Asia'},
            {'label': 'Europe', 'value': 'Europe'},
            {'label': 'North America', 'value': 'North America'},
            {'label': 'Oceania', 'value': 'Oceania'},
            {'label': 'South America', 'value': 'South America'}
        ],
        value='Africa'
)


@app.callback(
    Output('pop_graph', 'figure'),
    [Input('selection', 'value')])
def update_fig(selected_cont):
    df = px.data.gapminder().query("continent== selected_cont ")

    fig = px.line(df, x="year", y="lifeExp", color='country')


    return fig

    
if __name__ == '__main__':

    app.run_server(debug=False)