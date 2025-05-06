import pytest
from fib import fib

def test_fib_is_function():
    assert callable(fib), "fib should be a function"

def test_fib_has_docstring():
    assert fib.__doc__ is not None, "fib should have a docstring"

def test_fib_name():
    assert fib.__name__ == "fib", "fib function should be named 'fib'"
