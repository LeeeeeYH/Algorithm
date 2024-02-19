import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

N = int(input())
N = N-1
*ls, res = list(map(int, input().split()))
dp = [[-1]*21 for _ in range(101)]

def recur(cur, num):
    if num < 0 or num > 20:
        return 0
    if cur == N:
        if num == res:
            return 1
        return 0

    if dp[cur][num] == -1:
        dp[cur][num] = recur(cur+1, num+ls[cur]) + recur(cur+1, num-ls[cur])
    return dp[cur][num]

print(recur(1, ls[0]))