"""List exercises"""

list_one = ['a', 'b', 'c', 1, 2, 3]
list_deux = ["Un", "deux", "trois"]
list_trois = ["Un", "deux", "trois"]
list_quatre = ["UN", "deux", "trois"]


def combine_lists(one, two):
    """Return a new list that combines the two given lists."""
    return one + two


def rotate_list(my_list):
    """Move first list item to end of list and return the item."""
    # return my_list[0], my_list[-1] == my_list[-1], my_list[0]
    item = my_list.pop(0)
    my_list.append(item)
    return item


def reverse_words(sentence):
    """Return the given sentence with the words in reverse order."""
    return sentence.reverse()


def ith_item_power(bar, index):
    """Returns i-th element raised to the i-th power."""
    result = bar[index]
    return result**index


def comp_lists(one, two):
    """ Compares two lists. Obs: It's case sensitive."""
    same_items = set(one) & set(two)
    return same_items

