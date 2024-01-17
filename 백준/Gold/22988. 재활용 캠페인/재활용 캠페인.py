import sys
input = sys.stdin.readline

N, X = map(int, input().split())
C = sorted(map(int, input().split()))

# 풀병 거르기
l, r = 0, N-1
res = 0
for i in range(N-1, -1, -1):
    if C[i] >= X:
        r -= 1
        res += 1
    else: break

rest = r+1  # 나중에 계산할 남은병 개수

# 3개를 모으면 무조건 풀병
while l < r:
    if C[l] + C[r] >= X/2:
        l, r = l+1, r-1
        res, rest = res+1, rest-2
    else:
        l += 1

print(res + rest//3)