import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ls = list(map(int, input().split()))
have = dict()
have[0] = 1
summ = 0
res = 0

for i in ls:
    summ += i
    if summ - K in have:
        res += have[summ - K]

    if summ in have:
        have[summ] += 1
    else:
        have[summ] = 1

print(res)