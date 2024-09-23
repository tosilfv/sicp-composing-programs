from doctest import run_docstring_examples
def create_adder(k):
    """This function takes one argument k and returns a
    function that takes one argument n and adds
    arguments k and n together.

    >>> add_nums = create_adder(5)
    >>> add_nums(10)
    15
    """
    assert(type(int(k)) == int or type(float(k)) == float), 'create_adder(k) argument is not a number'
    def adder(n):
        assert(type(int(n)) == int or type(float(n)) == float), 'adder(n) argument is not a number'
        return k + n
    return adder

run_docstring_examples(create_adder, globals(), True)
nums = create_adder(2344.6)
sum_nums = nums(1.3876)
print(f"sum_nums: {sum_nums}")
