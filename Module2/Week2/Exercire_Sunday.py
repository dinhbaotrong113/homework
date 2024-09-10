# norm product
import numpy as np

def  compute_vector_length(vector):
    norm = np.sqrt(np.sum([v**2 for v in vector]))
    return norm

input_vector = np.array([-2,4,9,21])
print(compute_vector_length(input_vector))

# dot product
import numpy as np
def compute_dot_product(vector1, vector2):
    result = vector1.dot(vector2)
    return result

v1 = np.array([[-1,2],[3,-4]])
v2 = np.array([1,2])
print(compute_dot_product(v1,v2))

print(v1@v2)

# Multiply matrix with a vector
import numpy as np
v1 = np.array([[1,2],[3,4]])
v1 = np.reshape(v1, (-1,4), "F")[0]
v2 = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]])

def compute_multiply_matrix(vector1, vector2):
    result = vector1@vector2
    return result
print(compute_multiply_matrix(v1,v2))

print(v1@v2)

# inverse matrix
import numpy as np
v1 = np.array([[-2,6], [8,-4]])
iverse = np.linalg.inv(v1)
print(iverse)
