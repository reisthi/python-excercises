"""Tests for list exercises"""
import unittest


from lists import combine_lists, rotate_list, reverse_words, ith_item_power


class CombineListsTests(unittest.TestCase):

    """Tests for combine_lists."""

    def test_two_lists(self):
        first = [1, 2, 3]
        second = [4, 5, 6]
        third = [1, 2, 3, 4, 5, 6]
        self.assertEqual(combine_lists(first, second), third)

    def test_lists_unchanged(self):
        first = [1, 2, 3]
        second = [4, 5, 6]
        combine_lists(first, second)
        self.assertEqual(first, [1, 2, 3])
        self.assertEqual(second, [4, 5, 6])

    def test_one_empty_list(self):
        self.assertEqual(combine_lists([1, 2], []), [1, 2])


class RotateListTests(unittest.TestCase):

    """Tests for rotate_list."""

    def test_four_items(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(rotate_list(numbers), 1)
        self.assertEqual(numbers, [2, 3, 4, 1])

    def test_two_items(self):
        numbers = ['a', 'b']
        self.assertEqual(rotate_list(numbers), 'a')
        self.assertEqual(numbers, ['b', 'a'])

    def test_one_item(self):
        numbers = [0]
        self.assertEqual(rotate_list(numbers), 0)
        self.assertEqual(numbers, [0])

    # Comment the following line for testing the Reverse Rotate exercise
    @unittest.expectedFailure
    def test_reverse_rotate(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(rotate_list(numbers, reverse=True), 4)
        self.assertEqual(numbers, [4, 1, 2, 3])

    # Comment the following line for testing the Reverse Rotate exercise
    @unittest.expectedFailure
    def test_not_reverse(self):
        numbers = [4, 1, 2, 3]
        self.assertEqual(rotate_list(numbers, reverse=False), 4)
        self.assertEqual(numbers, [1, 2, 3, 4])


class ReverseWordOrder(unittest.TestCase):

    """Tests for reverse_words."""

    def test_three_words(self):
        self.assertEqual(reverse_words("who is this"), "this is who")

    def test_four_words(self):
        input_sentence = "words some are these"
        output_sentence = "these are some words"
        self.assertEqual(reverse_words(input_sentence), output_sentence)

    def test_one_word(self):
        self.assertEqual(reverse_words("hello"), "hello")

    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")


class IthItemsPowerTests(unittest.TestCase):

    """Tests for ith_item_power."""

    def test_square(self):
        self.assertEqual(ith_item_power([3, 2, 5], 2), 25)

    def test_fourth_power(self):
        self.assertEqual(ith_item_power([5, 6, 2, 7, 3], 4), 81)

    def test_zeroth_power(self):
        self.assertEqual(ith_item_power([3, 2, 5], 0), 1)

    def test_negative_powers(self):
        self.assertEqual(ith_item_power([3, 2, 5], -1), 0.2)


if __name__ == "__main__":
    unittest.main()
