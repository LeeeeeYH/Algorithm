import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
ls = [1] * N
for _ in range(B):
    ls[int(input()) - 1] = 0

summ = sum(ls[:K])
res = K-summ
for i in range(K, N):
    summ += ls[i] - ls[i-K]
    res = min(res, K-summ)
print(res)