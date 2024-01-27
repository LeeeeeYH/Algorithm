import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
als = sorted(map(int, input().split()))
bls = sorted(map(int, input().split()))
cls = sorted(map(int, input().split()))

def nearb(t):
    s, e = 0, B-1
    ret = bls[0]  # 가장 가까운 수
    ret_diff = abs(t-ret)
    while s <= e:
        mid = (s+e)//2
        diff = abs(bls[mid] - t)
        if t > bls[mid]:
            s = mid+1
        elif t < bls[mid]:
            e = mid-1
        else:
            return t
        if ret_diff > diff:
            ret_diff = diff
            ret = bls[mid]
    return ret

def nearc(t):
    s, e = 0, C-1
    ret = cls[0]  # 가장 가까운 수
    ret_diff = abs(t-ret)
    while s <= e:
        mid = (s+e)//2
        diff = abs(cls[mid] - t)
        if t > cls[mid]:
            s = mid+1
        elif t < cls[mid]:
            e = mid-1
        else:
            return t
        if ret_diff > diff:
            ret_diff = diff
            ret = cls[mid]
    return ret

res = 100_000_000
for a in als:
    b = nearb(a)
    c1, c2 = nearc(a), nearc(b)
    res = min(res, min(max([a,b,c1]) - min([a,b,c1]), max([a,b,c2]) - min([a,b,c2])))
print(res)