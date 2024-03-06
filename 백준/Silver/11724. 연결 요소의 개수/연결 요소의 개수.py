input = __import__('sys').stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
check = [False]*(N+1)

def dfs(v):
    for i in edges[v]:
        if not check[i]:
            check[i] = True
            dfs(i)

res = 0
for i in range(1, N+1):
    if not check[i]:
        res += 1
        check[i] = True
        dfs(i)
print(res)