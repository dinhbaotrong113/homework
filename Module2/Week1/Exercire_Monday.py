import numpy as np

a = np.zeros((3,7))
b = np.ones((3,9))
c = np.random.rand(3,4,5)
d = np.full((3,5), 6)
e = np.full_like(c, 6)
f = np.random.randint(a.shape)
g = np.concatenate(e,f)
print(g)
print(a)
print(b)
print(c)
print(e)
print(f)

import numpy as np
x = np.random.randint(4,9, size = (4,7))
print(x)
deleted_index = np.where(x == 5)
count = (x == 5)
print(count)
print(deleted_index)


data1 = [1,2,3]
data2 = [4,5,6]

for v1, v2 in zip(data1, data2):
    print(v1,v2)

## enumerate
import numpy as np
data1 = np.array([1,2,3])
data2 = np.array([4,5,6])
zip_arr = np.dstack((data1, data2))[0]
for i in range(len(data1)):
    print(zip_arr[i])
print(zip_arr)

for v1, v2 in zip_arr[0]:
    print(v1,v2)

for index, value in np.ndenumerate(data1):
    print(index, value)


import numpy as np
a = np.array([1,2,3,4])
print(a[[1,3]])
print(a[a>3])

### array manipulation
import numpy as np
arr1 = np.array([[1,2],[3,4],[5,6]])
arr2 = np.array([1,2])
print(arr1+arr2)


print(arr1.reshape(1,6))

arr2 = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print(arr2.flatten())

print(np.concatenate((arr1.reshape(1,6).flatten(),arr2.flatten())))