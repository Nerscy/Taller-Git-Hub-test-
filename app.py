import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas
import numpy
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
st.set_option('deprecation.showPyplotGlobalUse', False)
'''
Cargamos los datos
'''
train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')

'''
Hacemos Featuring Engineering
'''
train_df['Age'].fillna(train_df['Age'].mean(), inplace=True)
test_df['Age'].fillna(test_df['Age'].mean(), inplace=True)
train_df['Embarked'].fillna(train_df['Embarked'].mode()[0], inplace=True)
test_df['Embarked'].fillna(test_df['Embarked'].mode()[0], inplace=True)
