import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def recur(cur, start, nums):
    if cur == M:
        print(*nums)
        return

    for i in range(start, N+1):
        recur(cur+1, i+1, nums+[i])

recur(0, 1, [])