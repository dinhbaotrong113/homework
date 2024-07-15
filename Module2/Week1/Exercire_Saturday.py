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
keep = np.array([])
print(one_hot_code[0])
print(len(one_hot_code))
while len(one_hot_code)>0:
    np.append(keep, [one_hot_code[0]])
    print(keep)
    one_hot_code = np.delete(one_hot_code, np.where(one_hot_code == one_hot_code[0]))
print(keep)

    

