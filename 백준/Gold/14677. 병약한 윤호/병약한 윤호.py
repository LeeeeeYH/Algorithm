import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

bld = ['D', 'L', 'B']  # 3으로 나눴을때 나머지가 아점저에 해당
N = int(input())
ls = list(input().rstrip())
dp = [[-1]*1501 for _ in range(1501)]

def recur(l, r):
    if l > r:
        return 0

    state = (r-l) % 3
    if dp[l][r] == -1:
        dp[l][r] = 0
        if bld[state] == ls[l]:
            dp[l][r] = max(dp[l][r], recur(l+1, r) + 1)
        if bld[state] == ls[r]:
            dp[l][r] = max(dp[l][r], recur(l, r-1) + 1)
    return dp[l][r]

print(recur(0, 3*N - 1))