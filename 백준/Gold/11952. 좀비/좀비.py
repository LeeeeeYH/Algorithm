from collections import deque
from heapq import *
input = __import__('sys').stdin.readline

INF = 20_000_000_001
N, M, K, S = map(int, input().split())
pq = list(map(int, input().split()))
zombies = [int(input()) for _ in range(K)]
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

cities = [0]*(N+1)  # 0: 안전한 도시, 1: 위험한 도시, 2: 좀비점령 도시
# 위험한 도시 체크
q = deque()
for z in zombies:
    cities[z] = 2
    q.append([z, 0])
while q:
    cur, leng = q.popleft()
    if leng < S:
        for nxt in edges[cur]:
            if cities[nxt] == 0:
                cities[nxt] = 1
                q.append([nxt, leng + 1])

# 다익스트라
q = [[1, 0]]
dis = [INF]*(N+1)
dis[1] = 0
while q:
    cur, w = heappop(q)
    if cur == N:
        print(w-pq[cities[cur]])
        break
    if dis[cur] < w: continue

    for nxt in edges[cur]:
        if cities[nxt] == 2:
            continue
        else:
            dw = w + pq[cities[nxt]]
            if dis[nxt] > dw:
                dis[nxt] = dw
                heappush(q, [nxt, dw])
