"""Tests for star exercises"""
import unittest


from stars import unzip, interleave, html_tag


class UnzipTests(unittest.TestCase):

    """Tests for unzip."""

    def test_two_tuples(self):
        self.assertEqual(unzip([(0, 1), (2, 3)]), [(0, 2), (1, 3)])

    def test_three_tuples(self):
        zipped = [(0, 2, 4), (1, 3, 5)]
        expected = [(0, 1), (2, 3), (4, 5)]
        self.assertEqual(unzip(zipped), expected)


class InterleaveTests(unittest.TestCase):

    """Tests for interleave."""

    def test_empty_lists(self):
        self.assertEqual(interleave([], []), [])

    def test_single_item_each(self):
        self.assertEqual(interleave([1], [2]), [1, 2])

    def test_two_items_each(self):
        self.assertEqual(interleave([1, 2], [3, 4]), [1, 3, 2, 4])

    def test_four_items_each(self):
        in1 = [1, 2, 3, 4]
        in2 = [5, 6, 7, 8]
        out = [1, 5, 2, 6, 3, 7, 4, 8]
        self.assertEqual(interleave(in1, in2), out)

    def test_none_value(self):
        in1 = [1, 2, 3, None]
        in2 = [4, 5, 6, 7]
        out = [1, 4, 2, 5, 3, 6, None, 7]
        self.assertEqual(interleave(in1, in2), out)

    def test_more_than_two_arguments(self):
        in1 = [1, 2, 3]
        in2 = [4, 5, 6]
        in3 = [7, 8, 9]
        out = [1, 4, 7, 2, 5, 8, 3, 6, 9]
        self.assertEqual(interleave(in1, in2, in3), out)


class HTMLTagTests(unittest.TestCase):

    """Tests for html_tag."""

    def assertTagEqual(self, tag1, tag2):
        split1 = tag1[1:-1].split(' ')
        name1, attrs1 = split1[0], split1[1:]
        split2 = tag2[1:-1].split(' ')
        name2, attrs2 = split2[0], split2[1:]
        self.assertEqual(name1, name2)
        self.assertEqual(sorted(attrs1), sorted(attrs2))
        self.assertEqual(tag1[0], tag2[0])
        self.assertEqual(tag1[-1], tag2[-1])

    def test_input(self):
        html = html_tag("input", type="email", name="email",
                        placeholder="E-mail")
        expected = '<input name="email" placeholder="E-mail" type="email">'
        self.assertTagEqual(html, expected)

    def test_img(self):
        html = html_tag("img", src="https://placehold.it/10x10", alt="Sample")
        expected = '<img alt="Sample" src="https://placehold.it/10x10">'
        self.assertTagEqual(html, expected)


if __name__ == "__main__":
    unittest.main()
