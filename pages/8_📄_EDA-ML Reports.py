#https://www.geeksforgeeks.org/how-to-import-local-modules-with-python/
#EDA-Reports=os.path.join(cwd, "modules/programs/EDA-Reports.py")
#https://csatlas.com/python-import-file-module/

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

os.chdir("/mount/src/asnifen/")
sys.path.append("/mount/src/asnifen/modules")
sys.path.append("/mount/src/asnifen/modules/program")                
import modules.ReadPath as m

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

st.write(sys.path)
#m.show_pdf("./Einleitung.pdf")                
m.select_file() 
