input = __import__('sys').stdin.readline

N = int(input())
ls = sorted([list(map(int, input().split())) for _ in range(N)])
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if ls[i][1] > ls[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))