#!/usr/bin/env python3

import sys
import random

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

random.seed(int(cmdlinearg('seed', sys.argv[-1])))
n = int(cmdlinearg('n'))
k = int(cmdlinearg('k'))
max_h = int(cmdlinearg('hMax'))

print(n, k)

a = [1]*k
for i in range(n-k):
    a[random.randrange(0, k)] += 1

print(*a)

for i in range(n):
    print(*[random.randint(1, max_h) for j in range(k)])
