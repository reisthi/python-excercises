"""Tests for function exercises"""
import unittest

from functions import (get_hypotenuse, to_celsius, is_leap_year,
                       is_perfect_square)


class GetHypotenuseTests(unittest.TestCase):

    """Tests for get_hypotenuse."""

    def test_3_and_4(self):
        self.assertEqual(get_hypotenuse(3, 4), 5.0)

    def test_5_and_12(self):
        self.assertEqual(get_hypotenuse(5, 12), 13.0)


class ToCelsiusTests(unittest.TestCase):

    """Tests for to_celsius."""

    def test_freezing(self):
        self.assertEqual(to_celsius(32), 0.0)

    def test_boiling(self):
        self.assertEqual(to_celsius(212), 100.0)


class IsLeapYearTests(unittest.TestCase):

    """Tests for is_leap_year."""

    def test_2000(self):
        self.assertEqual(is_leap_year(2000), True)

    def test_1996(self):
        self.assertEqual(is_leap_year(1996), True)

    def test_2016(self):
        self.assertEqual(is_leap_year(2016), True)

    def test_1600(self):
        self.assertEqual(is_leap_year(1600), True)

    def test_1900(self):
        self.assertEqual(is_leap_year(1900), False)


class IsPerfectSquareTests(unittest.TestCase):

    """Tests for is_perfect_square."""

    def test_small_number(self):
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(4))
        self.assertFalse(is_perfect_square(8))
        self.assertFalse(is_perfect_square(35))

    def test_4_digit_number(self):
        self.assertTrue(is_perfect_square(5776))
        self.assertFalse(is_perfect_square(9306))

    def test_big_number(self):
        self.assertTrue(is_perfect_square(1586375448590241))
        self.assertFalse(is_perfect_square(1420958445736851))

    @unittest.expectedFailure
    def test_really_big_number(self):
        square_number = 70288580036600145852851472194557260071791442118756
        self.assertTrue(is_perfect_square(square_number))
        self.assertFalse(is_perfect_square(square_number-1))
        self.assertFalse(is_perfect_square(square_number+1))


if __name__ == "__main__":
    unittest.main()
