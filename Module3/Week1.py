# import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read data
data = pd.read_csv('D:/Homework/Module3/IMDB-Movie-Data.csv')
data_index = pd.read_csv('D:/Homework/Module3/IMDB-Movie-Data.csv', index_col= 'Title')

# view the data

print(data.head())

#Understand the basic information about data
data.info()
data.describe()

# data selection - indexing and slicing data
# Extract data as series
genre = data['Genre']
print(genre)
# Extract data as dataframe
data[['Genre']]

some_cols = data[['Title','Genre','Actors','Director','Rating']]

data.iloc[10:15][['Title','Rating','Revenue (Millions)']]

# Data Selection - Basded on Conditional filtering
print(data[((data['Year']>=2010)&(data['Year']<=2015))
&(data['Rating']<6.0)
&(data['Revenue (Millions)']>data['Revenue (Millions)'].quantile(0.95))])

# Groupby Operations

print(data.groupby('Director')[['Rating']].mean().head())

# Sorting Operations

print(data.groupby('Director')[['Rating']].mean().sort_values('Rating', ascending= False)[:6])

# View mising values
print(data.isna().sum())

# Deal with mising values - Deleting
data.drop('Metascore', axis = 1, inplace = True)

# dealing with missing values - Filling

revenue_mean = data_index['Revenue (Millions)'].mean()
print('The mean revenue is: ', revenue_mean)
print(data_index['Revenue (Millions)'].fillna(revenue_mean))

# apply() functions

def rating_group(rating):
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'

data['Rating_category'] = data['Rating'].apply(rating_group)
print(data[['Title','Rating_category']])