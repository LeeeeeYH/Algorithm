from heapq import *
input = __import__('sys').stdin.readline
INF = 987654321

N, E = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append([c, b])
    edges[b].append([c, a])
v1, v2 = map(int, input().split())
dis1, dis2, dis3 = [INF]*(N+1), [INF]*(N+1), [INF]*(N+1)

q = [[0, 1]]
dis1[1] = 0
while q:
    curw, cur = heappop(q)
    if curw > dis1[cur]:
        continue

    for w, next in edges[cur]:
        nextw = curw + w
        if dis1[next] > nextw:
            dis1[next] = nextw
            heappush(q, [nextw, next])
q = [[0, v1]]
dis2[v1] = 0
while q:
    curw, cur = heappop(q)
    if curw > dis2[cur]:
        continue

    for w, next in edges[cur]:
        nextw = curw + w
        if dis2[next] > nextw:
            dis2[next] = nextw
            heappush(q, [nextw, next])
q = [[0, v2]]
dis3[v2] = 0
while q:
    curw, cur = heappop(q)
    if curw > dis3[cur]:
        continue

    for w, next in edges[cur]:
        nextw = curw + w
        if dis3[next] > nextw:
            dis3[next] = nextw
            heappush(q, [nextw, next])

res1, res2 = dis1[v1] + dis2[v2] + dis3[N], dis1[v2] + dis3[v1] + dis2[N]
if res1 >= INF or res2 >= INF:
    print(-1)
else:
    print(min(res1, res2))