import pandas as pd
import numpy as np

a = np.array([[1,2],[3,4]])

#determinant
print(np.linalg.det(a))

b = np.linalg.inv(a)
print(b)
print(b.dot(a))
print(a.dot(b))

# cosine Similarity
import numpy as np

a = np.array([1,2,3])
b = np.array([4, 5, 6])

print(np.linalg.norm(a, ord = -np.inf))
print(np.linalg.norm(a))
def cosine(a,b):
    cosine = (a.dot(b))/(np.linalg.norm(a)*np.linalg.norm(b))
    return cosine

## image Similarity
import numpy as np
from PIL import Image

image1 = Image.open('D:/Homework/Module2/Week2/data/image1.jpg')
image2 = Image.open('D:/Homework/Module2/Week2/data/image2.jpg')
query_image = Image.open('D:/Homework/Module2/Week2/data/query_image.jpg')

image1_data = np.array(image1)
image2_data = np.array(image2)
query_image_data = np.array(query_image)

image1_data = np.sum(image1_data, axis = -1, keepdims= 1)/3
image2_data = np.sum(image2_data, axis = -1, keepdims= 1)/3
query_image_data = np.sum(query_image_data, axis = -1, keepdims= 1)/3

image1_data = image1_data.flatten()
image2_data = image2_data.flatten()
query_image_data = query_image_data.flatten()

cosine_image1_query = cosine(image1_data, query_image_data)
cosine_image2_query = cosine(image2_data, query_image_data)

print(cosine_image1_query)
print(cosine_image2_query)