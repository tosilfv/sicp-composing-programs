# Heron's method for approximating Square root

## Evolution A
"""def approx_sqrt(x, a):
    return 0.5 * (x + a/x)

def square_root(a, max_rounds = 100):
    x = 1
    k = 0
    while x * x != a and k < max_rounds:
        x = approx_sqrt(x, a)
        print(f"x: {x}")
        k = k + 1
    return x

square_root(24)
"""

## Evolution B
"""def approx_sqrt(x, a):
    return 0.5 * (x + a/x)

def close_to_sqrt(x, y, difference = 1e-14):
    assert(difference > 1e-15), 'difference cannot be below 1e-14'
    return abs(x - y) < difference

def square_root(a, max_rounds = 100):
    x = 1
    k = 0
    while not close_to_sqrt(x * x, a) and k < max_rounds:
        x = approx_sqrt(x, a)
        print(f"x: {x}")
        k = k + 1
    return x

square_root(24)
"""

## Evolution C
"""def approx_sqrt(x, a):
    return 0.5 * (x + a/x)

def close_to_sqrt(x, y, tolerance = 1e-14):
    assert(tolerance > 1e-15), 'tolerance must be over 1e-15'
    return abs(x - y) < tolerance

def improve(approx, close, guess = 1, max_rounds = 100):
    k = 0
    while not close(guess) and k < max_rounds:
        guess = approx(guess)
        print(f"guess: {guess}")
        k = k + 1
    return guess

def square_root(a):
    def approx(x):
        return approx_sqrt(x, a)
    def close(x):
        return close_to_sqrt(x * x, a)
    return improve(approx, close)

square_root(2)
"""

## Evolution D
from doctest import run_docstring_examples

def approx(x, a):
    """Approximates the square root of a, returns float.
    
    >>> approx(2, 4)
    2.0
    """
    return 0.5 * (x + a / x)

def close(x, y, tolerance = 1e-14):
    """Compares absolute value of x - y and tolerance, returns bool.
    
    >>> close(1 * 1, 25)
    False
    """
    assert(tolerance > 1e-15), 'tolerance must be over 1e-15'
    return abs(x - y) < tolerance

def calc(approx, close, guess = 1, max_approxs = 100):
    """Calculates close approximation of e.g. square root, returns float."""
    k = 0
    while not close(guess) and k < max_approxs:
        guess = approx(guess)
        print(f"guess: {guess}")
        k = k + 1
    return guess

def square_root(a):
    return calc(lambda x: approx(x, a),
                   lambda x: close(x * x, a))

run_docstring_examples(approx, globals(), True)
run_docstring_examples(close, globals(), True)
### Testing a Huge number:
square_root(14537524845386523763451735673455437524.26268675964722634563426432613)
