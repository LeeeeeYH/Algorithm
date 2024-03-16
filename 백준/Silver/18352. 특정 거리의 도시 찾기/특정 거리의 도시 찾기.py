from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
N, M, K, X = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    edges[A].append(B)
check = [False]*(N+1)

res = []
q = deque()
q.append([X, 0])
check[X] = True
while q:
    cur, w = q.popleft()
    if w == K:
        res.append(cur)
        continue

    for next in edges[cur]:
        if not check[next] and w < K:
            check[next] = True
            q.append([next, w+1])

if res:
    print(*sorted(res), sep='\n')
else:
    print(-1)