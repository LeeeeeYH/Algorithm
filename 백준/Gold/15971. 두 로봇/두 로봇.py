import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

N, A, B = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    v, w, l = map(int, input().split())
    edges[v].append([w, l])
    edges[w].append([v, l])

def dfs(v, bf, summ, maxx):
    if v == B:
        print(summ - maxx)
        exit(0)

    for next, leng in edges[v]:
        if next != bf:
            dfs(next, v, summ+leng, max(maxx, leng))

dfs(A, -1, 0, 0)