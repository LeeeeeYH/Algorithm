import sys
input = sys.stdin.readline

N, S = map(int, input().split())
ls = list(map(int, input().split()))
res = 0

def recur(cur, summ, check):
    if cur == N:
        global res
        if check and summ == S:
            res += 1
        return

    recur(cur + 1, summ + ls[cur], True)
    recur(cur + 1, summ, check)

recur(0, 0, False)
print(res)