"""
Contains functions that load the dataframe from given CSV,
and performs preprocessing.
"""

import numpy as np
import pandas as pd
from Constants import *

# TODO split to train and test
# TODO split train usink kfolds (with k=10?)

def createDF():
    """
    Loads dataframe from CSV and performs preprocessing.
    :return:
    """
    original_data = pd.read_csv(DATA_PATH, index_col=0)
    preprocess(original_data)

def preprocess(df):
    """
    Preprecesses the given dataframe.
    :param df: Dataframe to alter.
    :return: Altered dataframe.
    """
    df = preprocessRows(df)
    df = preprocessCols(df)
    # print(df.columns)
    # print(df)


def preprocessRows(df):
    """
    Removes outliers rows.
    :param df: Dataframe to alter.
    :return: altered dataframe.
    """
    df.drop(df[df['SES_GROUP'] == "OTHER"].index, inplace=True)
    df.dropna(axis=ROWS, thresh=6, subset=BLOOD_TEST_COLS, inplace=True)
    print(df.isna().sum())
    return df


def preprocessCols(df):
    """
    Converts cols to desired format.
    :param df: Dataframe to alter.
    :return: Altered dataframe.
    """
    df.drop('AGE_GROUP', axis=COLS, inplace=True) # Remove AGE_GROUP col
    df = pd.get_dummies(df, columns=['MIGZAR']) # Convert MIGZAR to dummy variables
    df['SES_GROUP'].replace(to_replace=['LOW', 'MID', 'HI'],
                            value=[1, 2, 3], inplace=True) # Convert SES_GROUP to numeric
    return df

createDF()
