import sys
input = sys.stdin.readline

N = int(input())
ls = sorted(map(int, input().split()))
M = int(input())
quest = list(map(int, input().split()))
for q in quest:
    s, e = 0, N-1
    l, r = N, 0
    found = False
    # 왼쪽 구하기
    while s <= e:
        m = (s+e)//2
        if q > ls[m]:
            s = m+1
        elif q < ls[m]:
            e = m-1
        else:
            found = True
            l = m
            e = m-1

    s, e = 0, N-1
    # 오른쪽 구하기
    while s <= e:
        m = (s+e)//2
        if q > ls[m]:
            s = m+1
        elif q < ls[m]:
            e = m-1
        else:
            r = m
            s = m+1
    print(r-l+1 if found else 0, end=" ")
