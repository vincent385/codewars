"""
    fib(n) = fib(n+2) - fib(n+1)
    Solution involves matrix transformation
    Might need to consider the logarithmic time version (modular arithmetic) *See bookmarks
"""


def fib(n):
    # recursive solution works but computation time O(2^n) is too slow for large values of n
    if n <= 1:
        return n
    return fib(n + 2) - fib(n + 1)


def fib_mtransform(m):
    # consider and study numpy matrix
    NotImplemented
 