import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

N = int(input())
ls = list(map(int, input().split()))
dp = [[-1]*2001 for _ in range(2001)]

def recur(l, r):
    if l > r:
        return 0

    days = N-(r-l)
    if dp[l][r] == -1:
        dp[l][r] = max(dp[l][r], recur(l+1, r) + days*ls[l], recur(l, r-1) + days*ls[r])
    return dp[l][r]

print(recur(0, N-1))