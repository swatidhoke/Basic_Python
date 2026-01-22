"""
NumPy Tutorial for Beginners
This script explains NumPy step by step for someone completely new to it.
Each section includes detailed explanations and examples.
"""

import numpy as np

# ------------------------------
# 1. Introduction to NumPy
# ------------------------------
# NumPy is a powerful Python library for numerical computations.
# It provides N-dimensional arrays, mathematical functions, and linear algebra tools.
# Using NumPy arrays is faster and more memory-efficient than regular Python lists.

# ------------------------------
# 2. Array Creation
# ------------------------------
# Arrays are the core of NumPy. Think of them as lists (1D) or matrices (2D).

# 1D array (single row of elements)
arr1 = np.array([1, 2, 3, 4])
print("1D array (single row):", arr1)

# 2D array (rows and columns)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array (matrix with rows and columns):\n", arr2)

# Array of zeros (input: shape = (rows, columns))
zeros = np.zeros((2,3))
print("2x3 array of zeros:\n", zeros)

# Array of ones
ones = np.ones((3,2))
print("3x2 array of ones:\n", ones)

# Array with a range of numbers (start, stop, step)
arange = np.arange(0,10,2)  # 0 to 9, step 2
print("Array using arange (0 to 10, step 2):", arange)

# Array with evenly spaced numbers (start, stop, number of elements)
linspace = np.linspace(0,1,5)  # 5 numbers from 0 to 1 inclusive
print("Array using linspace (5 numbers from 0 to 1):", linspace)

# Random array (numbers between 0 and 1), input: shape (rows, columns)
random_arr = np.random.rand(2,3)
print("2x3 array of random numbers between 0 and 1:\n", random_arr)

# ------------------------------
# 3. Array Operations
# ------------------------------
# Arrays support element-wise operations. Both arrays must have same shape.
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])

print("\nArray Operations")
print("Addition:", arr_a + arr_b)
print("Subtraction:", arr_a - arr_b)
print("Multiplication:", arr_a * arr_b)
print("Division:", arr_a / arr_b)
print(np.multiply(arr_a, arr_b))  # Using NumPy multiply function
# ------------------------------
# 4. Indexing & Slicing
# ------------------------------
arr = np.arange(10)  # 1D array 0-9
print("\nIndexing & Slicing")
print("Original 1D array:", arr)
print("Index 3 (4th element):", arr[3])
print("Slice 2-7:", arr[2:8])  # elements from index 2 to 7

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])  # 3x3 2D array
print("2D array:\n", arr2d)
print("Element at row 2, column 3:", arr2d[1,2])
print("Slice first 2 rows and last 2 columns:\n", arr2d[:2,1:])

# ------------------------------
# 5. Mathematical Functions
# ------------------------------
# Functions apply element-wise to arrays
arr = np.array([1,4,9,16])
print("\nMathematical Functions")
print("Square root:", np.sqrt(arr))
print("Exponential (e^x):", np.exp(arr))
print("Natural logarithm:", np.log(arr))
print("Sine values:", np.sin(arr))

# ------------------------------
# 6. Statistical Functions
# ------------------------------
arr = np.array([1,2,3,4,5])
print("\nStatistical Functions")
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Sum of elements:", np.sum(arr))
print("Minimum:", np.min(arr), "Maximum:", np.max(arr))

# ------------------------------
# 7. Linear Algebra
# ------------------------------
mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[5,6],[7,8]])
print("\nLinear Algebra")
print("Matrix multiplication:\n", np.dot(mat1, mat2))
print("Transpose:\n", mat1.T)
print("Determinant:", np.linalg.det(mat1))
print("Inverse:\n", np.linalg.inv(mat1))

# ------------------------------
# 8. Random Numbers
# ------------------------------
print("\nRandom Numbers")
print("Uniform 0-1 (3 numbers):", np.random.rand(3))
print("Normal distribution (3 numbers):", np.random.randn(3))
print("Random integers 1-9 (size 5):", np.random.randint(1,10,5))
print("Random integers 1-9 (size 3x3):", np.random.randint(1,10,(3, 3)))

# ------------------------------
# 9. Reshaping & Stacking
# ------------------------------
arr = np.arange(6)
print("\nOriginal 1D array:", arr)
reshaped = arr.reshape((2,3))  # Change 1D to 2x3 2D array
print("Reshaped to 2x3:\n", reshaped)
hstack = np.hstack((reshaped, reshaped))  # Combine arrays horizontally
vstack = np.vstack((reshaped, reshaped))  # Combine arrays vertically
print("Horizontal Stack:\n", hstack)
print("Vertical Stack:\n", vstack)

# ------------------------------
# End of Tutorial
# ------------------------------
# This beginner-friendly script covers basic to intermediate NumPy functions with explanations for shapes, inputs, and usage.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result_cross = np.cross(arr1, arr2)
print(result_cross )

arr = np.arange(1, 10).reshape(3, 3)
result_trace = np.trace(arr)
print(result_trace)

A = np.array([[1, 2], [3, 4]])
B = A.T

A = np.array([10, 20, 30, 40])
mask = (A >= 20) & (A <= 30)
B = A[mask]
print(B) 