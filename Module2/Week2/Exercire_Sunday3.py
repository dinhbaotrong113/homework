# cosine Similarity
import numpy as np

a = np.array([1,2,3,4])
b = np.array([1, 0, 3, 0])

def cosine(a,b):
    cosine = (a.dot(b))/(np.linalg.norm(a)*np.linalg.norm(b))
    return cosine
print(cosine(a,b))
# similarity
from scipy import spatial

def similarity(a,b):
    return 1- spatial.distance.cosine(a,b)
print(similarity(a,b))