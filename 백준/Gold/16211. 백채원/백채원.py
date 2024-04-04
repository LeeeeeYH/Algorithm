from collections import deque
from heapq import *
input = __import__('sys').stdin.readline

INF = 5_000_000_001
N, M, K = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, T = map(int, input().split())
    edges[A].append([B, T])
    edges[B].append([A, T])
fans = list(map(int, input().split()))

min_fan = [INF]*(N+1)  # 모든 추종자 중 도달할 수 있는 최소 시간
q = []
for fan in fans:
    q.append([0, fan])
    min_fan[fan] = 0
while q:
    curw, cur = heappop(q)
    if min_fan[cur] < curw: continue

    for nxt, w in edges[cur]:
        dw = curw + w
        if min_fan[nxt] > dw:
            min_fan[nxt] = dw
            heappush(q, [dw, nxt])

dis = [INF]*(N+1)  # 백채원이 도달할 최소시간
dis[1] = 0
q = []
heappush(q, [0, 1])
while q:
    curw, cur = heappop(q)
    if dis[cur] < curw: continue

    for nxt, w in edges[cur]:
        dw = curw + w
        if dis[nxt] > dw:
            dis[nxt] = dw
            heappush(q, [dw, nxt])

res = [i for i in range(2, N+1) if min_fan[i] > dis[i]]
if res:
    print(*res)
else:
    print(0)