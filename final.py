import csv
import pandas as pd
import numpy as np

imdb=pd.read_csv("imdb_top_1000.csv")
budgets=pd.read_csv("budgets2.csv")

imdbTitles=imdb['Series_Title']
budgetTitles=budgets['Title']

budgets.drop_duplicates(subset=None,inplace=True)
budgets.to_csv("budgets3.csv",index=False)