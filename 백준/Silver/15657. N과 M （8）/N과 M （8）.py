import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ls = sorted(list(map(int, input().split())))

def recur(cur, start, nums):
    if cur == M:
        print(*nums)
        return

    for i in range(start, N):
        recur(cur+1, i, nums+[ls[i]])

recur(0, 0, [])