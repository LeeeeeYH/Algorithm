import sys
input = sys.stdin.readline

N = int(input())
ls = sorted(map(int, input().split()))
M = int(input())
quest = list(map(int, input().split()))
for q in quest:
    s, e = 0, N-1
    res = 0
    while s <= e:
        m = (s+e)//2
        if q > ls[m]:
            s = m+1
        elif q < ls[m]:
            e = m-1
        else:
            res = 1
            break
    print(res, end=" ")