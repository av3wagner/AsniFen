import streamlit as st  
import streamlit.components.v1 as components
import time
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
import os
import subprocess
#import modules.ReadPath as m

st.set_page_config(
    page_title="EDA/ML Reports",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

Report="/mount/src/asnifen/modules/programs/EDA-Reports.py"
with open("/mount/src/asnifen/modules/programs/EDA-Reports.py", 'r', encoding='utf-8') as file:
    python_code = file.read()

#st.code(python_code, "python") 
exec(python_code)
#exec(python_code, globals())
