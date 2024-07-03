
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import xgboost as xgb



df = pd.read_excel ("E:\Project - Credit Risk Modelling\EPS_Dataset.xlsx")
df = df. drop( ['Bank name', 'Year'] , axis=1)

