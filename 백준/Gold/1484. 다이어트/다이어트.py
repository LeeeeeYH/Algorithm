import sys
input = sys.stdin.readline

G = int(input())
ls = [i*i for i in range(50_002)]
res = []
for i in range(1, 50_001):
    if ls[i+1] - ls[i] > G:
        break
    for j in range(i+1, 50_002):
        diff = ls[j] - ls[i]
        if diff > G:
            break
        elif diff == G:
            res.append(j)
            break
if len(res):
    print(*res, sep="\n")
else:
    print(-1)