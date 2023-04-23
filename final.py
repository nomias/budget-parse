import csv
import pandas as pd
import numpy as np

imdb=pd.read_csv("imdb_top_1000.csv")
budgets=pd.read_csv("budgets.csv")

imdbTitles=imdb['Series_Title']
budgetTitles=budgets['Title']
for imdbTit in imdbTitles:
    for budgetTit in budgetTitles:
        if imdbTit==budgetTit:
            imdb.loc[imdbTitles==budgetTit,"Budget"].values=budgets.loc[budgetTitles==budgetTit,"Budget"].values