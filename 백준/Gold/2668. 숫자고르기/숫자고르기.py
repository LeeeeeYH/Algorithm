input = __import__('sys').stdin.readline

N = int(input())
ls = [0] + [int(input()) for _ in range(N)]
check = [False]*(N+1)

def dfs(v, visited):
    next = ls[v]
    if next not in visited:
        if not check[next]:
            dfs(next, visited + [next])
    else:
        global res
        for i in visited[visited.index(next):]:
            res.append(i)
            check[i] = True

res = []
for i in range(1, N+1):
    if not check[i]:
        dfs(i, [i])
print(len(res))
for i in sorted(res):
    print(i)