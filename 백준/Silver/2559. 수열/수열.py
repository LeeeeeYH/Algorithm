import sys
input = sys.stdin.readline

N, K = map(int, input().split())
degrees = list(map(int, input().split()))

res = pre_sum = sum(degrees[:K])
for i in range(N-K):
    pre_sum += degrees[i+K] - degrees[i]
    res = max(res, pre_sum)
print(res)