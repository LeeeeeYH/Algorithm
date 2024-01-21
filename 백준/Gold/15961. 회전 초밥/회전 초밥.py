import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
ls = [int(input()) for _ in range(N)]
ls += ls
sushi = [0]*(d+1)
sushi[c] = 1
kind = 1
for i in range(k):
    if sushi[ls[i]] == 0:
        kind += 1
    sushi[ls[i]] += 1

res = kind
for i in range(N-1):
    sushi[ls[i]] -= 1
    if sushi[ls[i]] == 0:
        kind -= 1

    if sushi[ls[i+k]] == 0:
        kind += 1
    sushi[ls[i+k]] += 1

    res = max(res, kind)

print(res)