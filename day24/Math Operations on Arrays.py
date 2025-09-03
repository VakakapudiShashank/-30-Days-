# Day 24 — NumPy Array Operations
# pip install numpy

import numpy as np

def demo_numpy():
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([10, 20, 30, 40, 50])

    print("a:", a)
    print("b:", b)
    print("\nElement-wise addition:", a + b)
    print("Element-wise multiplication:", a * b)
    print("Mean of a:", a.mean())
    print("Standard deviation of b:", b.std())

    m = np.arange(1, 10).reshape(3, 3)
    print("\nMatrix m:\n", m)
    print("Transpose of m:\n", m.T)
    print("Dot product a·b:", np.dot(a, b[:5]))

    # Slicing
    print("\nSlicing a[1:4]:", a[1:4])

if __name__ == "__main__":
    demo_numpy()
