import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*3 for _ in range(N)]

def recur(cur, bf):
    if cur == N:
        return 0

    if dp[cur][bf] == -1:
        ret = 1_000_000
        for i in range(3):
            if i != bf:
                ret = min(ret, recur(cur+1, i) + ls[cur][i])
        dp[cur][bf] = ret
    return dp[cur][bf]

print(recur(0, -1))