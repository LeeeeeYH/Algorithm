import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (N+1)
def recur(cur, parent):
    for child in tree[cur]:
        if child != parent:
            parents[child] = cur
            recur(child, cur)

recur(1, 0)
for i in parents[2:]:
    print(i)