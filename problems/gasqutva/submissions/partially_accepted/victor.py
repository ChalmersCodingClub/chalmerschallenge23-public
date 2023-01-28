#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

n = int(input())
sums = [int(input()) for _ in range(n)]
graph = {}
for _ in range(n - 1):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    if i in graph:
        graph[i].add(j)
    else:
        graph[i] = set([j])
    if j in graph:
        graph[j].add(i)
    else:
        graph[j] = set([i])

v = set()
def susdfs(node, amount):
    if node in v:
        return 0
    v.add(node)
    s = 0
    for i in graph[node]:
        s += susdfs(i, sums[i] + amount)

    return amount + s

best = 0
student = -1

for i in range(n):
    v = set()
    a = susdfs(i, 100)
    if best < a:
        best = a
        student = i
print(student + 1)

