import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def insertionsort(x):
    """
    input: insertsion sort takes in a list or numpy array
    output: returns the list or array in sorted order

    notes: use insertion sort algorithm -- adapted from pseudocode in Cormen textbook
    """
    assign = 0
    cond = 0
    for j in range(1, len(x)):
        key = x[j]
        i = j-1
        while i >= 0 and x[i] > key:
            cond += 1
            x[i+1] = x[i]
            i = i-1
            assign += 1
        x[i+1] = key
        assign += 1
    return [x, cond, assign]

def bubblesort(x):
    """
    input: insertsion sort takes in a list or numpy array
    output: returns the list or array in sorted order

    notes: use bubble sort algorithm -- adapted from pseudocode in Cormen textbook
    """
    print('start bubble')
    assign = 0
    cond = 0
    for i in range(len(x)):
        for j in range(len(x)-1, i, -1):
            if x[j] < x[j-1]:
                cond += 1
                x[j], x[j-1] = x[j-1], x[j]
                assign += 1
    return [x, cond, assign]

def quicksort(x, start=0, end=None):
    """
    input: insertsion sort takes in a list or numpy array and the first and last index of the array
    output: returns the list or array in sorted order

    notes: use quicksort algorithm -- adapted from pseudocode in Cormen textbook
    """
    assign = 0
    cond = 0
    if end == None:
        cond += 1
        end = len(x)-1
    if start < end:
        cond += 1
        split, cond, assign  = partition(x, start, end, cond, assign)

        quicksort(x, start, split - 1)
        quicksort(x, split + 1, end)
    return [x, cond, assign]


def partition(A,p,r, cond, assign):
    '''
    input: an array and the first and last index of a region of the array
    output: a pivot index

    notes: partition algorithm adapted form pseudocode in Cormen textbook
    '''
    x = A[r]
    i = p-1
    j=p
    while j < r:
        if A[j] <= x:
            cond += 1
            i = i+1
            A[j], A[i] = A[i], A[j]
            assign += 1
        j += 1
    A[r] = A[i+1]
    A[i+1] = x
    assign += 1
    return i+1, cond, assign
