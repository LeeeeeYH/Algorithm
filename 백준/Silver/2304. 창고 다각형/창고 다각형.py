import sys
input = sys.stdin.readline

N = int(input())
pillars = [0]*1001
for _ in range(N):
    L, H = map(int, input().split())
    pillars[L] = H

left = [0]*1001
left[0] = pillars[0]
right = [0]*1001
right[1000] = pillars[1000]

for i in range(1, 1001):
    left[i] = max(left[i-1], pillars[i])
for i in range(999, -1, -1):
    right[i] = max(right[i+1], pillars[i])

res = 0
for i in range(1001):
    res += min(left[i], right[i])
print(res)