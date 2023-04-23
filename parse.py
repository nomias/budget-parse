import csv
import pandas as pd
import numpy as np

imdb=pd.read_csv("imdb_top_1000.csv")
movies=pd.read_csv("movies_metadata.csv",low_memory=False)

imdbTitles=imdb['Series_Title']
movieTitles=movies['original_title']

for imdbTit in imdbTitles:
    #print(imdbTit)
    imdbYearArr=imdb.loc[imdbTitles==imdbTit,'Released_Year'].values
    imdbYear=imdbYearArr[0]
    #print(imdbTit,imdbYear)
    for movieTit in movieTitles:
        #numpy.ndarray
        movieYear=0
        movieYearArr=movies.loc[movieTitles==imdbTit,'release_date'].values
        if isinstance(movieYearArr,(np.ndarray)):
            movieYear=int(movieYearArr[0].split('-',1)[0])
        else:
            movieYear=movieYearArr
        print(movieTit,imdbTit,movieYear)
        #movieYear=int(movieYearArr[0].split('-',1)[0])
        #print(movieTit,movieYear)
        if (imdbTit==movieTit) & (imdbYear==movieYear):
            print("success")
            budget=movies.loc[movieTitles==movieTit,'budget'].values
            with open('budgets.csv','a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow([movieTit,budget])
        break