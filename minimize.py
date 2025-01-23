# Create a Python program (Filename: minimize.py) to perform the following optimization problem.

import numpy as np

# print(np.arange(0, 1.01, 0.01))
# print(np.linspace(0, 1.0, 101))

def optimization(x):
    result = []
    for i in x:
        result.append(i**3 - 2 * np.sin(i) + 1)
    optimal_id = np.argmin(result)
    optimal_v = np.min(result)
    return x[optimal_id], optimal_v


x = np.linspace(0, 1, 5)
print(optimization(x))


