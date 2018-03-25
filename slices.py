"""Slice exercises"""


def last_n_elements(bar):
    """Return last ``n`` items from given list."""
    return bar.pop()


def last_words(bar, index):
    """Return the last words of the given string."""
    return bar.split()[-index:]


def split_in_half(bar):
    """Return two halves of the given iterable."""
    middle = int(len(bar) / 2)
    return bar[:middle], bar[middle:]


def first_and_last(bar):
    """ Returns the first and last items of a given string. """
    first, *middle, last = bar.split()
    return first, last
