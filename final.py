import csv
import pandas as pd

df=pd.read_csv('budgets.csv')
df.head()
df.isnull().any()