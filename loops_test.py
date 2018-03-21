"""Tests for loop exercises"""
import unittest

from loops import get_vowel_names, product, flatten, words_containing


class GetVowelNamesTests(unittest.TestCase):

    """Tests for get_vowel_names."""

    def test_one_vowel_name(self):
        names = ["Alice", "Bob", "Christy", "Jules"]
        self.assertEqual(get_vowel_names(names), ["Alice"])

    def test_multiple_vowel_names(self):
        names = ["Scott", "arthur", "Jan", "Elizabeth"]
        self.assertEqual(get_vowel_names(names), ["arthur", "Elizabeth"])

    def test_empty(self):
        self.assertEqual(get_vowel_names([]), [])


class ProductTests(unittest.TestCase):

    """Tests for product."""

    def test_one_number(self):
        self.assertEqual(product([10]), 10)

    def test_three_numbers(self):
        self.assertEqual(product([5, 6, 8]), 240)

    def test_empty_list(self):
        self.assertEqual(product([]), 1)


class FlattenTests(unittest.TestCase):

    """Tests for flatten."""

    def test_3_by_4_matrix(self):
        matrix = [[row * 3 + incr for incr in range(1, 4)] for row in range(4)]
        flattened = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(flatten(matrix), flattened)


class WordsContainingTests(unittest.TestCase):

    """Tests for words_containing."""

    def test_last_letter(self):
        words = ['My', 'life', 'is', 'my', 'message']
        matching = ['My', 'my']
        self.assertEqual(words_containing(words, 'y'), matching)

    def test_different_positions(self):
        words = ['My', 'life', 'is', 'my', 'message']
        matching = ['life', 'is']
        self.assertEqual(words_containing(words, 'i'), matching)

    def test_case_insensitive(self):
        words = ['My', 'life', 'is', 'my', 'message']
        matching = ['My', 'my', 'message']
        self.assertEqual(words_containing(words, 'm'), matching)


if __name__ == "__main__":
    unittest.main()
