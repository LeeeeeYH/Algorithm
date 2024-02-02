import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    ls = [[] for _ in range(N+1)]
    degree = [0]*(N+1)
    for _ in range(K):
        a, b = map(int, input().split())
        ls[a].append(b)
        degree[b] += 1
    W = int(input())

    time = [0]*(N+1)
    q = []

    for i in range(1, N+1):
        if degree[i] == 0:
            q.append(i)
            time[i] = D[i]

    while q:
        cur = q.pop(0)
        for j in ls[cur]:
            time[j] = max(time[j], time[cur] + D[j])
            degree[j] -= 1
            if degree[j] == 0:
                q.append(j)
    print(time[W])