import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().split()))

s, e = 1, 300000
res = 0

def check(x):
    can = 0
    for i in ls:
        if i >= x:
            can += 1
            if can == x:
                return True
        else:
            can = 0
    return False


while s <= e:
    mid = (s+e)//2

    if check(mid):
        s = mid + 1
        res = max(res, mid)
    else:
        e = mid - 1
print(res)