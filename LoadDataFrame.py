import numpy as np
import pandas as pd

def createDF():
    original_data = pd.read_csv("Data/diab_ckd_data.csv", index_col=0)
    preprocess(original_data)

def preprocess(data):
    print(data.head())

createDF()