import streamlit as st  
import streamlit.components.v1 as components
from  PIL import Image
import numpy as np
import pandas as pd
import base64
import sys
import inspect, os
import pathlib
from os import listdir
from os.path import isfile, join
import glob
import gunicorn

os.chdir("/mount/src/asnifen/")
sys.path.append("/mount/src/asnifen/")

st.set_page_config(
    page_title="Asfendijarov Kazakh National Medical University «АСНИ-МЕД»",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.write('test')
