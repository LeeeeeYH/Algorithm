import heapq
input = __import__('sys').stdin.readline

V, E = map(int, input().split())
K = int(input())
edges = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append([w, v])

dis = [987654321] * (V+1)
dis[K] = 0
q = []
heapq.heappush(q, [0, K])
while q:
    curw, cur = heapq.heappop(q)

    if curw > dis[cur]:
        continue
    for w, next in edges[cur]:
        nextw = curw + w
        if dis[next] > nextw:
            dis[next] = nextw
            heapq.heappush(q, [nextw, next])

for i in range(1, V+1):
    print(dis[i] if dis[i] != 987654321 else "INF")