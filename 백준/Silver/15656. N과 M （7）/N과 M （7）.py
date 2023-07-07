import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ls = sorted(list(map(int, input().split())))

def recur(cur, nums):
    if cur == M:
        print(*nums)
        return

    for i in range(N):
        recur(cur+1, nums+[ls[i]])

recur(0, [])