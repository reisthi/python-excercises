"""Range exercises"""


def get_factors(number):
    """Return a list of all factors of the given number."""
    result = []
    for x in range(1, number + 1):
        if number % x == 0:
            result.append(x)
    return result


def is_prime(number):
    """Return True if candidate number is prime."""
    for x in range(2, number):
        if number % x == 0:
            return False
    return True


def power_list():
    """Return a list that contains each number raised to the i-th power."""


def identity():
    """Return an identity matrix of size x size."""


def is_range():
    """Return True if given list could be represented by range with step 1."""


def triples():
    """Return list of Pythagorean triples less than input num."""


def prints(list):
    for n in range(list):
        print(n)