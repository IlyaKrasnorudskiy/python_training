import numpy as np

ITERATION_LIMIT = 1000

A = np.array([[9., 2., 3.],
              [2., 10., 5.],
              [3., 5., 11.],])
b = np.array([10., -3., 13.])

print("System:")
for i in range(A.shape[0]):
    row = [f"{A[i, j]}*x{j + 1}" for j in range(A.shape[1])]
    print(f'{" + ".join(row)} = {b[i]}')
print()

x = np.zeros_like(b)
for it_count in range(ITERATION_LIMIT):
    if it_count != 0:
        print(f"Iteration {it_count}: {x}")
    x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if x_new[i] == x_new[i-1]:
          break

    if np.allclose(x, x_new, atol=1e-10, rtol=0.):
        break

    x = x_new

print("Solution: ")
print(x)
error = np.dot(A, x) - b
print("Error:")
print(error)