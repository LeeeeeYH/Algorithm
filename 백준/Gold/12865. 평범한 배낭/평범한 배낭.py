import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N, K = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*(K+1) for _ in range(N)]

def recur(cur, summ):
    if summ > K:
        return -100_000_001
    if cur == N:
        return 0

    if dp[cur][summ] == -1:
        dp[cur][summ] = max(recur(cur+1, summ + ls[cur][0]) + ls[cur][1], recur(cur+1, summ))
    return dp[cur][summ]

print(recur(0, 0))