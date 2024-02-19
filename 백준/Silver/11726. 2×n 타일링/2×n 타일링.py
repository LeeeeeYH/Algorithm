# import sys
# input = sys.stdin.readline
#
# n = int(input())
#
# def recur(cur):
#     if cur > n:
#         return 0
#     elif cur == n:
#         return 1
#
#     return recur(cur+1) + recur(cur+2)
#
# print(recur(0))

import sys
sys.setrecursionlimit(10_000_000)
input = sys.stdin.readline

n = int(input())
dp = [-1]*1001

def recur(cur):
    if cur > n:
        return 0
    elif cur == n:
        return 1

    if dp[cur] == -1:
        dp[cur] = (recur(cur+1) + recur(cur+2))%10007
    return dp[cur]

print(recur(0))