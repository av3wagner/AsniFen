import pandas as pd
from datetime import datetime
import pandas as pd
#import numpy as np
#import sqlite3
import dash
from dash import dash_table
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import Dash, dcc, html, Input, Output, State, callback
import plotly.express as px
import plotly.graph_objects as go
#import chart_studio.plotly as py 
from jupyter_dash import JupyterDash
import flask
#import json
#import requests
#from urllib.request import urlopen
#from prophet import Prophet
#from pandas_datareader import data, wb
#import base64

raw_df = pd.read_csv('data/heart.csv')
DesktopWidth="1707px"
DesktopHeight="960px"
image_path = 'assets/WagnerFoto.jpg'
Front_path = 'assets/Front.jpg'

Front_image = html.Img(src='assets/Front.jpg', style={"height":"200", "width":"150", 'padding-left':10,})
image = html.Img(src='assets/WagnerFoto.jpg', style={"height":"200", "width":"150", 'padding-left': 220,})
def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')

app = JupyterDash(external_stylesheets=[dbc.themes.SLATE])
server=app.server
#print(raw_df.head(10))
app.title = "Kazakhstan Dashboard"
app.layout = html.Div([
  dcc.Tabs(id="tabs-with-classes", 
              value='Table11', 
              parent_className='custom-tabs', 
              className='custom-tabs-container',
        children=[
            dcc.Tab(
                label="Титул-лист системы",
                value="Table11",
                style=tab_style,
                selected_style=tab_selected_style,
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
  ],
         style=tabs_styles,
         colors={"border": "yellow", "primary": "red",
                 "background": "#111111",},
     ),html.Div(id='tabs-content-classes')
    
   ],style={"background": "#111111", 'marginLeft':5,'marginRight':20}
  )          
@app.callback(Output('tabs-content-classes', 'children'),
              Input('tabs-with-classes', 'value'))
def render_content(value): 
    tab=value
    if tab == 'Table11':
        return html.Div([
               html.Img(src=b64_image('Image/Front4.jpg'),
                        style={
                        "display": "inline-block",
                        "width": "99.75%",
                        #"height": "610px",    
                        "margin-left": "3px",
                        "margin-right": "0px", 
                        'marginTop':0,   
                        'marginBottom':0, 'padding': '1px 1px 1px 2px',    
                        "verticalAlign": "top"
               })
        ])

if __name__ == '__main__':
    app.run(debug=False)
