import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

counts = [1] * (N+1)

def count_subtree(cur, parent):
    for child in edges[cur]:
        if parent != child:
            count_subtree(child, cur)
            counts[cur] += counts[child]

count_subtree(R, 0)

for _ in range(Q):
    print(counts[int(input())])