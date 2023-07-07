import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def recur(cur, nums):
    if cur == M:
        print(*nums)
        return

    for i in range(1, N+1):
        recur(cur+1, nums+[i])

recur(0, [])