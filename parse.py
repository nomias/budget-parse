import csv
import pandas as pd
import numpy as np

imdb=pd.read_csv("imdb_top_1000.csv")
movies=pd.read_csv("movies_metadata.csv",low_memory=False)

imdbTitles=imdb['Series_Title']
movieTitles=movies['original_title']

for imdbTit in imdbTitles:
    for movieTit in movieTitles:
        if (imdbTit==movieTit):
            print("success")
            budget=movies.loc[movieTitles==movieTit,'budget'].values
            if budget.any():
                budget=int(budget[0])
            else:
                budget=int(budget)
            revenue=movies.loc[movieTitles==movieTit,'revenue'].values
            revenue=int(revenue[0])
            profit=revenue-budget
            diff=0
            if budget>0:
                diff=profit/budget
            else:
                diff=0
            target=0
            if diff>1.5:
                target=1
            with open('budgets.csv','a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow([movieTit,budget,revenue,profit,diff,target])
