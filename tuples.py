"""Tuple exercises"""
# Tuples and strings are immutable
# A single item is not a tuple item. Ex: tuple = (1)
# Unless you add a comma in the end. Ex: tuple = (1,)


def get_oldest(bar1, bar2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    year_one, year_two = bar1.split('/')[-1], bar2.split('/')[-1]
    month_one, month_two = bar1.split('/')[-2], bar2.split('/')[-2]
    day_one, day_two = bar1.split('/')[-3], bar2.split('/')[-3]

    date_one = (year_one, month_one, day_one)
    date_two = (year_two, month_two, day_two)

    if date_one > date_two:
        return print(str(date_two), "is older than: ", str(date_one))
    else:
        return print(str(date_one), "is older than: ", str(date_two))


def name_key(name):
    """Return last-first name tuple from first-last name tuple."""
    first_name = name.split(' ')[-2]
    last_name = name.split(' ')[-1]
    return last_name, first_name


def sort_names(name):
    """Return given first-last name tuples sorted by last name."""
    return sorted(name, key=name_key)


def name_key_simpler(name):
    first, last = name.split()
    return last, first


def swap_ends(bar):
    """Swap the first and last items in the given list."""

