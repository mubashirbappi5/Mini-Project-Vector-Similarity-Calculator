import numpy as np
from calculator.vector import cosine_similarity

A = [float(x) for x in input("Enter your vector A (comma-separated): ").split(",")]
B = [float(x) for x in input("Enter your vector B (comma-separated): ").split(",")]

similarity = cosine_similarity(A, B)
print("Dot Product:", np.dot(A, B))
print("Magnitude of vector A:", np.linalg.norm(A))
print("Magnitude of vector B:", np.linalg.norm(B))
print("Cosine Similarity:", similarity)
