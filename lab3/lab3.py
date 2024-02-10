def fibonacci(n: int) -> int:
    """Returns n-th Fibonacci number.

    Args:
        n: Index of the Fibonacci number to be found
    
    Returns:
        A Fibonacci number in int format
    
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(10)
    55
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
    return a

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Formatting based on Google's style guide
# https://google.github.io/styleguide/pyguide.html