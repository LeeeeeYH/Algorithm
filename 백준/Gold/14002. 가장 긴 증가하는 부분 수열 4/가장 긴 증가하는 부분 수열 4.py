input = __import__('sys').stdin.readline

N = int(input())
ls = list(map(int, input().split()))
dp = [1]*N
for i in range(1, N):
    for j in range(i):
        if ls[i] > ls[j]:
            dp[i] = max(dp[i], dp[j] + 1)

maxx = max(dp)
print(maxx)
res = []

for i in range(N-1, -1, -1):
    if maxx == dp[i]:
        res.append(ls[i])
        maxx -= 1

print(*res[::-1])