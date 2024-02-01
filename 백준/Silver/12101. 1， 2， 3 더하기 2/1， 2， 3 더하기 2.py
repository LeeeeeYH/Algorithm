import sys
input = sys.stdin.readline

n, k = map(int, input().split())
res = [[0]]

def recur(ls, summ):
    if summ > n:
        return
    elif summ == n:
        global res
        res += [ls]
        return

    for i in range(1, 4):
        recur(ls + [i], summ+i)

recur([], 0)

if k <= len(res):
    print(*res[k], sep="+")
else:
    print(-1)