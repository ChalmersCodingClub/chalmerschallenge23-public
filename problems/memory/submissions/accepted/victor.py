#!/usr/bin/env python3

n, k = map(int, input().split())
ns = sorted([*map(int, input().split())])
a = 0
for i in range(len(ns) - 1):
    if ns[i] == ns[i + 1]:
        a += 1
if a == n - 1:
    a += 1
print(a)
