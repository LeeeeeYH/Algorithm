input = __import__('sys').stdin.readline

n = int(input())
resx, resy = map(int, input().split())
m = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)
check = [False]*(n+1)

def dfs(v, chon):
    if v == resy:
        print(chon)
        exit(0)

    check[v] = True
    for i in edges[v]:
        if not check[i]:
            dfs(i, chon+1)

dfs(resx, 0)
print(-1)