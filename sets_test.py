"""Tests for set exercises"""
import unittest


from sets import get_most_common


class GetMostCommonTests(unittest.TestCase):

    """Tests for get_most_common."""

    def test_numbers(self):
        self.assertEqual(get_most_common([{1, 2}, {2, 3}, {3, 4}]), {2, 3})

    def test_restaurants(self):
        trey = {'Habaneros', 'Karl Strauss', 'Opera', 'Punjabi Tandoor'}
        diane = {'Siam Nara', 'Punjabi Tandoor', 'Opera'}
        peter = {'Karl Strauss', 'Opera', 'Habaneros'}
        common = get_most_common([trey, diane, peter])
        self.assertEqual(common, {'Opera'})


if __name__ == "__main__":
    unittest.main()
