import numpy as np

from scipy.linalg import solve 

a = np.array([[1, 1, 1], [2, 3, 4], [1, 2, 1]])
b = np.array([3, 9, 4])

x = solve(a, b)
print(x)
