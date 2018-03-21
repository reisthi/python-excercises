"""Decorator exercises"""
import json
from functools import partial, wraps


def call_logger(func):
    """Return a new function that calls func and prints when it was called."""
    def new_func(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function returned")
        return result
    return new_func


def jsonify(func):
    """Decorate function to JSON-encode return value."""
    @wraps(func)
    def new_func(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return new_func


def groot(func):
    """Return function which prints 'Groot' (ignore decoratee)."""
    @wraps(func)
    def new_func(*args, **kwargs):
        print("Groot")
    return new_func


def four(func):
    """Return 4 (ignore decorated function)."""
    return 4


def hide_errors(func):
    """Trap and ignore non-exiting errors."""
    @wraps(func)
    def new_func(*args):
        try:
            return func(*args)
        except Exception:
            return
    return new_func


def catch_all(func):
    """Trap non-exiting errors and ask user if we should ignore."""
    @wraps(func)
    def new_func(*args):
        try:
            return func(*args)
        except Exception as error:
            print("Exception occurred: {}".format(error))
            answer = input("Should we ignore this exception (Y/n)? ")
            if answer.lower() == "n":
                raise
    return new_func


def count_calls(func):
    """Pass call counts into first argument to the function."""
    @wraps(func)
    def new_func(*args):
        new_func.call_count += 1
        return func(new_func.call_count, *args)
    new_func.call_count = 0
    return new_func


def make_partial(func):
    """Returns a new partially-evaluated function."""
    @wraps(func)
    def new_func(*args):
        return partial(func, *args)
    return new_func
