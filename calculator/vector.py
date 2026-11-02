

import numpy as np
A = [float(x) for x in input("Enter your vector A (comma-separated): ").split(",")]
B = [float(x) for x in input("Enter your vector B (comma-separated): ").split(",")]

metrix = np.array([A, B]) 

Magnitude = np.linalg.norm(A), np.linalg.norm(B)
print("Magnitude of vector A:", Magnitude[0])
print("Magnitude of vector B:", Magnitude[1])
