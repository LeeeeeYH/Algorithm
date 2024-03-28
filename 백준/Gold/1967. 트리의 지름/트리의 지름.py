from heapq import *
input = __import__('sys').stdin.readline

INF = 1_000_001
N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

# 가장 먼 노드 구하기
dis = [INF]*(N+1)
dis[1] = 0
q = [[0, 1]]
while q:
    curw, cur = heappop(q)
    if curw > dis[cur]:
        continue

    for nxt, w in edges[cur]:
        nxtw = curw + w
        if dis[nxt] > nxtw:
            dis[nxt] = nxtw
            heappush(q, [nxtw, nxt])

firsti, first = 1, 1  # 루트에서 가장 먼 노드
for i in range(1, N+1):
    if first < dis[i]:
        first = dis[i]
        firsti = i

# 가장 먼 노드에서 가장 먼 노드 구하기
dis = [INF]*(N+1)
dis[firsti] = 0
q = [[0, firsti]]
while q:
    curw, cur = heappop(q)
    if curw > dis[cur]:
        continue

    for nxt, w in edges[cur]:
        nxtw = curw + w
        if dis[nxt] > nxtw:
            dis[nxt] = nxtw
            heappush(q, [nxtw, nxt])

print(max(dis[1:]))