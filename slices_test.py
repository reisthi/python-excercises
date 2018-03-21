"""Tests for slice exercises"""
import unittest


from slices import last_n_elements, last_words, split_in_half


class LastNElementsTests(unittest.TestCase):

    """Tests for last_n_elements."""

    def test_fruits(self):
        inputs = ['apple', 'orange', 'banana', 'strawberry', 'kiwi']
        outputs = ['banana', 'strawberry', 'kiwi']
        self.assertEqual(last_n_elements(inputs, 3), outputs)

    def test_last_one(self):
        inputs = ['apple', 'orange', 'banana', 'strawberry', 'kiwi']
        outputs = ['kiwi']
        self.assertEqual(last_n_elements(inputs, 1), outputs)

    def test_empty_list(self):
        self.assertEqual(last_n_elements([], 3), [])

    @unittest.expectedFailure
    def test_last_zero_elements(self):
        inputs = ['apple', 'orange', 'banana', 'strawberry', 'kiwi']
        self.assertEqual(last_n_elements(inputs, 0), [])


class LastWordsTests(unittest.TestCase):

    """Tests for last_words."""

    def test_last_two(self):
        sentence = "Oh what a day, what a lovely day!"
        words = "lovely day!"
        self.assertEqual(last_words(sentence, 2), words)

    def test_last_four(self):
        sentence = "Oh what a day, what a lovely day!"
        words = "what a lovely day!"
        self.assertEqual(last_words(sentence, 4), words)

    def test_empty_string(self):
        self.assertEqual(last_words("", 2), "")

    @unittest.expectedFailure
    def test_last_zero_words(self):
        sentence = "Oh what a day, what a lovely day!"
        self.assertEqual(last_words(sentence, 0), "")


class HalfTests(unittest.TestCase):

    """Tests for split_in_half."""

    def test_even(self):
        self.assertEqual(split_in_half([1, 2, 3, 4]), ([1, 2], [3, 4]))

    def test_odd(self):
        self.assertEqual(split_in_half([1, 2, 3, 4, 5]), ([1, 2], [3, 4, 5]))

    def test_two(self):
        self.assertEqual(split_in_half([1, 2]), ([1], [2]))

    def test_empty(self):
        self.assertEqual(split_in_half([]), ([], []))

    def test_one(self):
        self.assertEqual(split_in_half([1]), ([], [1]))

    def test_string(self):
        self.assertEqual(split_in_half("Hello world!"), ('Hello ', 'world!'))

    def test_tuple(self):
        self.assertEqual(split_in_half((1, 2)), ((1,), (2,)))


if __name__ == "__main__":
    unittest.main()
