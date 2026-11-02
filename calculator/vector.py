from collections.abc import Sequence

import numpy as np


def cosine_similarity(vector_a: Sequence[float], vector_b: Sequence[float]) -> float:
    """Return the cosine similarity of two one-dimensional vectors."""
    array_a = np.asarray(vector_a, dtype=float)
    array_b = np.asarray(vector_b, dtype=float)

    if array_a.ndim != 1 or array_b.ndim != 1:
        raise ValueError("Vectors must be one-dimensional.")
    if array_a.shape != array_b.shape:
        raise ValueError("Vectors must have the same number of elements.")

    dot_product = np.dot(array_a, array_b)
    magnitude_a = np.linalg.norm(array_a)
    magnitude_b = np.linalg.norm(array_b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cosine similarity is undefined for a zero-magnitude vector.")

    return float(dot_product / (magnitude_a * magnitude_b))
