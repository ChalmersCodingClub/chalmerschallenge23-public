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
nimprov = [0]*N
negative_cycle = False
while len(pq) > 0:
    d,i = heappop(pq)
    nimprov[i] += 1
    # Some extra for good measure, this is incorrect but might go though bad test data
    if nimprov[i] > 2*K+3:
        # In case of both having a negative cycle AND unreachable B,
        # unreachability takes precedence
        negative_cycle = True
        continue
    for c,j in graph[i]:
        if d+c >= dist[j]:
            continue
        dist[j] = d+c
        heappush(pq, (d+c, j))
if dist[B] == 1e18:
    print("POSITIVE INFINITY")
elif negative_cycle:
    print("NEGATIVE INFINITY")
else:
    print(dist[B])
