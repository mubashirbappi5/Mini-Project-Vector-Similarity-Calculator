import unittest

from calculator.vector import cosine_similarity


class CosineSimilarityTests(unittest.TestCase):
    def test_identical_vectors_have_similarity_one(self):
        self.assertAlmostEqual(cosine_similarity([1, 2], [1, 2]), 1.0)

    def test_orthogonal_vectors_have_similarity_zero(self):
        self.assertAlmostEqual(cosine_similarity([1, 0], [0, 1]), 0.0)

    def test_opposite_vectors_have_similarity_negative_one(self):
        self.assertAlmostEqual(cosine_similarity([1, 2], [-1, -2]), -1.0)

    def test_zero_magnitude_vector_raises_value_error(self):
        with self.assertRaises(ValueError):
            cosine_similarity([0, 0], [1, 2])

    def test_different_vector_lengths_raise_value_error(self):
        with self.assertRaises(ValueError):
            cosine_similarity([1, 2], [1])


if __name__ == "__main__":
    unittest.main()
