# Decorators are used e.g. for tracing.
from doctest import run_docstring_examples

def trace_1(f):
    """Returns a version of function f that first prints
       before is getting called.
    """
    def wrapper(x):
        print(f"\nYou called {f} on argument {x}.")
        return f(x)
    return wrapper

@trace_1 ## Comment out to run doctest
def square(x):
    """Squares the value of x.

    >>> square(2)
    4
    """
    return x * x

def cube(x):
    """Cubes the value of x.

    >>> cube(2)
    8
    """
    return x * x * x
cube = trace_1(cube) ## same as @trace_1

run_docstring_examples(square, globals(), True)
run_docstring_examples(cube, globals(), True)

num = 5

squared = square(num)
print(f"{num} squared: {squared}")
cubed = cube(num)
print(f"{num} cubed: {cubed}")
