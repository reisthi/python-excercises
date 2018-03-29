"""Dictionary exercises"""


def flip_dict(old):
    """Return a new dictionary that maps the original values to the keys."""
    new = {}
    for key, value in old.items():
        new[value] = key
    return new


def get_all_factors():
    """Return a dictionary mapping numbers to their factors."""


def translate(sentence):
    """Return a transliterated version of the given sentence."""
    # d = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    # new = []
    # for word in sentence.split():
    #     new.append(d[word])
    # return ' '.join(new)


def count_words():
    """Return the number of times each word occurs in the string."""


def is_anagram():
    """Return True if the given words are anagrams."""


def get_ascii_codes():
    """Return a dictionary mapping the strings to ASCII codes."""


def dict_from_truple():
    """Turn three-item tuples into a dictionary of two-valued tuples."""


def dict_from_tuple():
    """Turn multi-item tuples into a dictionary of two-valued tuples."""


dict_one = {'one': 1, 'two': 2}
dict_two = {'three': 3, 'four': 4}


def display_dict(wip):
    """ Returns all the items of a dictionary. """
    # name_of_the_dict.items()
    return wip.items()


def dict_values(wip):
    """ Get the values of a dictionary. """
    # name_of_the_dict.values()
    return wip.values()


def dict_update(wip):
    """ Adds a dictionary to the current dictionary. """
    # name_of_the_dict_one.update(name_of_dict_2)
    return wip.update(dict_two)


def merge_merges(wip, wip_two):
    """ Simple way to marge two dictionaries in python 3. """
    # ** is the magic, details on the brackets
    return {**wip, **wip_two}


def dict_copy(wip):
    """ Returns a shallow copy of a dictionary. """
    copy_of_dict = wip.copy()
    return copy_of_dict


def dict_clear(wip):
    """ Deletes all key-values of a dictionary. """
    return wip.clear()
