import sys
from random import randint, seed, shuffle, random
from math import isqrt

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

seed(int(cmdlinearg('seed', sys.argv[-1])))

NLIM = 10**5
MLIM = 10**5

K = randint(40, 50)
N = 2*K+1
M = 3*K
A = 0
B = N-1
edges = []
for i in range(K):
    weight = max(int(2**min(K-i, 29) * randint(80,120)/100), 1)
    edges.append([2*i, 2*i+2, max(1, weight//2)])
    edges.append([2*i, 2*i+1, weight])
    edges.append([2*i+1, 2*i+2, -weight])

if True:
    Nextra = randint((NLIM-N)//5, (NLIM-N)//3)
    order = list(range(N-1, N+Nextra))
    edges += [[order[i], order[i+1], randint(1,10**3)] for i in range(Nextra)]

    shuffle(order)
    edges += [[order[i], order[i+1], randint(1,10**3)] for i in range(Nextra)]

    used = set(tuple(sorted((a,b))) for a,b,_ in edges)
    for i in range(randint(1, MLIM-len(edges))):
        a,b = randint(N,N+Nextra-1),randint(N,N+Nextra-1)
        if not tuple(sorted((a,b))) in used:
            edges.append([a,b,randint(1,10**3)])

    N += Nextra
    M = len(edges)
    B = N-1

relabel = list(range(N))
shuffle(relabel)
A = relabel[A]
B = relabel[B]
for i in range(M):
    edges[i][0] = relabel[edges[i][0]]
    edges[i][1] = relabel[edges[i][1]]
shuffle(edges)

print(N, M, K, A, B)
for a, b, c in edges:
    print(a, b, c)
