import pandas as pd
import numpy as np

data = pd.read_csv('D:/Homework/Module2/Week1/temperature-1d.csv').to_numpy()

temp = data[:,1].reshape(-1,24)
sum_temp_one_day = temp.sum(axis=1)
average_one_day = sum_temp_one_day/24
mean = average_one_day.repeat(24)
print(average_one_day)

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'qt')
plt.plot(temp)
plt.plot()
plt.xlabel('index')
plt.ylabel('temp')
plt.show



import pandas as pd
import numpy as np
one_hot_code = np.array([1,1,2,1,3,3,2,1,4])
keep = []
while len(one_hot_code)>0:
    keep.append(one_hot_code[0])
    one_hot_code = np.delete(one_hot_code, np.where(one_hot_code == one_hot_code[0]))

re_place = np.identity(len(keep))
print(keep)
print(re_place)
one_hot_code = np.array([1,1,2,1,3,3,2,1,4])
for i in range(len(keep)):
    print(keep[i])
    one_hot_code[np.where(one_hot_code == keep[i])] = re_place[i]

print(one_hot_code)




import numpy as np
arr2 = np.repeat(1 ,10).reshape (2 , -1)
print(arr2)
    
import numpy as np
arr1 = np . arange (10) . reshape (2 , -1)
arr2 = np . repeat (1 ,10) . reshape (2 , -1)
c = np . concatenate ([ arr1 , arr2 ] , axis =1)
print ("C = ", c )

import numpy as np
arr = np . array ([1 ,2 ,3])
print ( np . repeat ( arr ,3) )
print ( np . tile ( arr ,3) )

import numpy as np

def maxx(x,y):
    if x>= y:
        return x
    else: 
        return y
    
a = np.array ([5 ,7 ,9 ,8 ,6 ,4 ,5])
b = np.array ([6 ,3 ,4 ,8 ,9 ,7 ,1])

vec_to = np.vectorize(maxx)
print(vec_to(a,b))

import numpy as np

a = np . array ([5 ,7 ,9 ,8 ,6 ,4 ,5])
b = np . array ([6 ,3 ,4 ,8 ,9 ,7 ,1])

print (" Result ", np . where (a <b , b , a ) )

