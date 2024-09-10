# Create a Series

import pandas as pd
import numpy as np
data = pd.Series(['C+', 'Golang', 'Java', 'Python', 'Swift'],
                 index = list('cgjps'),
                 name = 'Programing Language')
print(data['c'])

# Drop a row

k = data.drop(['c', 'g'])
print(k.iloc[::])

# insert a row

data['k'] = 'Kotlin'
print(data)

# Sort index

data.sort_index(inplace= True)
print(data)

data.reset_index(inplace=True, drop= True)
print(data)
 #common Pandas funtion

import pandas as pd
data = pd.Series([1,5,2,7], name = 'numbers')

print(data.iloc[::2])
print(data.min())
print(data.max())
print(data.sum())
print(data.std())
print(data.var())
print(data.mean())
print(data.idxmax())
print(data.argmax())

import pandas as pd
import numpy as np
data = pd.Series(['C+', 'Golang', 'Java', 'Python', 'Swift'],
                 index = list('cgjps'),
                 name = 'Programing Language')

print(data.str.count('a'))
print(data.str.count('a').groupby(level=('j')))
# mising value

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('D:/Homework/Module3/Week1/2024.8.21/weatherHistory_v1.csv')

data_s = data.iloc[:200].interpolate()
data_s.plot.kde(0.2)
plt.show()
plt.title('Boxplot với Matplotlib')
plt.xlabel('Nhóm')
plt.ylabel('Giá trị')


