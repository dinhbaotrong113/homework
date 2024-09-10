#eigenvalue and eigenvector
import numpy as np
def compute_eigenvalues_eigenvector(matrix):
    eigenvalues, eigenvector = np.linalg.eig(matrix)
    return eigenvalues, eigenvector

input_matrix = np.array([[0.9,0.2],[0.1,0.8]])
print(compute_eigenvalues_eigenvector(input_matrix))

