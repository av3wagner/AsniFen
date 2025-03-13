import streamlit as st  
import streamlit.components.v1 as components
stop=18
from datetime import datetime
import time
timestart = datetime.now()
stt = time.time()
now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics
import matplotlib.pyplot as plt
import math
import random
import seaborn as sns
#import scikit-plot
import scipy
import warnings

warnings.filterwarnings('ignore')
sns.set()

# preprocessing
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_curve, roc_auc_score, accuracy_score, log_loss 
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import metrics
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold, learning_curve, ShuffleSplit
from sklearn.model_selection import cross_val_predict as cvp
from sklearn.calibration import CalibratedClassifierCV

# models
from sklearn.linear_model import LogisticRegression, LogisticRegression, Perceptron, RidgeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC, LinearSVC, SVR, NuSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb
from xgboost import XGBClassifier
import lightgbm as lgb
from lightgbm import LGBMClassifier

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# ensemble
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier 
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier, VotingClassifier

from sklearn.metrics import roc_auc_score
#from scikitplot.metrics import plot_roc_curve
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from sklearn.metrics import RocCurveDisplay, roc_curve
from sklearn.metrics import PrecisionRecallDisplay, precision_recall_curve
from sklearn import metrics
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, classification_report,f1_score,confusion_matrix,precision_score,recall_score,balanced_accuracy_score

import os, sys, inspect, time, datetime
import subprocess
import json
from time import time, strftime, localtime
from datetime import timedelta
import shutil
#from docx import Document
today = datetime.date.today()
year = today.year

os.chdir("/mount/src/asnifen/")
sys.path.append("/mount/src/asnifen/")
sys.path.append("/mount/src/asnifen/assets")
sys.path.append("/mount/src/asnifen/modules")
sys.path.append("/mount/src/asnifen/modules/programs")

#cwd = "modules" #os.getcwd()
#st.write(sys.path)

ImportBib="/mount/src/asnifen/modules/ImportBib.py"
import time
exec(open(ImportBib).read(), globals())
time.sleep(2.0)

#ConfigINI2025=os.path.join(cwd, "ConfigINI2025.py")
#exec(open(ConfigINI2025).read(), globals())
#import time
#time.sleep(2.0)

#AsniDef=os.path.join(cwd, "AsniDef.py")
#AsNiDef="/mount/src/asnifen/modules/programs/AsniDef.py"
#exec(open("/mount/src/asnifen/modules/programs/AsniDef.py").read(), globals())
#import time
#time.sleep(2.0)

#AsNiDefFa2=os.path.join(cwd, "AsNiDefFa2.py")
#AsNiDefFa2="/mount/src/asnifen/modules/AsNiDefFa2.py"
#exec(open(AsNiDefFa2).read(), globals())
#import time
#time.sleep(2.0)

matrix ="/mount/src/asnifen/data/heart.csv"
#data = pd.read_csv('/mount/src/asnifen/data/heart.csv')
df = pd.read_csv(matrix) 

df.rename({'Y': 'target'}, axis=1, inplace=True)
df = df.fillna(0)

st.markdown("")
col1, col2, col3 = st.columns( [40, 1, 1])
with col1:  
    st.markdown(f'<h2 style="color:yellow;font-size:24px;text-align:left">{"Набор данных для анализа"}</h2>', unsafe_allow_html=True)
    st.markdown("")

st.dataframe(df)  

train, test = train_test_split(df, test_size = 0.4)

X_train = train[train.columns.difference(['target'])]
y_train = train['target']

X_test = test[test.columns.difference(['target'])]
y_test = test['target']

cv_n_split = 2
random_state = 0
test_train_split_part = 0.2

train0, test0 = X_train, X_test
target0 = y_train
train, test, target, target_test = train_test_split(train0, target0, test_size=test_train_split_part, random_state=random_state)

st.markdown("")
col1, col2, col3 = st.columns( [1, 40, 1])
with col2:  
    st.markdown(f'<h2 style="color:yellow;font-size:24px;text-align:center">{"Базовая статистическа о данных"}</h2>', unsafe_allow_html=True)
st.markdown("")

st.write(test.describe())  
