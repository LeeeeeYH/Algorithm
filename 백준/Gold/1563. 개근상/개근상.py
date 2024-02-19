# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# def recur(cur, l, a):
#     if cur == N:
#         return 1
#
#     ret = recur(cur+1, l, 0)
#     if l < 1:
#         ret += recur(cur+1, l+1, 0)
#     if a < 2:
#         ret += recur(cur+1, l, a+1)
#     return ret
#
# print(recur(0, 0, 0))

import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())
dp = [[[-1]*3 for _ in range(2)] for _ in range(N)]

def recur(cur, l, a):
    if cur == N:
        return 1

    if dp[cur][l][a] == -1:
        dp[cur][l][a] = recur(cur+1, l, 0)
        if l < 1:
            dp[cur][l][a] += recur(cur+1, l+1, 0)
        if a < 2:
            dp[cur][l][a] += recur(cur+1, l, a+1)
    return dp[cur][l][a]

print(recur(0, 0, 0) % 1_000_000)