#https://csatlas.com/python-import-file-module/
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
import os, sys
import subprocess

os.chdir("/mount/src/asnifen/")
sys.path.append("/mount/src/asnifen/modules"
sys.path.append("/mount/src/asnifen/modules/program"     
                
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

def show_pdf(file_path):
    st.title('✨ Визуализация PDF документа 📜')
    st.markdown("")
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000" height="700" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def execute_python_file1(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            python_code = file.read()
            exec(python_code)
    except FileNotFoundError:
        st.markdown(f"Error: The file '{file_path}' does not exist.")


def execute_python_file(file_path):
    try:
        completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
        if completed_process.returncode == 0:
            st.markdown("Execution successful.")
            st.markdown("Output:")
            st.markdown(completed_process.stdout)
        else:
            st.markdown(f"Error: Failed to execute '{file_path}'.")
            st.markdown("Error output:")
            st.markdown(completed_process.stderr)
    except FileNotFoundError:
        st.markdown(f"Error: The file '{file_path}' does not exist.")

#st.write(sys.path)
#file_path = '/mount/src/asnifen/modules/programs/Reports.py' 
#file_path = '/mount/src/asnifen/assets/Einleitung.pdf' 
#file_path = '/mount/src/asnifen/modules/programs/Einleitung.pdf' 
#st.write(file_path)
#show_pdf(file_path)
#execute_python_file1(file_path)

m.select_file() 
