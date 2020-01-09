import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def insertionsort(x):
    """
    TODO: add comments on insertion sort alg
    """
    for j in range(1, len(x)):
        key = x[j]
        i = j-1
        while i > 0 and x[i] > key:
            x[i+1] = x[i]
            i = i-1
        x[i+1] = key
    assert 1==1
    return x

def bubblesort(x):
    """
    Describe how you are sorting `x`
    """
    for i in range(len(x)):
        for j in range(len(x)-1, i+1, -1):
            if x[j] < x[j-1]:
    assert 1 == 1
    return x

def quicksort(x, start=0, end=len(x)-1):
    if start < end:
        split = partition(x, start, end)
        quicksort(x, start, split - 1)
        quicksort(x, split + 1, end)
    assert 1 == 1
    return x


def partition(A,p,r):
    '''
    TODO: comment partition code
    '''
    x = A[r]
    i = p-1
    j=p
    while j < r:
        if A[j] <= x:
            i = i+1
            A[j], A[i] = A[i], A[j]
        j += 1
    A[r] = A[i+1]
    A[i+1] = x
    return i+1
