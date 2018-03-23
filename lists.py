"""List exercises"""


def combine_lists(one, two):
    """Return a new list that combines the two given lists."""
    return one + two


def rotate_list(my_list):
    """Move first list item to end of list and return the item."""
    # return my_list[0], my_list[-1] == my_list[-1], my_list[0]
    item = my_list.pop(0)
    my_list.append(item)
    return item


def reverse_words():
    """Return the given sentence with the words in reverse order."""


def ith_item_power():
    """Returns i-th element raised to the i-th power."""


#
# from lists import rotate_list
# b = [4, 5, 6]
# rotate_list(b)