import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = [0] * M

def recur(cur, start, check):
    if cur == M:
        print(*num)
        return

    for i in range(start, N+1):
        if not check & (1<<i):
            num[cur] = i
            recur(cur+1, i + 1, check|1<<i)

recur(0, 1, 0)