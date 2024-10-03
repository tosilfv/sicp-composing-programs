from doctest import run_docstring_examples

def sum_nums_up_to_n(n, term):
    """ Sums positive integers according to term up to n.

    >>> sum_nums_up_to_n(2, square)
    5
    >>> sum_nums_up_to_n(2, cube)
    9
    """
    sum, x = 0, 1
    while x <= n:
        sum, x = sum + term(x), x + 1
    return sum

def square(x):
    return x * x

def cube(x):
    return x * x * x

def approximate_pi(x):
    return 8 / ((4 * x - 3) * (4 * x - 1))

def calculate_squares(n):
    return sum_nums_up_to_n(n, square)

def calculate_cubes(n):
    return sum_nums_up_to_n(n, cube)

def calculate_pi(n):
    return sum_nums_up_to_n(n, approximate_pi)

sum_of_squares = calculate_squares(100)
sum_of_cubes = calculate_cubes(100)
sum_of_pi = calculate_pi(1e6) # values above 1e6 compute SLOWLY!

print(f"\n\nsum_of_squares: {sum_of_squares} \n\n")
print(f"\n\nsum_of_cubes: {sum_of_cubes} \n\n")
print(f"\n\nsum_of_pi: {sum_of_pi} \n\n")

run_docstring_examples(sum_nums_up_to_n, globals(), True)
