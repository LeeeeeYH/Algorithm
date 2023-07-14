# import sys
# input = sys.stdin.readline
#
# N = int(input())
# ls = [list(map(int, input().split())) for _ in range(N)]
#
# def recur(cur, bf):
#     if cur == N:
#         return 0
#
#     min_now = 10000000
#     for i in range(3):
#         if i != bf:
#             min_now = min(min_now, recur(cur + 1, i) + ls[cur][i])
#     return min_now
#
# print(recur(0, -1))


# 이 백트를 DP로 변경

import sys
input = sys.stdin.readline

N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]
CHECK = 10 ** 6
dp = [[CHECK] * 3 for i in range(N)]

def recur(cur, bf):
    if cur == N:
        return 0

    if dp[cur][bf] == CHECK:
        for i in range(3):
            if i != bf:
                dp[cur][bf] = min(dp[cur][bf], recur(cur + 1, i) + ls[cur][i])
    return dp[cur][bf]

print(recur(0, -1))