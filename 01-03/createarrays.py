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
    print(np.random.normal(loc=0, scale=0.1, size=10))


if __name__ == "__main__":
    test_run()
