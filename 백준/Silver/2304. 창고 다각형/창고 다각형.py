import sys
input = sys.stdin.readline

N = int(input())
pillars = [0] * 1001
for i in range(N):
    L, H = map(int, input().split())
    pillars[L] = H

left, right = [0]*1001, [0]*1001
left[1], right[1000] = pillars[1], pillars[1000]
for i in range(2, 1001):
    left[i] = max(left[i-1], pillars[i])
    right[1001-i] = max(right[1002-i], pillars[1001-i])

res = 0
for i in range(1, 1001):
    res += min(left[i], right[i])

print(res)