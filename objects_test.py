"""Tests for object exercises"""
import unittest

from objects import (exclude, call, call_later, call_again, only_once, cache,
                     partial)


class ExcludeTests(unittest.TestCase):

    """Tests for exclude."""

    def test_bool_exclude(self):
        self.assertEqual(
            exclude(bool, [False, True, False]),
            [False, False],
        )

    def test_lambda_exclude(self):
        self.assertEqual(
            exclude(lambda x: len(x) > 3, ["red", "blue", "green"]),
            ['red'],
        )


class CallTests(unittest.TestCase):

    """Tests for call."""

    def test_int_call(self):
        self.assertEqual(call(int), 0)

    def test_five_call(self):
        self.assertEqual(call(int, "5"), 5)

    def test_hello_call(self):
        self.assertEqual(call(len, "hello"), 5)

    def test_zip_call(self):
        self.assertEqual(list(call(zip, [1, 2], [3, 4])), [(1, 3), (2, 4)])


class CallLaterTests(unittest.TestCase):

    """Tests for call_later."""

    def test_append_to_list(self):
        names = []
        append_name = call_later(names.append, "Trey")
        self.assertIsNone(append_name())
        self.assertEqual(names, ['Trey'])
        append_name()
        self.assertEqual(names, ['Trey', 'Trey'])

    def test_zip_later(self):
        call_zip = call_later(zip, [1, 2], [3, 4])
        self.assertEqual(list(call_zip()), [(1, 3), (2, 4)])


class CallAgainTests(unittest.TestCase):

    """Tests for call_again."""

    def test_str_on_list(self):
        names = []
        response, names_as_str = call_again(str, names)
        self.assertEqual(response, '[]')
        names.append("Diane")
        self.assertEqual(names_as_str(), "['Diane']")


class OnlyOnceTests(unittest.TestCase):

    """Tests for only_once."""

    def test_do_once(self):
        def do_something(x, y):
            return x * 2 + y ** 2

        do_something_once = only_once(do_something)
        do_something_once(1, 2)
        with self.assertRaises(ValueError):
            do_something_once(1, 2)


class CacheTests(unittest.TestCase):

    """Tests for cache."""

    def test_no_arguments(self):
        def compute(): return 4
        cached_func = cache(compute)
        self.assertEqual(cached_func(), 4)
        self.assertEqual(cached_func(), 4)

    def test_one_argument(self):
        def compute(x): return x
        cached_func = cache(compute)
        self.assertEqual(cached_func(1), 1)
        self.assertEqual(cached_func(2), 2)
        self.assertEqual(cached_func(1), 1)

    def test_mutate_and_compute(self):
        responses = []
        def compute(x, y):
            responses.append(x * 2 + y ** 2)
            return responses[-1]
        cached_func = cache(compute)
        self.assertEqual(responses, [])
        self.assertEqual(cached_func(1, 2), 6)
        self.assertEqual(responses, [6])
        self.assertEqual(cached_func(1, 2), 6)
        self.assertEqual(responses, [6])
        self.assertEqual(cached_func(2, 1), 5)
        self.assertEqual(responses, [6, 5])

    @unittest.expectedFailure
    def test_keyword_arguments(self):
        responses = []
        def compute(x, y):
            responses.append(x * 2 + y ** 2)
            return responses[-1]
        cached_func = cache(compute)
        self.assertEqual(responses, [])
        self.assertEqual(cached_func(1, 2), 6)
        self.assertEqual(responses, [6])
        self.assertEqual(cached_func(2, 1), 5)
        self.assertEqual(responses, [6, 5])
        self.assertEqual(cached_func(1, 2), 6)
        self.assertEqual(responses, [6, 5])
        self.assertEqual(cached_func(x=1, y=2), 6)
        self.assertEqual(responses, [6, 5, 6])


# Helper function for PartialTests
def my_func(*args, **kwargs):
    return (args, kwargs)


class PartialTests(unittest.TestCase):

    """Tests for partial."""

    def test_no_arguments(self):
        g = partial(my_func)
        self.assertEqual(g(), ((), {}))
        self.assertEqual(g(3), ((3,), {}))
        self.assertEqual(g(3, 4, 5), ((3, 4, 5), {}))
        self.assertEqual(g(m='m'), ((), {'m': 'm'}))
        self.assertEqual(g(m='m', x=3), ((), {'x': 3, 'm': 'm'}))
        self.assertEqual(g(1, 2, m='m', x=3), ((1, 2), {'x': 3, 'm': 'm'}))

    def test_only_positional_args(self):
        g = partial(my_func, 1, 'a')
        self.assertEqual(g(), ((1, 'a'), {}))
        self.assertEqual(g(3), ((1, 'a', 3), {}))
        self.assertEqual(g(3, 4, 5), ((1, 'a', 3, 4, 5), {}))
        self.assertEqual(g(m='m'), ((1, 'a'), {'m': 'm'}))
        self.assertEqual(g(m='m', x=3), ((1, 'a'), {'x': 3, 'm': 'm'}))
        self.assertEqual(
            g(1, 2, m='m', x=3),
            ((1, 'a', 1, 2), {'x': 3, 'm': 'm'})
        )

    def test_only_keyword_arguments(self):
        g = partial(my_func, a='a', x=1)
        self.assertEqual(g(), ((), {'a': 'a', 'x': 1}))
        self.assertEqual(g(3), ((3,), {'a': 'a', 'x': 1}))
        self.assertEqual(g(3, 4, 5), ((3, 4, 5), {'a': 'a', 'x': 1}))
        self.assertEqual(g(m='m'), ((), {'a': 'a', 'x': 1, 'm': 'm'}))
        self.assertEqual(g(m='m', x=3), ((), {'a': 'a', 'x': 3, 'm': 'm'}))
        self.assertEqual(
            g(1, 2, m='m', x=3),
            ((1, 2), {'a': 'a', 'x': 3, 'm': 'm'})
        )

    def test_positional_and_keyword_arguments(self):
        g = partial(my_func, 1, 'a', a='a', x=1)
        self.assertEqual(g(), ((1, 'a'), {'a': 'a', 'x': 1}))
        self.assertEqual(g(3), ((1, 'a', 3), {'a': 'a', 'x': 1}))
        self.assertEqual(g(3, 4, 5), ((1, 'a', 3, 4, 5), {'a': 'a', 'x': 1}))
        self.assertEqual(g(m='m'), ((1, 'a'), {'a': 'a', 'x': 1, 'm': 'm'}))
        self.assertEqual(
            g(m='m', x=3),
            ((1, 'a'), {'a': 'a', 'x': 3, 'm': 'm'})
        )
        self.assertEqual(
            g(1, 2, m='m', x=3),
            ((1, 'a', 1, 2), {'a': 'a', 'x': 3, 'm': 'm'})
        )


if __name__ == "__main__":
    unittest.main()
