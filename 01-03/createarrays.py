"""Creating NumPy arrays."""

import numpy as np


def test_run():
    # List of tuples to 2D array
    print(np.array([(2, 3, 4), (5, 6, 7)]))
    print(np.array([[2, 3, 4], [5, 6, 7]]))
    # Empty array
    print(np.empty(5))
    print(np.empty((5, 4)))
    print(np.ones((5, 4), dtype=np.int))
    print(np.zeros((5, 4)))
    # Generating random numbers
    print(np.random.random((5, 4)))
    print(np.random.rand(5, 4))
    print(np.random.randint(0, 10, size=(2, 3)))
    print(np.random.normal(loc=0, scale=0.1, size=10))
    # Array attributes
    a = np.random.random((5, 4))
    print(a.shape)  # dimensions (height, width, ...)
    print(a.ndim)  # = len(shape)
    print(a.size)  # total no. of elements
    print(a.dtype)  # datatype
    # Statistics: min, max, mean (across rows, cols, and overall)
    print(a.min(axis=0))  # minimum of each column
    print(a.max(axis=1))  # maximum of each row
    print(a.mean())  # leave out axis arg.
    # Modifying array elements
    b = np.random.rand(5, 4)
    print(b)
    b[:, 3] = [1, 2, 3, 4, 5]
    print(b)


if __name__ == "__main__":
    test_run()
