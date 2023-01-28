#!/usr/bin/env python3

n, k = map(int, input().split())
ns = [*map(int, input().split())]
if k + 1 == n * 2:
    print(n)
else:
    print(len([*filter(lambda l: ns.count(l) == 2, set(ns))]))