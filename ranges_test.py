"""Tests for range exercises"""
import unittest

from ranges import (get_factors, power_list, is_prime, identity, is_range,
                    triples)


class GetFactorsTests(unittest.TestCase):

    """Tests for get_factors."""

    def test_2(self):
        self.assertEqual(get_factors(2), [1, 2])

    def test_6(self):
        self.assertEqual(get_factors(6), [1, 2, 3, 6])

    def test_100(self):
        self.assertEqual(get_factors(100), [1, 2, 4, 5, 10, 20, 25, 50, 100])

    @unittest.expectedFailure
    def test_negatives(self):
        message = "Only positive numbers are supported"
        with self.assertRaisesRegexp(ValueError, message):
            get_factors(-1)
        with self.assertRaisesRegexp(ValueError, message):
            get_factors(-1000)

    @unittest.expectedFailure
    def test_non_integers(self):
        with self.assertRaises(TypeError):
            get_factors(6.0)
        with self.assertRaises(TypeError):
            get_factors(6.5)


class PrimalityTests(unittest.TestCase):

    """Tests for is_prime."""

    def test_21(self):
        self.assertFalse(is_prime(21))

    def test_23(self):
        self.assertTrue(is_prime(23))


class PowerListTests(unittest.TestCase):

    """Tests for power_list."""

    def test_integers(self):
        self.assertEqual(power_list([3, 2, 5]), [1, 2, 25])

    def test_floats(self):
        inputs = [78, 700, 82, 16, 2, 3, 9.5]
        outputs = [1, 700, 6724, 4096, 16, 243, 735091.890625]
        self.assertEqual(power_list(inputs), outputs)


class IdentityTests(unittest.TestCase):

    """Tests for identity."""

    def test_2_by_2_matrix(self):
        expected = [[1, 0], [0, 1]]
        self.assertEqual(identity(2), expected)

    def test_3_by_3_matrix(self):
        expected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(identity(3), expected)

    def test_4_by_4_matrix(self):
        expected = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        self.assertEqual(identity(4), expected)


class IsRangeTests(unittest.TestCase):

    """Tests for is_range."""

    def test_range_starting_at_zero(self):
        self.assertTrue(is_range([0, 1, 2, 3]))

    def test_nonrange_starting_at_zero(self):
        self.assertFalse(is_range([0, 2, 1, 3]))

    def test_range_starting_at_nonzero(self):
        self.assertTrue(is_range([5, 6, 7, 8]))

    def test_nonrange_starting_at_nonzero(self):
        self.assertFalse(is_range([5, 6, 8]))


class TriplesTests(unittest.TestCase):

    """Tests for triples."""

    def test_triples_1(self):
        expected = []
        self.assertEqual(triples(1), expected)

    def test_triples_6(self):
        expected = [(3, 4, 5)]
        self.assertEqual(triples(6), expected)

    def test_triples_25(self):
        expected = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17),
                    (9, 12, 15), (12, 16, 20)]
        self.assertEqual(triples(25), expected)


if __name__ == "__main__":
    unittest.main()
