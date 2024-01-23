import sys
input = sys.stdin.readline

N, S = map(int, input().split())
ls = list(map(int, input().split()))

i, summ = 0, 0
res = N+1
for j in range(N):
    summ += ls[j]
    while i <= j:
        if summ >= S:
            res = min(res, j-i+1)
            summ -= ls[i]
            i += 1
        else:
            break

print(res if res != N+1 else 0)