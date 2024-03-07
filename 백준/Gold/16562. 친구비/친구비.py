import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

N, M, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
edges = [[] for _ in range(N+1)]
for _ in range(M):
    v, w = map(int, input().split())
    edges[v].append(w)
    edges[w].append(v)

check = [False]*(N+1)
groups = []

def dfs(v):
    check[v] = True
    global gnum
    groups[gnum].append(v)
    for i in edges[v]:
        if not check[i]:
            dfs(i)

gnum = 0
for i in range(1, N+1):
    if not check[i]:
        groups.append([])
        dfs(i)
        gnum += 1

for i in range(1, N+1):
    if not check[i]:
        print("Oh no")
        break
else:
    res = 0
    for group in groups:
        res += min([A[x] for x in group])
    print(res if res <= k else "Oh no")