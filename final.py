import csv
import pandas as pd
import numpy as np
#from sklearn.linear_model import LinearRegression,Ridge,Lasso

bud=pd.read_csv('budgetse.csv')
imdb=pd.read_csv('imdb_top_1000 copy.csv')

#print(imdb)
budList=bud['Title']
imdbList=imdb['Series_Title']
bud.info()
imdb.info()
bud.drop_duplicates()
bud.to_csv("test.csv",index=False)
#imdb.drop(imdb.tail(500).index,inplace=True)
#budgets=pd.DataFrame({'Budget':np.array(bud['Budget'].values)})
#print(budgets)
#imdbList.update(budgets.any())
#imdb['Budget']=bud['Budget'].values
#i=1
#for n in imdbList:
    #for m in budList:
        #print(i)
        #i+=1
        #if (n==m):
            #print(n,m)
            #row=imdb[imdb['Series_Title'] == m].index
            #print(row)
            #budget=bud.loc[budList==n,'Budget'].values
            #imdb.at[row,'Budget']=budget


#lr=LinearRegression