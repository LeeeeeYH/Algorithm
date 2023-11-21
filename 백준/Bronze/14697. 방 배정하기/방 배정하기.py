import sys
input = sys.stdin.readline

A, B, C, N = map(int, input().split())
visited = [False] * (N+1)

def recur(num):
    if num == 0:
        print(1)
        exit(0)

    for i in [A, B, C]:
        next = num - i
        if next >= 0 and not visited[next]:
            visited[next] = True
            recur(next)

recur(N)
print(0)