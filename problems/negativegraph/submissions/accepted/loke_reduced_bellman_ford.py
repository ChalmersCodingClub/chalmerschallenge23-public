#!/usr/bin/env python3
from heapq import heappush, heappop

N, M, K, A, B = [int(x) for x in input().split()]
fullgraph = [[] for _ in range(N)]
relabel = { A: 0, B: 1 } if A != B else { A:0 }
for i in range(M):
    a,b,c = [int(x) for x in input().split()]
    fullgraph[a].append((c,b))
    if c < 0 and a not in relabel:
        relabel[a] = len(relabel)
    if c < 0 and b not in relabel:
        relabel[b] = len(relabel)

def dijkstra_avoiding_negative(start):
    pq = [(0, start)]
    dist = [1e18]*N
    dist[start] = 0
    while len(pq) > 0:
        d,i = heappop(pq)
        for c,j in fullgraph[i]:
            if d+c >= dist[j]:
                continue
            if c < 0:
                continue
            dist[j] = d+c
            heappush(pq, (d+c, j))
    for c,j in fullgraph[start]:
        dist[j] = min(dist[j], c)
    return dist

# Create reduced graph in O(K M)
# Note that RN = O(K)
RN = len(relabel)
graph = [[] for _ in range(RN)]
for i in relabel:
    dist = dijkstra_avoiding_negative(i)
    for j in relabel:
        if dist[j] == 1e18:
            continue
        graph[relabel[i]].append((dist[j], relabel[j]))

def bellman_ford():
    dist = [1e18 for _ in range(RN)]
    dist[relabel[A]] = 0
    # This loop is O(K^3)
    for _ in range(RN):
        for a in range(RN):
            if dist[a] == 1e18: continue
            for c,b in graph[a]:
                dist[b] = min(dist[b], dist[a]+c)

    for _ in range(RN):
        for a in range(RN):
            if dist[a] == 1e18: continue
            for c,b in graph[a]:
                if dist[a]+c < dist[b]:
                    dist[b] = -1e18
    if dist[relabel[B]] == 1e18:
        print("POSITIVE INFINITY")
    elif dist[relabel[B]] == -1e18:
        print("NEGATIVE INFINITY")
    else:
        print(dist[relabel[B]])

bellman_ford()
