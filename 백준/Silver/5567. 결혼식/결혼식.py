from collections import deque
input = __import__('sys').stdin.readline

n = int(input())
m = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
check = [False]*(n+1)

res = 0
q = deque()
q.append([1, 0])
check[1] = True
while q:
    cur, w = q.popleft()

    for next in edges[cur]:
        if not check[next] and w < 2:
            check[next] = True
            res += 1
            q.append([next, w+1])
print(res)