# Iteration is a special case of recursion.
from doctest import run_docstring_examples

def fact_iter(n):
    """Gets n factorial by starting k as 1 that goes up to n
       and multiplies k each time.
       
    >>> fact_iter(5)
    120
    """
    assert(n > 0), 'n must be positive'
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total

def fact_recu(n):
    """Gets n factorial by n times n minus 1 factorial if
       n is over zero and 1 otherwise.
    
    >>> fact_recu(10)
    3628800
    """
    assert(n >= 0), 'n must be positive or zero'
    if n == 0:
        return 1
    return n * fact_recu(n - 1)

run_docstring_examples(fact_iter, globals(), True)
run_docstring_examples(fact_recu, globals(), True)
print(f"fact_iter(3): {fact_iter(3)}")
print(f"fact_recu(3): {fact_recu(3)}")
