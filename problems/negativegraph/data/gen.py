import sys
from random import randint, seed, shuffle, random
from math import isqrt

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

# Star
# Line
# Complete
# Line with M-N random extra edges

seed(int(cmdlinearg('seed', sys.argv[-1])))

MLIM = 10**5
KLIM = 50

kind = cmdlinearg('kind', sys.argv[-2])
nmax = int(cmdlinearg('nmax', MLIM))
extraedgemax = int(cmdlinearg('extraedgemax', nmax))
kfrac = float(cmdlinearg('kfrac', 0.05))
completefrac = float(cmdlinearg('completefrac', 0.5))

N = randint(2, nmax)
A = None
if kind == "complete":
    edges = []
    N = randint(2, min(nmax, isqrt(MLIM)//2))
    for a in range(N):
        for b in range(a):
            if random() < completefrac or len(edges) < 2:
                edges.append([a,b,randint(1,10**9)])
            if random() < completefrac:
                edges.append([b,a,randint(1,10**9)])
elif kind == "oneline":
    N = randint(2, nmax//2)
    order = list(range(N))
    shuffle(order)
    A = order[0]
    edges = [[order[i], order[i+1], randint(1,10**9)] for i in range(N-1)]

    used = set(tuple(sorted((a,b))) for a,b,_ in edges)
    for i in range(randint(1, min(extraedgemax, MLIM-N))):
        a,b = randint(0,N-1),randint(0,N-1)
        while tuple(sorted((a,b))) in used:
            a,b = randint(0,N-1),randint(0,N-1)
        edges.append([a,b,randint(1,10**9)])
elif kind == "twoline":
    N = randint(2, nmax//2)
    order = list(range(N))
    shuffle(order)
    A = order[0]
    edges = [[order[i], order[i+1], randint(1,10**9)] for i in range(N-1)]

    order = list(range(N))
    shuffle(order)
    edges += [[order[i], order[i+1], randint(1,10**9)] for i in range(N-1)]

    used = set(tuple(sorted((a,b))) for a,b,_ in edges)
    for i in range(randint(1, min(extraedgemax, MLIM-len(edges)))):
        a,b = randint(0,N-1),randint(0,N-1)
        while tuple(sorted((a,b))) in used:
            a,b = randint(0,N-1),randint(0,N-1)
        edges.append([a,b,randint(1,10**9)])
else:
    assert False

M = len(edges)
K = min(randint(0, KLIM), int(M*kfrac))
if A == None:
    A = randint(0,N-1)
B = A
while A == B:
    B = randint(0,N-1)

for i in range(K):
    j = randint(0,M-1)
    while edges[j][2] < 0:
        j = randint(0,M-1)
    edges[j][2] *= -1

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
