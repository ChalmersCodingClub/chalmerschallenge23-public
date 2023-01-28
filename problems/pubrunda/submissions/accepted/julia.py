#!/usr/bin/env python3
N = int(input())

bestpub = ""
time = 0

for i in range(N):
    p,k,t = input().split()
    k = int(k)
    t = int(t)
    if (k + 1) * t > time:
        time = (k + 1) * t
        bestpub = p

print(bestpub, time)
