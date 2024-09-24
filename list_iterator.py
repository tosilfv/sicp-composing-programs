from doctest import run_docstring_examples
def iter_list(t):
    """Returns a sublist of list iterator t where
       each subsequent list item is greater than the
       previous one.
    
    >>> iter_list(iter([5, 2, 4, 1, 5, 3, 7, 0, 9, 12, 11]))
    [5, 7, 9, 12]
    """
    try:
        x = next(t)
    except StopIteration:
        return []
    return [x] + iter_list(filter(lambda y: y > x, t))

run_docstring_examples(iter_list, globals(), True)
