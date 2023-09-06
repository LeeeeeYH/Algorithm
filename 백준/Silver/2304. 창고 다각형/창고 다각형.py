N = int(input())
pillars = [0]*1004

for _ in range(N):
    L, H = map(int, input().split())
    pillars[L] = H

forward = [0]*1004
backward = [0]*1004
forward[0] = pillars[0]
backward[1000] = pillars[1000]

for i in range(1, 1001): # 1 ~ 1000
    forward[i] = max(forward[i-1], pillars[i])
    backward[1000-i] = max(backward[1001-i], pillars[1000-i])

res = 0
for i in range(0, 1001): # 0 ~ 1000
    res += min(forward[i], backward[i])
print(res)