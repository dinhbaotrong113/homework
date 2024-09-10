# exam 1
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:/Homework/Module3/Week1/2024.8.23/WeatherHistory2D.csv')
datetime = pd.to_datetime(df['Formatted Date'], utc = True)
df['year'] = datetime.dt.year
df['month'] = datetime.dt.month
df['day'] = datetime.dt.day
df['hour'] = datetime.dt.hour
df.drop(['Formatted Date'], axis = 1, inplace= True)
# print(df)
print(df[df['year']>2010])
print(df[df.year>2010])
# exam 3
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:/Homework/Module3/Week1/2024.8.23/creditcard.csv')

