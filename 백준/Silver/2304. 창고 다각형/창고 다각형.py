import sys
input = sys.stdin.readline

N = int(input())
pillars = [0] * 1002
for i in range(N):
    L, H = map(int, input().split())
    pillars[L] = H

left, right = [0]*1002, [0]*1002
for i in range(1, 1001):
    left[i] = max(left[i-1], pillars[i])
for i in range(1000, 0, -1):
    right[i] = max(right[i+1], pillars[i])

res = 0
for i in range(1, 1001):
    res += min(left[i], right[i])
print(res)