# Luhn Algorithm checks if credit card number is valid.
# The returning sum must be a multiple of 10 to be valid.
from doctest import run_docstring_examples

def split(m):
    """Splits m to two parts, all but the last digit and the last digit."""
    return m // 10, m % 10 # 2024: 202, 4

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

def luhn_sum_digits(n):
    """From the rightmost digit, moving left, double every second digit,
       e.g. luhn_sum_digits(10): 2 + 0 = 2,
       or
       e.g. luhn_sum_digits(15): 2 + 5 = 7,
       then return the sum of ALL digits,
       returns int.
    
    >>> luhn_sum_digits(10)
    2
    >>> luhn_sum_digits(15)
    7
    """
    assert(n >= 0), 'n cannot be negative'
    if n < 10:
        return n
    all_but_last, last = split(n)
    return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    """If doubling is greater than 9 then return the sum of digits,
       e.g. luhn_sum_double(8): 2 * 8 = 16 => 1 + 6 = 7,
       otherwise return 2 * n
       e.g. luhn_sum_double(4): 2 * 4 = 8,
       returns int.
    
    >>> luhn_sum_double(8)
    7
    >>> luhn_sum_double(4)
    8
    """
    assert(n >= 0), 'n cannot be negative'
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    return luhn_sum_digits(all_but_last) + luhn_digit

run_docstring_examples(sum_digits, globals(), True)
run_docstring_examples(luhn_sum_digits, globals(), True)
run_docstring_examples(luhn_sum_double, globals(), True)

print(f"luhn_sum_digits(5105105105105100): {luhn_sum_digits(5105105105105100)}")
