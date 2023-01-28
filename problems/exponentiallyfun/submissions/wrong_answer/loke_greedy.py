#!/usr/bin/env python3
N = int(input())
assert 2 <= N <= 50_000
MOD = 10**9 + 7

def gen_primes(limit):
    isprime = [True]*limit
    isprime[0] = isprime[1] = False
    for p in range(limit):
        if isprime[p]:
            for r in range(p*p, limit, p):
                isprime[r] = False
    primes = [i for i in range(limit) if isprime[i]]
    return primes
PRIMES = gen_primes(N+1)

def highest(n):
    ret = 1
    while n % 3 != 0:
        ret = (ret * 2) % MOD
        n -= 2
    ret = (ret * pow(3, n//3, MOD)) % MOD
    return ret

def lowest(n): # (incorrect greedy)
    ret = 1
    while n > 0:
        if n == 6:
            ret = (ret * 2*2*2) % MOD
            n -= 6
            continue
        from bisect import bisect_right
        p_i = bisect_right(PRIMES, n) - 1
        p = PRIMES[p_i]
        assert p_i+1 == len(PRIMES) or p <= n < PRIMES[p_i+1]
        if n - p == 1:
            p_i -= 1
            p = PRIMES[p_i]
        ret = (ret * p) % MOD
        n -= p
    return ret
print(lowest(N), highest(N))
