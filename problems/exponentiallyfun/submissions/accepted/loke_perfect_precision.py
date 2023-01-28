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

def lowest(N):
    # DP[n] = x is the smallest x solving `s(x) = n`
    # using the primes we have iterated through
    DP = [-1]*(N+1)
    DP[0] = 1
    for p in PRIMES:
        for n in range(N+1-p):
            if DP[n] == -1:
                continue
            cand = DP[n]*p
            if DP[n+p] == -1 or DP[n+p] > cand:
                DP[n+p] = cand
    return DP[N] % MOD
print(lowest(N), highest(N))
