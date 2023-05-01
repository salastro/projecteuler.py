def multiplies_less_than(l: list, n: int) -> list:
    """Take a list of integers and return a list of those integers that are
    multiples of the numbers in the list that are less than the number n."""
    m = [ False ] * n # Generate a list of lenght n with all False values.
    for i in l:
        for j in range(i, n, i):
            m[j] = True # Set the multiples of i to True.
    return [ i for i in range(n) if m[i] ] # Return the multiples.

print(sum(multiplies_less_than([3, 5], 1000)))
