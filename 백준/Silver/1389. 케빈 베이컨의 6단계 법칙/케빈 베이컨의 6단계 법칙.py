from heapq import *
input = __import__('sys').stdin.readline

MAX = 10001
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

res, resi = MAX, 0
for i in range(1, N+1):
    dis = [MAX]*(N+1)
    q = [[0, i]]
    dis[i] = 0
    while q:
        curw, cur = heappop(q)
        if dis[cur] < curw: continue

        for next in edges[cur]:
            if dis[next] > curw+1:
                dis[next] = curw+1
                heappush(q, [curw+1, next])

    summ = sum(dis[1:])
    if res > summ:
        res = summ
        resi = i
print(resi)