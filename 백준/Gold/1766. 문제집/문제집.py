import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
degree = [0]*(N+1)
ls = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    ls[a].append(b)
    degree[b] += 1

res = []
q = []

for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(q, i)

while q:
    cur = heapq.heappop(q)
    res.append(cur)

    for i in ls[cur]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(q, i)

print(*res)