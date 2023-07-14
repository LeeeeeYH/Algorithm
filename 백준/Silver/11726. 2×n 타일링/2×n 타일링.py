# import sys
# input = sys.stdin.readline
#
# n = int(input())
#
# def recur(cur):
#     if cur > n:
#         return 0
#     if cur == n:
#         return 1
#
#     return recur(cur+1) + recur(cur+2)
#
# print(recur(0) % 10007)


# 백트를 dp로

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
dp = [-1] * n

def recur(cur):
    if cur > n:
        return 0
    if cur == n:
        return 1

    if dp[cur] == -1:
        dp[cur] = recur(cur+1) + recur(cur+2)
    return dp[cur]

print(recur(0) % 10007)