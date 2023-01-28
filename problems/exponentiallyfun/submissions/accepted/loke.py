#!/usr/bin/env python3
from math import log2

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

def lowest(N):
    # DP[n] = (logsum, x%MOD)
    # of lowest solution s(x) = n
    # using the primes we have iterated through
    logsum = [1e9]*(N+1)
    xmod = [0]*(N+1)
    logsum[0], xmod[0] = 0, 1
    for p in PRIMES:
        for n in range(N+1-p):
            if logsum[n] + log2(p) < logsum[n+p]:
                logsum[n+p] = logsum[n] + log2(p)
                xmod[n+p] = (xmod[n]*p)%MOD
    return xmod[N]
print(lowest(N), highest(N))
