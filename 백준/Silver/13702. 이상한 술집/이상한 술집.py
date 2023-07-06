import sys
input = sys.stdin.readline

N, K = map(int, input().split())
pots = [int(input()) for _ in range(N)]

i, j = 0, 2**31 - 1
res = 0
while i <= j:
    mid = (i + j)//2
    cnt = 0
    for pot in pots:
        cnt += pot//mid

    if cnt >= K:
        i = mid + 1
        res = mid
    else:
        j = mid - 1
print(res)