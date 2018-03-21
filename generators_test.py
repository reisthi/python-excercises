"""Test for generator exercises"""
import unittest

from generators import (all_together, total_length, first_prime_over,
                        get_primes_over)


class AllTogetherTests(unittest.TestCase):

    """Tests for all_together."""

    def test_list_and_tuple(self):
        outputs = list(all_together([1, 2], (3, 4)))
        expected = [1, 2, 3, 4]
        self.assertEqual(outputs, expected)

    def test_with_strings(self):
        outputs = list(all_together([1, 2], (3, 4), "hello"))
        expected = [1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o']
        self.assertEqual(outputs, expected)

    def test_empty_list(self):
        outputs = list(all_together([], (), '', [1, 2]))
        self.assertEqual(outputs, [1, 2])

    def test_iterator(self):
        outputs = all_together([1], [2])
        self.assertEqual(list(outputs), [1, 2])
        self.assertEqual(list(outputs), [])


class TotalLengthTests(unittest.TestCase):

    """Tests for total_length."""

    def test_list(self):
        self.assertEqual(total_length([1, 2, 3]), 3)

    def test_nothing(self):
        self.assertEqual(total_length(), 0)

    def test_iterators(self):
        squares = (n**2 for n in [1, 2, 3])
        self.assertEqual(total_length([1, 2, 3], [4, 5], squares), 8)


class FirstPrimeOverTests(unittest.TestCase):

    """Tests for first_prime_over."""

    def test_first_prime_over_one_million(self):
        self.assertEqual(first_prime_over(1000000), 1000003)

    def test_first_prime_over_three_million(self):
        self.assertEqual(first_prime_over(3000000), 3000017)


class GetPrimesOverTests(unittest.TestCase):

    """Tests for get_primes_over."""

    def test_10_primes_over_one_million(self):
        ten_primes = [1000003, 1000033, 1000037, 1000039, 1000081,
                      1000099, 1000117, 1000121, 1000133, 1000151]
        self.assertSequenceEqual(get_primes_over(1000000, 10), ten_primes)

    def test_first_prime_over_one_million(self):
        self.assertSequenceEqual(get_primes_over(1000000, 1), [1000003])


if __name__ == "__main__":
    unittest.main()
