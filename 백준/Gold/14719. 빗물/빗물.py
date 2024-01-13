import sys
input = sys.stdin.readline

H, W = map(int, input().split())
ls = list(map(int, input().split()))

left, right = [ls[0]] + [0]*(W-1), [0]*(W-1) + [ls[W-1]]
for i in range(1, W):
    left[i] = max(left[i-1], ls[i])
for i in range(W-2, -1, -1):
    right[i] = max(right[i+1], ls[i])

res = 0
for i in range(W):
    res += min(left[i], right[i]) - ls[i]
print(res)