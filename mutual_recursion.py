# Mutual recursion divides a recursive procedure among
# two functions that call each other.

def is_even(m):
    """Checks if number m is even, returns boolean."""
    assert(type(int(m)) == int or type(float(m)) == float), 'is_even(m) argument is not a number'
    if m == 0:
        return True
    return is_odd(m - 1)

def is_odd(n):
    assert(type(int(n)) == int or type(float(n)) == float), 'is_odd(n) argument is not a number'
    """Checks if number n is odd, returns boolean."""
    if n == 0:
        return False
    return is_even(n - 1)

print(f"is_even(6): {is_even(6)}")
print(f"is_odd(5): {is_odd(5)}")