import sys
input = sys.stdin.readline

G = int(input())
res = []
for i in range(1, 50001):
    for j in range(i+1, 50002):
        sub = j*j - i*i
        if sub > G:
            break
        elif sub == G:
            res.append(j)

if res:
    print(*res, sep="\n")
else:
    print(-1)