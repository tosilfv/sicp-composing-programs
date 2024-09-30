# Newton's method to finding zeros of the function.
from doctest import run_docstring_examples

def find_zero(f, df):
    """Takes in function and its derivative and gives back zero approximation."""
    return calc(update(f, df),
                lambda x: close(f(x), 0))

def update(f, df):
    """Takes in x and gives back better x."""
    return lambda x: x - f(x) / df(x)

def power(x, n):
    """Raises number x to particular power n, returns int or float.
    
    >>> power(2, 3)
    8
    """
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def close(x, y, tolerance = 1e-16):
    """Compares absolute value of x - y and tolerance, returns bool.
    
    >>> close(2 * 2, 52)
    False
    """
    assert(tolerance <= 1e-15), 'tolerance must be at least 1e-15'
    return abs(x - y) < tolerance

def calc(approx, close, guess = 1, max_approxs = 100):
    """Calculates close approximation of e.g. square root, returns float."""
    k = 0
    while not close(guess) and k < max_approxs:
        guess = approx(guess)
        # print(f"guess: {guess}")
        k = k + 1
    return guess

def nth_root_of_a(n, a):
    """Finds the n'th root of a, returns float."""
    return find_zero(lambda x: power(x, n) - a,
                     lambda x: n * power(x, n-1))

run_docstring_examples(power, globals(), True)
run_docstring_examples(close, globals(), True)
print(nth_root_of_a(2, 4))
print(nth_root_of_a(2, 16))
print(nth_root_of_a(2, 64))
print(nth_root_of_a(3, 64))
print(nth_root_of_a(3, 729))
print(nth_root_of_a(6, 64))
