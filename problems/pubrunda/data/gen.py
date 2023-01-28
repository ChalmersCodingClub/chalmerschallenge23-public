import sys
from random import seed, randint
import random

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

def random_name():
    s = ""
    for i in range(randint(1, 10)):
        if randint(1,2)==1:
            s += chr(randint(ord('a'), ord('z')))
        else:
            s += chr(randint(ord('A'), ord('Z')))
    return s

seed(int(cmdlinearg('seed', sys.argv[-1])))

maxtk = int(cmdlinearg('maxtk', 10000))

N = int(cmdlinearg('N'))
print(N)

names = set()

for i in range(N):
    name = random_name()
    while name in names: name = random_name()
    names.add(name)
    print(name, randint(0,maxtk), randint(1,max(1, maxtk)))
