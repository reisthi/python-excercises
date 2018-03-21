"""Tests for dictionary exercises"""
import unittest


from dictionaries import (flip_dict, translate, get_all_factors, count_words,
                          is_anagram, get_ascii_codes, dict_from_truple,
                          dict_from_tuple)


class FlipDictTests(unittest.TestCase):

    """Tests for flip_dict."""

    def test_no_collisions(self):
        inputs = {
            'Python': "2015-09-15",
            'Java': "2015-09-14",
            'C': "2015-09-13",
        }
        outputs = {
            '2015-09-13': 'C',
            '2015-09-15': 'Python',
            '2015-09-14': 'Java',
        }
        self.assertEqual(flip_dict(inputs), outputs)

    @unittest.expectedFailure
    def test_with_collisions(self):
        inputs = {
            'Python': "2015-09-15",
            'Java': "2015-09-14",
            'C': "2015-09-13",
            'JavaScript': "2015-09-13",
        }
        with self.assertRaises(ValueError):
            flip_dict(inputs)


class GetAllFactorsTests(unittest.TestCase):

    """Tests for get_all_factors."""

    def test_small_numbers(self):
        inputs = {1, 2, 3, 4}
        outputs = {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4]}
        self.assertEqual(get_all_factors(inputs), outputs)

    def test_larger_numbers(self):
        inputs = {62, 293, 314}
        outputs = {62: [1, 2, 31, 62], 293: [1, 293], 314: [1, 2, 157, 314]}
        self.assertEqual(get_all_factors(inputs), outputs)


class TranslateTests(unittest.TestCase):

    """Tests for translate."""

    def test_cat(self):
        self.assertEqual(translate("gato"), "cat")

    def test_the_cat(self):
        self.assertEqual(translate("el gato"), "the cat")

    def test_cat_in_house(self):
        inputs = "el gato esta en la casa"
        outputs = "the cat is in the house"
        self.assertEqual(translate(inputs), outputs)


class CountWordsTests(unittest.TestCase):

    """Tests for count_words."""

    def test_simple_sentence(self):
        actual = count_words("oh what a day what a lovely day")
        expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
        self.assertEqual(actual, expected)

    def test_apostrophe(self):
        actual = count_words("don't stop believing")
        expected = {"don't": 1, 'stop': 1, 'believing': 1}
        self.assertEqual(actual, expected)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_capitalization(self):
        actual = count_words("Oh what a day what a lovely day")
        expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
        self.assertEqual(actual, expected)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_symbols(self):
        actual = count_words("Oh what a day, what a lovely day!")
        expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
        self.assertEqual(actual, expected)


class IsAnagramTests(unittest.TestCase):

    """Tests for is_anagram."""

    def test_short_anagram(self):
        self.assertTrue(is_anagram("tea", "eat"))

    def test_different_lengths(self):
        self.assertFalse(is_anagram("tea", "treat"))

    def test_sink_and_skin(self):
        self.assertTrue(is_anagram("sink", "skin"))

    def test_same_letters_different_lengths(self):
        self.assertFalse(is_anagram("sinks", "skin"))

    def test_different_capitalization(self):
        self.assertTrue(is_anagram("Trey", "Yert"))
        self.assertTrue(is_anagram("Listen", "silent"))


class GetASCIICodeTests(unittest.TestCase):

    """Tests for get_ascii_codes."""

    def test_multiple_words(self):
        words = ["hello", "bye", "yes", "no", "python"]
        outputs = {
            'yes': [121, 101, 115],
            'hello': [104, 101, 108, 108, 111],
            'python': [112, 121, 116, 104, 111, 110],
            'no': [110, 111],
            'bye': [98, 121, 101],
        }
        self.assertEqual(get_ascii_codes(words), outputs)


class DictFromTrupleTests(unittest.TestCase):

    """Tests for dict_from_truple."""

    def test_three_tuples(self):
        inputs = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        outputs = {1: (2, 3), 4: (5, 6), 7: (8, 9)}
        self.assertEqual(dict_from_truple(inputs), outputs)


class DictFromTupleTests(unittest.TestCase):

    """Tests for dict_from_tuple."""

    def test_four_items(self):
        inputs = [(1, 2, 3, 4), (5, 6, 7, 8)]
        outputs = {1: (2, 3, 4), 5: (6, 7, 8)}
        self.assertEqual(dict_from_tuple(inputs), outputs)

    def test_three_items(self):
        inputs = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        outputs = {1: (2, 3), 4: (5, 6), 7: (8, 9)}
        self.assertEqual(dict_from_tuple(inputs), outputs)


if __name__ == "__main__":
    unittest.main()
