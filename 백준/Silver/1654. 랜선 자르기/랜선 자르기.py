import sys
input = sys.stdin.readline

K, N = map(int, input().split())
ls = [int(input()) for _ in range(K)]

s, e = 1, 2**31-1
res = 0
while s <= e:
    mid = (s+e)//2
    lan = sum([i//mid for i in ls])

    if lan < N:
        e = mid-1
    else:
        res = mid
        s = mid+1
print(res)