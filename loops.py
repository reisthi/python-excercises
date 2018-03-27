"""Loop exercises"""


def get_vowel_names(bars):
    """Return a list containing all names given that start with a vowel."""
    vowels = 'aeiou'
    vowel_names = []
    for name in bars:
        if name[0].lower() in vowels:
            vowel_names.append(bars)
    return vowel_names


def product(numbers):
    """Returning all given numbers multiplied together."""
    result = 1
    for n in numbers:
        result *= n
    return result


def flatten():
    """Return a flattened version of the given 2-D matrix ()."""


def words_containing(bar, letter):
    """Return all words that contain the given letter."""
    bucket = []
    for a in bar:
        if letter in a:
            bucket.append(a)
    return bucket


