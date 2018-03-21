"""Tests for module exercises"""
from io import StringIO
import unittest

from helpers import run_program, import_module, redirect_stdout, ModuleTestCase


class GreetingsTests(ModuleTestCase):

    """
    Tests for greetings.

    Greet given user or greet the world if no arguments given.
    """

    module_path = 'greetings.py'

    def test_no_arguments(self):
        output = run_program('greetings.py')
        self.assertEqual(output, "Hello world!\n")

    def test_with_argument(self):
        output = run_program('greetings.py', ['Trey'])
        self.assertEqual(output, "Hello Trey!\n")

    # Comment the following line for testing changes for multiple arguments
    @unittest.expectedFailure
    def test_with_multiple_arguments(self):
        output = run_program('greetings.py', ['Trey', 'Hunner'])
        self.assertEqual(output, "Hello Trey Hunner!\n")


class HelloTests(ModuleTestCase):

    """
    Tests for hello.

    Print hello world when run from command-line but not when imported.
    """

    module_path = 'hello.py'

    def test_cli(self):
        output = run_program('hello.py')
        self.assertEqual(output, "Hello world!\n")

    def test_import(self):
        with redirect_stdout(StringIO()) as output:
            import_module('hello')
        self.assertIn("command-line", output.getvalue())

    @unittest.expectedFailure
    def test_exception_on_import(self):
        with self.assertRaises(ImportError) as cm:
            import_module('hello')
        self.assertIn("command-line", str(cm.exception))


class AddTests(ModuleTestCase):

    """
    Tests for add.

    Add two numbers together.
    """

    module_path = 'add.py'

    def test_integers(self):
        output = run_program('add.py', ['1', '2'])
        self.assertEqual(output, "3.0\n")

    def test_floats(self):
        output = run_program('add.py', ['1.5', '2'])
        self.assertEqual(output, "3.5\n")

    def test_negative_numbers(self):
        output = run_program('add.py', ['-7', '2'])
        self.assertEqual(output, "-5.0\n")
        output = run_program('add.py', ['-2', '-1'])
        self.assertEqual(output, "-3.0\n")

    def test_strings(self):
        with self.assertRaises(Exception):
            run_program('add.py', ['hello', 'hi'])


class DifferenceTests(ModuleTestCase):

    """
    Tests for difference.

    Print the difference between two numbers.
    """

    module_path = 'difference.py'

    def test_integers(self):
        output = run_program('difference.py', ['3', '5'])
        self.assertEqual(output, "2.0\n")

    def test_floats(self):
        output = run_program('difference.py', ['6', '3.5'])
        self.assertEqual(output, "2.5\n")

    def test_negative_numbers(self):
        output = run_program('difference.py', ['-7', '2'])
        self.assertEqual(output, "9.0\n")

    def test_strings(self):
        with self.assertRaises(Exception):
            run_program('difference.py', ['hello', 'hi'])


class AverageTests(ModuleTestCase):

    """
    Tests for average.

    Average all given numbers.
    """

    module_path = 'average.py'

    def test_whole_number_result(self):
        output = run_program('average.py', ['2', '3', '4'])
        self.assertEqual(output, "Average is 3.0\n")

    def test_decimal_number_result(self):
        output = run_program('average.py', ['2', '3', '4', '5', '6', '7'])
        self.assertEqual(output, "Average is 4.5\n")

    @unittest.expectedFailure
    def test_no_numbers(self):
        with self.assertRaises(SystemExit) as context:
            output = run_program('average.py')
        self.assertEqual(str(context.exception), "No numbers to average!")

    @unittest.expectedFailure
    def test_strings(self):
        with self.assertRaises(SystemExit) as context:
            run_program('average.py', ['hello', 'hi'])
        self.assertEqual(
            str(context.exception),
            "Invalid values entered, only numbers allowed!",
        )


if __name__ == "__main__":
    unittest.main()
