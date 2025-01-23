import numpy as np

# Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
v1 = np.random.rand(1000,1)
v2 = np.random.rand(1000,1)
########################################################################
## Method1: for loop
l1 = []
l2 = []
for i in range(v1.size):
    l1.append(np.abs(v1[i]-v2[i]))
    l2.append((v1[i] - v2[i])**2)

l1_distance = np.sum(l1)
l2_distance = np.sqrt(np.sum(l2))

print(l1_distance)
print(l2_distance)
########################################################################
## Method2: numpy array broadcasting
l1_distance = 0
l2_distance = 0
l1_distance = np.sum(np.abs(v1-v2))
l2_distance = np.sqrt(np.sum((v1-v2)**2))
print(l1_distance)
print(l2_distance)
