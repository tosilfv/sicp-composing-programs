# Currying transforms multi-argument function into single-argument function.
from doctest import run_docstring_examples
from operator import add

def curry_v1(f):
    """Takes in fn, returns f of x y.
    
    >>> k = curry_v1(add)
    >>> k(22)(33)
    55
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

curry_v2 = lambda f: lambda x: lambda y: f(x, y)

run_docstring_examples(curry_v1, globals(), True)

m = curry_v1(add)
n = m(3)
s = n(4)
print(f"s: {s}")

u = curry_v2(add)
v = u(3.0)(4.0)
print(f"v: {v}")
