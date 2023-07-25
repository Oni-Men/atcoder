T = int(input())
cases = [int(input()) for _ in range(T)]

primes = [True] * (10 ** 6)
primes[0] = False
primes[1] = False

for i in range(2, len(primes)):
    if not primes[i]:
        continue
    j = 2
    while i * j < len(primes):
        primes[i * j] = False
        j += 1

primes = [i for i, p in enumerate(primes) if p]

for n in cases:
    for i in primes:
        if n % i != 0:
            continue
        if n % i ** 2 == 0:
            p = i
            q = n // (p ** 2)
            print(p, q)
        else:
            q = i
            p = round((n / q) ** 0.5)
            print(p, q)
        break
