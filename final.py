import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error,mean_squared_error
import matplotlib.pyplot as plt

budgets=pd.read_csv("budgets.csv")
budgets.drop_duplicates(subset=None,inplace=True)
budgets.to_csv("budgetsClean.csv",index=False)

df=pd.read_csv("budgetsClean.csv")
df.head()