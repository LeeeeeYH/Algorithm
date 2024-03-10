# 이걸 어떻게 dfs로..?
input = __import__('sys').stdin.readline

N, A, B = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    v, w, l = map(int, input().split())
    edges[v].append([w, l])
    edges[w].append([v, l])
check = [False]*(N+1)

q = [[A, 0, 0]]  # [vertex, 거리합, max 거리]
check[A] = True
while q:
    v, summ, maxx = q.pop(0)
    if v == B:
        print(summ - maxx)
        break

    for next, leng in edges[v]:
        if not check[next]:
            check[next] = True
            q.append([next, summ+leng, max(maxx, leng)])