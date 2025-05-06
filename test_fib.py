from fib import fib

def test_fib_is_function():
    assert callable(fib), "fib should be a function"

def test_fib_has_docstring():
    assert fib.__doc__ is not None, "fib should have a docstring"

def test_fib_name():
    assert fib.__name__ == "fib", "fib function should be named 'fib'"

def test_fib_0_returns_0():
    assert fib(0) == 0, "fib(0) should return 0"

def test_fib_1_returns_1():
    assert fib(1) == 1, "fib(1) should return 1"

def test_fib_2_returns_1():
    assert fib(2) == 1, "fib(2) should return 1"

def test_fib_3_returns_2():
    assert fib(3) == 2, "fib(3) should return 2"

def test_fib_4_returns_3():
    assert fib(4) == 3, "fib(4) should return 3"

def test_fib_5_returns_5():
    assert fib(5) == 5, "fib(5) should return 5"

def test_fib_6_returns_8():
    assert fib(6) == 8, "fib(6) should return 8"

def test_fib_7_returns_13():
    assert fib(7) == 13, "fib(7) should return 13"

def test_fib_8_returns_21():
    assert fib(8) == 21, "fib(8) should return 21"

def test_fib_9_returns_34():
    assert fib(9) == 34, "fib(9) should return 34"

def test_fib_10_returns_55():
    assert fib(10) == 55, "fib(10) should return 55"
