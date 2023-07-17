# import sys
# sys.setrecursionlimit(10**7)
# input = sys.stdin.readline
#
# T = int(input())
#
# for _ in range(T):
#     n = int(input())
#     def recur(cur):
#         if cur > n:
#             return 0
#         elif cur == n:
#             return 1
#
#         return recur(cur+1) + recur(cur+2) + recur(cur+3)
#
#     print(recur(0))


# 백트를 dp로

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dp = [-1] * (n+1)
    def recur(cur):
        if cur > n:
            return 0
        elif cur == n:
            return 1

        if dp[cur] == -1:
            dp[cur] = recur(cur+1) + recur(cur+2) + recur(cur+3)
        return dp[cur]

    print(recur(0))