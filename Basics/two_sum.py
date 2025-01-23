# Given a list A and a value X, create a Python program (Filename: two_sum.py) to test whether there are two elements in A whose summation is X.


def two_sum(A, X):
    flag = False
    for i in range(len(A)-1):         # 0, 1, ..., n-2
        for j in range(i+1, len(A)):  # i+1, i+2, ..., n-1
            if A[i]+A[j] == X:
                flag = True
                break
    if flag:
        print("yes, it is")
    else:
        print("no, it is not")


two_sum([1,2,3,4,5,6,7], 228)