"""Tests for regular expression exercises"""
from textwrap import dedent
import unittest

from regexes import (count_punctuation, count_numbers, get_extension,
                     normalize_jpeg, normalize_whitespace, is_hex_color)


class CountPunctionationTests(unittest.TestCase):

    """Tests for count_punctuation."""

    def test_count_punctuation(self):
        self.assertEqual(
            count_punctuation("^_^ hello there! @_@"),
            {'^': 2, '@': 2, '!': 1}
        )


class CountNumbersTests(unittest.TestCase):

    """Tests for count_numbers."""

    def test_count_numbers(self):
        self.assertEqual(
            count_numbers("Why was 6 afraid of 7? Because 7 8 9."),
            {'7': 2, '9': 1, '6': 1, '8': 1}
        )


class GetExtensionTests(unittest.TestCase):

    """Tests for get_extension."""

    def test_zip(self):
        self.assertEqual(get_extension('archive.zip'), 'zip')

    def test_jpeg(self):
        self.assertEqual(get_extension('image.jpeg'), 'jpeg')

    def test_xhtml(self):
        self.assertEqual(get_extension('index.xhtml'), 'xhtml')

    def test_gzipped_tarball(self):
        self.assertEqual(get_extension('archive.tar.gz'), 'gz')


class NormalizeJPEGTests(unittest.TestCase):

    """Tests for normalize_jpeg."""

    def test_jpeg(self):
        self.assertEqual(normalize_jpeg('avatar.jpeg'), 'avatar.jpg')

    def test_capital(self):
        self.assertEqual(normalize_jpeg('Avatar.JPEG'), 'Avatar.jpg')

    def test_mixed_case(self):
        self.assertEqual(normalize_jpeg('AVATAR.Jpg'), 'AVATAR.jpg')

    def test_gif(self):
        self.assertEqual(normalize_jpeg('avatar.gif'), 'avatar.gif')


class NormalizeWhitespaceTests(unittest.TestCase):

    """Tests for normalize_whitespace."""

    def test_two_spaces(self):
        self.assertEqual(normalize_whitespace("hello  there"), "hello there")

    def test_poem(self):
        poem = dedent("""
            Hold fast to dreams
            For if dreams die
            Life is a broken-winged bird
            That cannot fly.

            Hold fast to dreams
            For when dreams go
            Life is a barren field
            Frozen with snow.
        """).strip()
        self.assertEqual(
            normalize_whitespace(poem),
            'Hold fast to dreams For if dreams die '
            'Life is a broken-winged bird That cannot fly. '
            'Hold fast to dreams For when dreams go '
            'Life is a barren field Frozen with snow.'
        )


class IsHexColorTests(unittest.TestCase):

    """Tests for is_hex_color."""

    def test_purple_short(self):
        self.assertTrue(is_hex_color("#639"))

    def test_four_digits(self):
        self.assertFalse(is_hex_color("#6349"))

    def test_five_digits(self):
        self.assertFalse(is_hex_color("#63459"))

    def test_dark_purple(self):
        self.assertTrue(is_hex_color("#634569"))

    def test_purple_long(self):
        self.assertTrue(is_hex_color("#663399"))

    def test_black(self):
        self.assertTrue(is_hex_color("#000000"))

    def test_two_digits(self):
        self.assertFalse(is_hex_color("#00"))

    def test_mixed_case(self):
        self.assertTrue(is_hex_color("#FFffFF"))

    def test_hex(self):
        self.assertTrue(is_hex_color("#decaff"))

    def test_invalid_character(self):
        self.assertFalse(is_hex_color("#decafz"))


if __name__ == "__main__":
    unittest.main()
