import pandas as pd
from datetime import datetime
import pandas as pd
import numpy as np
import sqlite3
import dash
from dash import dash_table
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import Dash, dcc, html, Input, Output, State, callback
import plotly.express as px
import plotly.graph_objects as go
import chart_studio.plotly as py 
from jupyter_dash import JupyterDash
import flask
import json
import requests
from urllib.request import urlopen
from prophet import Prophet
from pandas_datareader import data, wb
import base64

raw_df = pd.read_csv('data/heart.csv')
app = JupyterDash(external_stylesheets=[dbc.themes.SLATE])
server=app.server
print(raw_df.head(10))

if __name__ == '__main__':
    app.run(debug=False)
