from heapq import *
input = __import__('sys').stdin.readline

MAX = 100_001
dirs = [[-1,0],[0,1],[1,0],[0,-1]]
N, M, X = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])

disX = [MAX]*(N+1)
disX[X] = 0
q = [[0, X]]
while q:
    curw, cur = heappop(q)
    if disX[cur] < curw: continue

    for next, w in edges[cur]:
        dw = curw + w
        if disX[next] > dw:
            disX[next] = dw
            heappush(q, [dw, next])

res = 0
for i in range(1, N+1):
    if i != X:
        dis = [MAX]*(N+1)
        dis[i] = 0
        q = [[0, i]]
        while q:
            curw, cur = heappop(q)
            if dis[cur] < curw: continue

            for next, w in edges[cur]:
                dw = curw + w
                if dis[next] > dw:
                    dis[next] = dw
                    heappush(q, [dw, next])

        res = max(res, dis[X] + disX[i])
print(res)