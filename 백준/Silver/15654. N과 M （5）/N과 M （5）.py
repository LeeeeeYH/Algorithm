import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ls = sorted(list(map(int, input().split())))

def recur(cur, nums, check):
    if cur == M:
        print(*nums)
        return

    for i in range(N):
        if not check & 1<<i:
            recur(cur+1, nums+[ls[i]], check | 1<<i)

recur(0, [], 0)