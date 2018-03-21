"""Tests for zip exercises"""
import unittest


from zip import parse_row, transpose, reverse_difference, sum_each


class ParseRowTests(unittest.TestCase):

    """Tests for parse_row."""

    def test_multiple_colors(self):
        inputs = "purple,indigo,red,blue,green\n0.15,0.25,0.3,0.05,0.25"
        outputs = {
            'blue': '0.05',
            'green': '0.25',
            'purple': '0.15',
            'red': '0.3',
            'indigo': '0.25',
        }
        self.assertEqual(parse_row(inputs), outputs)


class TransposeTests(unittest.TestCase):

    """Tests for transpose."""

    def test_empty(self):
        self.assertEqual(transpose([]), [])

    def test_single_item(self):
        self.assertEqual(transpose([[1]]), [[1]])

    def test_two_rows(self):
        self.assertEqual(transpose([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_three_rows(self):
        inputs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        outputs = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(transpose(inputs), outputs)


class ReverseDifferenceTests(unittest.TestCase):

    """Tests for reverse_difference."""

    def test_empty(self):
        self.assertEqual(reverse_difference([]), [])

    def test_one(self):
        self.assertEqual(reverse_difference([1]), [0])

    def test_two(self):
        self.assertEqual(reverse_difference([0, 0]), [0, 0])

    def test_three(self):
        self.assertEqual(reverse_difference([3, 2, 1]), [2, 0, -2])

    def test_four(self):
        self.assertEqual(reverse_difference([9, 8, 7, 6]), [3, 1, -1, -3])

    def test_five(self):
        inputs = [1, 2, 3, 4, 5]
        outputs = [-4, -2, 0, 2, 4]
        self.assertEqual(reverse_difference(inputs), outputs)


class SumEachTests(unittest.TestCase):

    """tests for sum_each."""

    def test_list_of_two_two_item_tuples(self):
        self.assertEqual(sum_each([(1, 2), (4, 5)]), (5, 7))

    def test_list_of_three_two_item_tuples(self):
        self.assertEqual(sum_each([(1, 2), (4, 5), (7, 8), (1, 1)]), (13, 16))

    def test_list_of_4_3_item_tuples(self):
        inputs = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 1, 0)]
        outputs = (13, 16, 18)
        self.assertEqual(sum_each(inputs), outputs)


if __name__ == "__main__":
    unittest.main()
