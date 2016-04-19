"""How fast is NumPy?"""

import numpy as np
from time import time


def how_long(func, *args):
    """
    Execute function with given arguments, and measure execution time.
    Parameters
    ----------
    func : function
    """
    t0 = time()
    result = func(*args)
    t1 = time()
    return result, t1 - t0


def manual_mean(arr):
    """
    Compute mean (average) of all elements in the given 2D array.

    Parameters
    ----------
    arr : ndarray

    Returns
    -------
    float
        the mean of all the elements in the array
    """
    the_sum = 0
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            the_sum += arr[i, j]
    return the_sum / arr.size


def numpy_mean(arr):
    """
    Compute mean (average) using NumPy.
    Parameters
    ----------
    arr : ndarray
    """
    return arr.mean()


def test_run():
    nd1 = np.random.random((1000, 10000))
    # Time the two functions, retrieving results and execution times
    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)
    print("Manual: {:.6f} ({:.3f} secs.) vs. NumPy: {:.6f} ({:.3f} secs.)"
          .format(res_manual, t_manual, res_manual, t_numpy))
    # Make sure both give us the same answer
    assert abs(res_manual - res_numpy) <= 10e-6, "Results aren't equal!"
    # Compute speedup
    speedup = t_manual / t_numpy
    print("NumPy is", speedup, "times faster than manual for loops.")


if __name__ == "__main__":
    test_run()
