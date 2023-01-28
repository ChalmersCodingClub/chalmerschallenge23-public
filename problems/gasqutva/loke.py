#!/usr/bin/env python3
import resource
import sys
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
sys.setrecursionlimit(10**5)

N = int(input())
generosity = []
for i in range(N):
    generosity.append(int(input()))
graph = [[] for _ in range(N)]
for i in range(N-1):
    i,j = [int(x) for x in input().split()]
    graph[i-1].append(j-1)
    graph[j-1].append(i-1)

parent = [-1]*N
children = [[] for _ in range(N)]
def root_tree(i):
    for j in graph[i]:
        if parent[i] == j:
            continue
        parent[j] = i
        children[i].append(j)
        root_tree(j)
root_tree(0)

subtree_size = [0]*N
subtree_weight = [0]*N
def precompute(i):
    s = 0
    w = 0
    for j in children[i]:
        precompute(j)
        s += subtree_size[j]
        w += subtree_weight[j]
    subtree_size[i] = 1 + s
    subtree_weight[i] = subtree_size[i] * generosity[i] + w
precompute(0)

def solve(i, top_weight):
    bottom_weight = sum(subtree_weight[j] for j in children[i])
    ans = (bottom_weight + top_weight, i)
    for j in children[i]:
        child_top_weight = (
            (top_weight + bottom_weight - subtree_weight[j])
            + (N - subtree_size[j]) * generosity[i]
        )
        a, s = solve(j, child_top_weight)
        if a > ans[0] or (a == ans[0] and s < ans[1]):
            ans = (a,s)
    return ans

amount, student = solve(0, 0)
print(student+1)
