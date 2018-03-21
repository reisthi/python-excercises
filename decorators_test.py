"""Tests for decorator exercises"""
from io import StringIO
from textwrap import dedent
import unittest
from unittest.mock import patch, MagicMock
from functools import partial

from helpers import redirect_stdout
from decorators import (call_logger, jsonify, groot, four, hide_errors,
                        catch_all, count_calls, make_partial)


class CallLoggerTests(unittest.TestCase):

    """Tests for call_logger."""

    def test_prints_before_and_after(self):
        def greet(): print("Hello")
        greet = call_logger(greet)
        with redirect_stdout(StringIO()) as stdout:
            greet()
        self.assertEqual(stdout.getvalue(), dedent("""
            Function started
            Hello
            Function returned
        """).lstrip())

    def test_returned(self):
        def return_hi(): return 'hi'
        return_hi = call_logger(return_hi)
        with redirect_stdout(StringIO()) as stdout:
            self.assertEqual(return_hi(), 'hi')
        self.assertEqual(stdout.getvalue(), dedent("""
            Function started
            Function returned
        """).lstrip())

    def test_takes_arguments(self):
        def add(x, y): return x + y
        add = call_logger(add)
        with redirect_stdout(StringIO()) as stdout:
            self.assertEqual(add(1, 2), 3)
            self.assertEqual(add(x=1, y=2), 3)


class JSONifyTests(unittest.TestCase):

    """Tests for jsonify."""

    def test_serialize_none(self):
        func = jsonify(lambda: None)
        self.assertEqual(func(), 'null')

    def test_serialize_list(self):
        def make_list(): return [4, 'hi', True, 5.5]
        make_list = jsonify(make_list)
        self.assertEqual(make_list(), '[4, "hi", true, 5.5]')

    def test_returned(self):
        def return_hi(): return 'hi'
        return_hi = jsonify(return_hi)
        self.assertEqual(return_hi(), '"hi"')

    def test_takes_arguments(self):
        def add(x, y): return x + y
        add = jsonify(add)
        self.assertEqual(add(1, 2), '3')
        self.assertEqual(add(x=1, y=2), '3')


class GrootTests(unittest.TestCase):

    """Tests for groot."""

    def test_print_groot(self):
        def greet(name): print("Hello {}".format(name))
        greet = groot(greet)
        with redirect_stdout(StringIO()) as stdout:
            greet("Trey")
        self.assertEqual(stdout.getvalue(), "Groot\n")

    def test_nothing_returned(self):
        def return_hi(): return 'hi'
        return_hi = groot(return_hi)
        with redirect_stdout(StringIO()) as stdout:
            self.assertEqual(return_hi(), None)

    def test_function_ignored(self):
        def return_hi(): dictionary['key'] = 'value'
        dictionary = {}
        return_hi = groot(return_hi)
        with redirect_stdout(StringIO()) as stdout:
            self.assertEqual(return_hi(), None)
        self.assertEqual(dictionary, {})

    def test_takes_arguments(self):
        def add(x, y): return x + y
        add = groot(add)
        with redirect_stdout(StringIO()) as stdout:
            add(1, 2)
            add(x=1, y=2)


class FourTests(unittest.TestCase):

    """Tests for four."""

    def test_return_four(self):
        def greet(name): print("Hello {}".format(name))
        with redirect_stdout(StringIO()) as stdout:
            greet = four(greet)
        self.assertEqual(stdout.getvalue(), '')
        self.assertEqual(greet, 4)


class HideErrorsTests(unittest.TestCase):

    """Tests for hide_errors."""

    def test_no_errors_raised(self):
        def error(): return 1 / 0
        error = hide_errors(error)
        self.assertEqual(error(), None)

    def test_return_value(self):
        def one(): return 1
        one = hide_errors(one)
        self.assertEqual(one(), 1)

    def test_takes_arguments(self):
        def divide(x, y): return x / y
        divide = hide_errors(divide)
        self.assertEqual(divide(1, 0), None)
        self.assertEqual(divide(0, 1), 0)
        self.assertEqual(divide(2, 2), 1)


class CatchAllTests(unittest.TestCase):

    """Tests for catch_all."""

    def test_suppress_error(self):
        def divide(x, y): return x / y
        divide = catch_all(divide)
        with redirect_stdout(StringIO()) as stdout:
            with patch('builtins.input', side_effect=['y']) as input:
                divide(1, 0)
        self.assertEqual(
            stdout.getvalue().strip(),
            "Exception occurred: division by zero"
        )
        input.assert_called_with("Should we ignore this exception (Y/n)? ")

    def test_do_not_suppress(self):
        def divide(x, y): return x / y
        divide = catch_all(divide)
        with redirect_stdout(StringIO()) as stdout:
            with patch('builtins.input', side_effect=['n']) as input:
                with self.assertRaises(ZeroDivisionError):
                    divide(1, 0)
        self.assertEqual(
            stdout.getvalue().strip(),
            "Exception occurred: division by zero"
        )
        input.assert_called_with("Should we ignore this exception (Y/n)? ")

    def test_return_value(self):
        def one(): return 1
        one = catch_all(one)
        self.assertEqual(one(), 1)

    def test_takes_arguments(self):
        def divide(x, y): return x / y
        divide = hide_errors(divide)
        self.assertEqual(divide(2, 1), 2)
        self.assertEqual(divide(0, 1), 0)


class CountCallsTests(unittest.TestCase):

    """Tests for count_calls."""

    def test_count_increments(self):
        func = MagicMock()
        func.__name__ = "func"
        decorated = count_calls(func)
        func.assert_not_called()
        decorated()
        func.assert_called_once_with(1)
        decorated()
        func.assert_called_with(2)

    def test_return_value(self):
        def one(count): return 1
        one = count_calls(one)
        self.assertEqual(one(), 1)

    def test_takes_arguments(self):
        def add(count, x, y): return x + y
        add = count_calls(add)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 3), 4)


class MakePartialTests(unittest.TestCase):

    """Tests for make_partial."""

    def test_make(self):
        @make_partial
        def add(x, y):
            return x + y
        self.assertIsInstance(add(1), partial)

    def test_add_1_2(self):
        @make_partial
        def add(x, y):
            return x + y
        self.assertEqual(add(1)(2), 3)

    def test_add_1_3(self):
        @make_partial
        def add(x, y):
            return x + y
        self.assertEqual(add(1)(3), 4)


if __name__ == "__main__":
    unittest.main()
