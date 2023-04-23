import csv
import pandas as pd
import tmdbsimple as tmdb

tmdb.API_KEY='d9f1fdf6bacf6783ff16e7d8a495dce8'
tmdb.REQUESTS_TIMEOUT=10

df=pd.read_csv('imdb_top_1000.csv')
list=df['Series_Title']
i=1
for i in range(1000):
    name=list[i]
    year=df.loc[list==name,'Released_Year'].values
    #print(year)
    search=tmdb.Search()
    response=search.movie(query=name)
    for s in search.results:
        title=s['title']
        year2=s['release_date'].split('-',1)[0]
        #print(year2)
        id=s['id']
        if (name==title):
            response=tmdb.Movies(id).info()
            budget=response['budget']
            with open('budgets.csv','a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow([title,int(budget)])
    i+=1
#movie=tmdb.Movies(603)
#response=movie.info()
#print(movie.budget)