import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
parent = [0]*(N+1)

def recur(cur, prev):
    for child in edges[cur]:
        if child != prev:
            parent[child] = cur
            recur(child, cur)

recur(1, -1)
print(*parent[2:], sep='\n')