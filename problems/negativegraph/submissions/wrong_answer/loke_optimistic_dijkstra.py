#!/usr/bin/env python3
from heapq import heappush, heappop

N, M, K, A, B = [int(x) for x in input().split()]
graph = [[] for _ in range(N)]
for i in range(M):
    a,b,c = [int(x) for x in input().split()]
    graph[a].append((c,b))

dist = [1e18]*N
pq = [(0,A)]
dist[A] = 0
while len(pq) > 0:
    d,i = heappop(pq)
    for c,j in graph[i]:
        if d+c >= dist[j]:
            continue
        # Incorrectly assume that reaching nodes through a cheaper route
        # than the first one means that we found a negative cycle.
        if dist[j] < 1e18:
            print("NEGATIVE INFINITY")
            exit()
        dist[j] = d+c
        heappush(pq, (d+c, j))
if dist[B] == 1e18:
    print("POSITIVE INFINITY")
else:
    print(dist[B])
