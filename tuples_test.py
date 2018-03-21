
"""Tests for tuple exercises"""
import unittest


from tuples import get_oldest, name_key, sort_names, swap_ends


class GetOldestTests(unittest.TestCase):

    """Tests for get_oldest."""

    def test_same_month_and_day(self):
        newer = "01/27/1832"
        older = "01/27/1756"
        self.assertEqual(get_oldest(newer, older), older)

    def test_february_29th(self):
        newer = "02/29/1972"
        older = "12/21/1946"
        self.assertEqual(get_oldest(newer, older), older)

    def test_smaller_month_bigger_day(self):
        newer = "03/21/1946"
        older = "02/24/1946"
        self.assertEqual(get_oldest(older, newer), older)

    def test_same_month_and_year(self):
        newer = "06/24/1958"
        older = "06/21/1958"
        self.assertEqual(get_oldest(older, newer), older)


class NameKeyTests(unittest.TestCase):

    """Tests for name_key."""

    def test_michael_gambino(self):
        michael = "Michael Gambino"
        self.assertEqual(name_key(michael), ('Gambino', 'Michael'))

    def test_suzanne_smith(self):
        suzanne = "Suzanne Smith"
        self.assertEqual(name_key(suzanne), ('Smith', 'Suzanne'))


class SortNamesTests(unittest.TestCase):

    """Tests for sort_names."""

    def test_sort_by_last_name(self):
        tanya = "Tanya Jackson"
        ben = "Ben Speigel"
        names = [ben, tanya]
        output = [tanya, ben]
        self.assertEqual(sort_names(names), output)
        self.assertEqual(sort_names(reversed(names)), output)

    def test_same_last_name(self):
        evelyn = "Evelyn Moore"
        jill = "Jill Moore"
        names = [evelyn, jill]
        output = [evelyn, jill]
        self.assertEqual(sort_names(names), output)
        self.assertEqual(sort_names(reversed(names)), output)

    def test_three_names(self):
        evelyn = "Evelyn Moore"
        jill = "Jill Moore"
        tanya = "Tanya Jackson"
        names = [evelyn, jill, tanya]
        output = [tanya, evelyn, jill]
        self.assertEqual(sort_names(names), output)

    def test_four_names(self):
        evelyn = "Evelyn Moore"
        jill = "Jill Moore"
        tanya = "Tanya Jackson"
        ben = "Ben Speigel"
        names = [jill, ben, tanya, evelyn]
        output = [tanya, evelyn, jill, ben]
        self.assertEqual(sort_names(names), output)

    def test_already_sorted(self):
        evelyn = "Evelyn Moore"
        jill = "Jill Moore"
        tanya = "Tanya Jackson"
        ben = "Ben Speigel"
        names = [tanya, evelyn, jill, ben]
        output = [tanya, evelyn, jill, ben]
        self.assertEqual(sort_names(names), output)


class SwapEndsTests(unittest.TestCase):

    """Tests for swap_ends."""

    def test_one_item(self):
        numbers = [1]
        swap_ends(numbers)
        self.assertEqual(numbers, [1])

    def test_two_items(self):
        numbers = [1, 2]
        swap_ends(numbers)
        self.assertEqual(numbers, [2, 1])

    def test_three_items(self):
        numbers = [1, 2, 3]
        swap_ends(numbers)
        self.assertEqual(numbers, [3, 2, 1])

    def test_four_items(self):
        numbers = [1, 2, 3, 4]
        swap_ends(numbers)
        self.assertEqual(numbers, [4, 2, 3, 1])

    def test_five_items(self):
        numbers = [1, 2, 3, 4, 5]
        swap_ends(numbers)
        self.assertEqual(numbers, [5, 2, 3, 4, 1])

    def test_return_value_is_None(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertIsNone(swap_ends(numbers))


if __name__ == "__main__":
    unittest.main()
