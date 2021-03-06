import numpy as np
from scripts import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    # empty vector
    e = np.empty(2,dtype=float)
    assert np.array_equal(algs.bubblesort(e)[0], e)

    # single element
    s = np.array([1])
    assert np.array_equal(algs.bubblesort(s)[0], s)

    # dup elements, even length
    d = np.array([1,3,2,1,5,1])
    assert np.array_equal(algs.bubblesort(d)[0], np.array([1,1,1,2,3,5]))

    # odd length
    o = np.array([3,2,4])
    assert np.array_equal(algs.bubblesort(o)[0], np.array([2,3,4]))

    #char
    c = ['a','b','a','c']
    assert algs.bubblesort(c)[0] == ['a','a','b','c']


def test_quicksort():

    # empty vector
    e = np.empty(2,dtype=float)
    assert np.array_equal(algs.quicksort(e)[0], e)

    # single element
    s = np.array([1])
    assert np.array_equal(algs.quicksort(s)[0], s)

    # dup elements, even length
    d = np.array([1,3,2,1,5,1])
    assert np.array_equal(algs.quicksort(d)[0], np.array([1,1,1,2,3,5]))

    # odd length
    o = np.array([3,2,4])
    assert np.array_equal(algs.quicksort(o)[0], np.array([2,3,4]))

    #char
    c = ['a','b','a','c']
    assert algs.quicksort(c)[0] == ['a','a','b','c']



def test_insertionsort():

    # empty vector
    e = np.empty(2,dtype=float)
    assert np.array_equal(algs.insertionsort(e)[0], e)

    # single element
    s = np.array([1])
    assert np.array_equal(algs.insertionsort(s)[0], s)

    # dup elements, even length
    d = np.array([1,3,2,1,5,1])
    assert np.array_equal(algs.insertionsort(d)[0], np.array([1,1,1,2,3,5]))

    # odd length
    o = np.array([3,2,4])
    assert np.array_equal(algs.insertionsort(o)[0], np.array([2,3,4]))

    #char
    c = ['a','b','a','c']
    assert algs.insertionsort(c)[0] == ['a','a','b','c']
