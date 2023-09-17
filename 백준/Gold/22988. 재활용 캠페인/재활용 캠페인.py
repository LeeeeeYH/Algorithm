import sys
input = sys.stdin.readline

N, X = map(int, input().split())
Ci = sorted(map(int, input().split()))

l, r = 0, N-1
cnt = 0
for i in range(N-1, -1, -1):
    if Ci[i] >= X:
        r -= 1
        cnt += 1
    else:
        break
rest = r+1

while l < r:
    if Ci[l] + Ci[r] >= X/2:
        l += 1
        r -= 1
        rest -= 2
        cnt += 1
    else:
        l += 1

print(cnt + rest//3)