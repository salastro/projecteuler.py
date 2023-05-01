def generate_fibonacci(n: int) -> list:
    """Generate a Fibonacci sequence less than n."""
    f = [0, 1]
    i = 0
    while f[i + 1] <= n:
        f.append(f[i] + f[i + 1])
        i += 1
    f.pop(i+1) # remove the last element (which is greater than n)
    return f

def check_even(numbers: list) -> list:
    """Return a list of even numbers."""
    return [n for n in numbers if n % 2 == 0]

def sum_even_fibonacci(n: int) -> int:
    """Return the sum of even Fibonacci numbers less than n."""
    return sum(check_even(generate_fibonacci(n)))
     
print(sum_even_fibonacci(4_000_000))
