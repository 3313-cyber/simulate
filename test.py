import numpy as np

A=np.array([[1, 2], [3, 4]])
poles=np.linalg.eigvals(A)
print(poles)