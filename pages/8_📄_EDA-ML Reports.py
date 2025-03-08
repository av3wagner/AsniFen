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
#m.select_file()  
#"/mount/src/asnifen/modules/ReadPath.py"
#cwd = os.getcwd()
#Reports=os.path.join(cwd, "modules/programs/Reports.py")
#print(EDA-Reports)
#exec(open("/mount/src/asnifen/modules/programs/EDA-Reports.py").read(), globals())
#exec(open(Reports).read(), globals())
#EDA-Reports=os.path.join(cwd, "modules/programs/EDA-Reports.py")
#print(EDA-Reports)
#exec(open(EDA-Reports).read(), globals())
#cwd = os.getcwd()
#Report=os.path.join(cwd, "modules\programs\Reports.py")
#exec(open(Report, "r", encoding="utf-8").read(), globals())

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
