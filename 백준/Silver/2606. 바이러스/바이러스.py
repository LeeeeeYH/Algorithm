input = __import__('sys').stdin.readline

N = int(input())
M = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
check = [False]*(N+1)

def dfs(v):
    check[v] = True
    for i in edges[v]:
        if not check[i]:
            dfs(i)

dfs(1)
print(check.count(True)-1)
