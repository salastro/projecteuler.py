def generate_primes(n):
    p = [ False ] * n
    for i in range(2, n):
        if not p[i]:
            for j in range(i*i, n, i):
                p[j] = True
    return [ i for i in range(2, n) if not p[i] ]

def prime_factors(n):
    primes = generate_primes(int(n**0.5) + 1)
    factors = []
    for p in primes:
        if n % p == 0:
            factors.append(p)
    return factors

print(max(prime_factors(600851475143)))
