import numpy as np

# Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
X = np.random.rand(3, 1)
# change it to [-5, 10] as [0, 15] - 5
X = 15*X - 5
print(X)
print('--------------------------')
##############################################################################
softmax_X = np.exp(X) / np.sum(np.exp(X))
print(softmax_X)
print('--------------------------')
# compare softmax based normalization to the linear normalization
linear_normalized_X = (X - np.min(X)) / (np.max(X)-np.min(X))
print(linear_normalized_X)