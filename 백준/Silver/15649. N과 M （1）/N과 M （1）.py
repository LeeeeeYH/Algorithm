import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def recur(cur, nums, check):
    if cur == M:
        print(*nums)
        return

    for i in range(1, N+1):
        if not check & 1<<i:
            recur(cur+1, nums+[i], check | 1<<i)

recur(0, [], 0)