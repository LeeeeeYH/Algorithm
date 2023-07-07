import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alp = sorted(list(map(str, input().split())))
mo = [1 if i in ['a','e','i','o','u'] else 0 for i in alp]

def recur(cur, start, ls, j, m, check): # 단계, 자음, 모음
    if cur == L:
        if j >= 2 and m >= 1:
            print(ls)
        return

    for i in range(start, C):
        if not check & 1<<i:
            recur(cur + 1, i+1, ls+alp[i], j + (1 - mo[i]), m + mo[i], check | 1<<i)

recur(0, 0, '', 0, 0, 0)