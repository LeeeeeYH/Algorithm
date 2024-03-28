input = __import__('sys').stdin.readline
from collections import deque

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0]*(N+1)
# def find_parent(cur, prev):
#     for child in tree[cur]:
#         if child != prev:
#             parent[child] = cur
#             find_parent(child, cur)
# find_parent(1, 0)

# bfs로 변경
q = deque()
q.append(1)
while q:
    cur = q.popleft()
    for child in tree[cur]:
        if parent[cur] != child:
            parent[child] = cur
            q.append(child)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    check = [False]*(N+1)
    while a != 0:
        check[a] = True
        a = parent[a]

    while not check[b]:
        b = parent[b]
    print(b)