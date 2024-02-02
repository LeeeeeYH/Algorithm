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
        q.append(i)

while q:
    cur = q.pop(0)
    res.append(cur)

    for j in ls[cur]:
        degree[j] -= 1
        if degree[j] == 0:
            q.append(j)

print(*res)