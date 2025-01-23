# What is the summation of all the odd numbers between 0 and 10,000? Please write your Python code to implement this task (Filename: sum.py).

mysum = 0

# method 1
# for i in range(10001):
#     if i%2 == 1:
#         print(i)
#         mysum = mysum + i


# # method 2
# for i in range(1, 10001, 2):
#     print(i)
#     mysum = mysum+i


## method 3
import numpy as np
mysum = np.sum(range(1, 10001, 2))


print(mysum)