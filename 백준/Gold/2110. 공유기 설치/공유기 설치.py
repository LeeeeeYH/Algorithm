import sys
input = sys.stdin.readline

N, C = map(int, input().split())
ls = sorted([int(input()) for _ in range(N)])

# 최소 거리를 x라고 했을때 가능한 최대 공유기의 수
def count(x):
    ret = 1
    installed = ls[0]
    for i in ls[1:]:
        if i - installed >= x:
            installed = i
            ret += 1
    return ret

s, e = 1, 1_000_000_000
res = 0

while s <= e:
    mid = (s+e)//2
    cnt = count(mid)
    if cnt >= C:
        res = mid
        s = mid+1
    else:
        e = mid-1
print(res)