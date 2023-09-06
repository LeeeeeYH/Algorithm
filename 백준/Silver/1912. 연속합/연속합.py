import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
pre_sum = [0]*(n+1)
min_sum = 0
res = arr[1]

for i in range(1, n+1):
    pre_sum[i] = arr[i] + pre_sum[i-1]
    res = max(res, pre_sum[i] - min_sum)
    min_sum = min(min_sum, pre_sum[i])

print(res)