import numpy as np
A = [float(x) for x in input("Enter your vector A (comma-separated): ").split(",")]
B = [float(x) for x in input("Enter your vector B (comma-separated): ").split(",")]

metrix = np.array([A, B]) 

dotproduct = np.dot(A, B)
print("Dot Product:", dotproduct)
