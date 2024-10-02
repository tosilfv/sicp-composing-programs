# Recursive function calls itself.
from doctest import run_docstring_examples

def split(m):
    return m // 10, m % 10

def sum_digits(n):
    """Sums digits of number n together, returns int or float.
    
    >>> sum_digits(546)
    15
    """
    assert(n >= 0), 'n cannot be negative'
    if n < 10:
        return n
    all_but_last, last = split(n)
    return sum_digits(all_but_last) + last

run_docstring_examples(sum_digits, globals(), True)

print(f"sum_digits(1234567.0): {sum_digits(1234567.0)}")
