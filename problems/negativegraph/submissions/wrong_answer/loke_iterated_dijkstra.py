#!/usr/bin/env python3
from heapq import heappush, heappop

N, M, K, A, B = [int(x) for x in input().split()]
graph = [[] for _ in range(N)]
for i in range(M):
    a,b,c = [int(x) for x in input().split()]
    graph[a].append((c,b))

# Dijstra from A until we meet reach node through negative edge.
# Then restart Dijstra from both A and this node, removing the negative edge.
# Restart again whenever we reach a node through a negative edge.
# We will perform at most K Dijstras.

# EDIT: This is actually incorrect. A node can be reachable through both edges (-10) and (-6, -6).
# The first edge will be taken since it has the earliest reached destination. But -6-6=-12<-10, so
# we will eventually update the distance again, leading us to think we have reached a negative cycle.

def try_dijkstra(starts):
    dist = [1e18]*N
    pq = starts[:]
    negtraversal = []
    for d,i in starts:
        dist[i] = d
    while len(pq) > 0:
        d,i = heappop(pq)
        assert dist[i] == d
        for c,j in graph[i]:
            if d+c >= dist[j]:
                continue
            if c < 0:
                heappush(negtraversal, (d+c, j))
                continue
            dist[j] = d+c
            heappush(pq, (d+c, j))
    if len(negtraversal) > 0:
        dd,j = negtraversal[0]
        for (d,i) in starts:
            if i == j:
                assert dd < d
                print("NEGATIVE INFINITY")
                exit()
        heappush(starts, negtraversal[0])
    else:
        if dist[B] == 1e18:
            print("POSITIVE INFINITY")
        else:
            print(dist[B])
        exit()

starts = [(0, A)]
while True:
    try_dijkstra(starts)
