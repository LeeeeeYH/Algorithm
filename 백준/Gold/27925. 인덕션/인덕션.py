import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().split()))
maxx = 25001
dp = [[[[maxx]*10 for _ in range(10)] for _ in range(10)] for _ in range(N)]

def recur(cur, a, b, c):
    if cur == N:
        return 0

    if dp[cur][a][b][c] == maxx:
        dp[cur][a][b][c] = min(recur(cur + 1, ls[cur], b, c) + min((a-ls[cur])%10, (ls[cur]-a)%10),
                               recur(cur + 1, a, ls[cur], c) + min((b-ls[cur])%10, (ls[cur]-b)%10),
                               recur(cur + 1, a, b, ls[cur]) + min((c-ls[cur])%10, (ls[cur]-c)%10))
    return dp[cur][a][b][c]

print(recur(0, 0, 0, 0))