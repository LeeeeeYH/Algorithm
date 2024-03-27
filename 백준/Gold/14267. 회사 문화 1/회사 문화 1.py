import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

n, m = map(int, input().split())
child = [[] for _ in range(n+1)]
p = list(map(int, input().split()))
for i in range(1, n):
    child[p[i]].append(i+1)
comp = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    comp[a] += b

res = [0]*(n+1)
def recur(cur, prev, score):
    res[cur] = score + comp[cur]
    for i in child[cur]:
        if i != prev:
            recur(i, cur, score + comp[cur])

recur(1, -1, 0)
print(*res[1:])