# DP로 변경

import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]
dp = [-1] * N

def recur(cur):
    if cur > N:
        return -98765321
    if cur == N:
        return 0

    if dp[cur] == -1:
        dp[cur] = max(recur(cur + ls[cur][0]) + ls[cur][1], recur(cur + 1))
    return dp[cur]

print(recur(0))