import sys
from random import randint, seed
import random

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

seed(int(cmdlinearg('seed', sys.argv[-1])))

N = int(cmdlinearg('N'))
type = cmdlinearg('type')
assert type in ['rnd', 'star', 'line', 'starline']

print(N)
print(*[randint(0,10**9) for _ in range(N)], sep="\n")

adj = []
for i in range(1, N):
    if type=='rnd':
        nb = randint(0,i-1)
    if type=='star':
        nb = 0
        if randint(0,1000)==0:
            nb = randint(0,i-1)
    if type=='line':
        nb = i-1
        while randint(0,100)==0:
            nb = max(0,nb-1)
    if type=='starline':
        if i<N//2:
            nb=0
        else:
            nb=i-1
    adj.append([i, nb])
    random.shuffle(adj[-1])
random.shuffle(adj)

rename = list(range(N))
random.shuffle(rename)

for u,v in adj:
    print(rename[u]+1, rename[v]+1)
