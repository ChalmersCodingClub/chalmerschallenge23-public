import sys
from random import seed, randint
import random

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

seed(int(cmdlinearg('seed', sys.argv[-1])))
N = int(cmdlinearg('N'))
K = int(cmdlinearg('K'))

print(N, K)

cards = [i//2+1 for i in range(2*N)]

print(*random.sample(cards, K))
