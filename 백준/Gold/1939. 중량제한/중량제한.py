from collections import deque
input = __import__('sys').stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edges[A].append([B, C])
    edges[B].append([A, C])
f1, f2 = map(int, input().split())

s, e = 1, 1_000_000_000
res = 1
while s <= e:
    mid = (s+e)//2
    can = False

    q = deque()
    q.append(f1)
    check = [False]*(N+1)
    check[f1] = True
    while q:
        cur = q.popleft()
        if cur == f2:
            can = True
            break

        for next, limit in edges[cur]:
            if not check[next] and mid <= limit:
                check[next] = True
                q.append(next)

    if can:
        res = max(res, mid)
        s = mid + 1
    else:
        e = mid - 1
print(res)