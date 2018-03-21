"""Tests for exception exercises"""
import unittest

from unittest.mock import patch

from helpers import ModuleTestCase, run_program

from exception import len_or_none, deep_add, deep_flatten


class LenOrNoneTests(unittest.TestCase):

    """Tests for len_or_none."""

    def test_hello_string(self):
        self.assertEqual(len_or_none("hello"), 5)

    def test_4(self):
        self.assertIsNone(len_or_none(4))

    def test_empty_list(self):
        self.assertEqual(len_or_none([]), 0)

    def test_range(self):
        self.assertEqual(len_or_none(range(10)), 10)


class DeepAddTests(unittest.TestCase):

    """Tests for deep_add."""

    def test_shallow(self):
        self.assertEqual(deep_add([1, 2, 3, 4]), 10)

    def test_deeply_nested_iterables(self):
        self.assertEqual(deep_add([(1, 2), [3, {4, 5}]]), 15)


class CountdownTests(ModuleTestCase):

    """
    Tests for countdown.

    Count down from a given number, pausing for 1 second between each number.
    """

    module_path = 'countdown.py'

    def test_no_ctrl_c(self):
        with patch('time.sleep') as sleep:
            output = run_program('countdown.py', ['5'])
        self.assertEqual(output, '5\n4\n3\n2\n1\n')
        sleep.assert_called_with(1)
        self.assertEqual(sleep.call_count, 5)

    def test_ctrl_c_once(self):
        def ctrl_c(_): raise KeyboardInterrupt
        with patch('time.sleep', side_effect=ctrl_c) as sleep:
            output = run_program('countdown.py', ['1'])
        self.assertEqual(output, '1\nPress Ctrl-C again to exit\n')
        sleep.assert_called_once_with(1)

    def test_ctrl_c_twice(self):
        def ctrl_c(_): raise KeyboardInterrupt
        with patch('time.sleep', side_effect=ctrl_c) as sleep:
            output = run_program('countdown.py', ['2'], raises=SystemExit)
        self.assertEqual(
            output,
            '2\nPress Ctrl-C again to exit\n1\nGoodbye!\n',
        )
        sleep.assert_called_with(1)
        self.assertEqual(sleep.call_count, 2)


class DeepFlattenTests(unittest.TestCase):

    """Tests for deep_flatten."""

    def test_deep_lists(self):
        inputs = [0, [1, [2, 3]], [4]]
        outputs = [0, 1, 2, 3, 4]
        self.assertEqual(list(deep_flatten(inputs)), outputs)

    def test_empty_deep_list(self):
        self.assertEqual(list(deep_flatten([[()]])), [])

    @unittest.expectedFailure
    def test_bonus_strings(self):
        inputs = [(1, 2), [3, "bye", {4, 5}]]
        outputs = [1, 2, 3, 'bye', 4, 5]
        self.assertEqual(list(deep_flatten(inputs)), outputs)


if __name__ == "__main__":
    unittest.main()
