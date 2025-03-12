from matplotlib import *
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets, linear_model, metrics
from sklearn import preprocessing
from sklearn.compose import make_column_transformer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingRegressor, ExtraTreesRegressor, AdaBoostClassifier
from sklearn.feature_selection import SelectKBest, SelectPercentile, f_classif, f_regression, mutual_info_regression
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from xgboost import XGBRegressor, XGBClassifier
from xgboost import plot_importance
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.stats as stats
import seaborn as sns
import sys
import warnings
import time
import os, sys, inspect, time, datetime
import subprocess
import json
from time import time, strftime, localtime
from datetime import timedelta
import shutil
from configparser import ConfigParser
import configparser
from time import time, strftime, localtime
from datetime import timedelta
import pandas as pd
import pathlib

from docx import Document
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.io as pio
import plotly.offline
import plotly.offline as po
import plotly as pl
import plotly as pplt
import patchworklib as pw
import dash
import cufflinks as cf
import colorama
from termcolor import colored
from plotly import tools
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.offline import iplot
from plotly.subplots import make_subplots
from IPython.core.display import HTML
from collections import Counter
from colorama import Fore, Style 
