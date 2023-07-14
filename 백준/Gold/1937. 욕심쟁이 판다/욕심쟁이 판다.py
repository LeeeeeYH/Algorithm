# import sys
# input = sys.stdin.readline
#
# CHECK = 10**6
# dirs = [[-1,0],[0,1],[1,0],[0,-1]]
# n = int(input())
# board = [[CHECK]*(n+2)] + [[CHECK] + list(map(int, input().split())) + [CHECK] for _ in range(n)] + [[CHECK]*(n+2)]
#
# def recur(x, y):
#     ret = 0
#     for d in dirs:
#         dx, dy = x+d[0], y+d[1]
#         if board[x][y] > board[dx][dy]:
#             ret = max(ret, recur(dx, dy))
#     return ret + 1
#
# res = 0
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         res = max(res, recur(i, j))
# print(res)


# 백트를 dp로

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

CHECK = 10**6
dirs = [[-1,0],[0,1],[1,0],[0,-1]]
n = int(input())
board = [[CHECK]*(n+2)] + [[CHECK] + list(map(int, input().split())) + [CHECK] for _ in range(n)] + [[CHECK]*(n+2)]
dp = [[-1]*(n+2) for _ in range(n+2)]

def recur(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 0
        for d in dirs:
            dx, dy = x+d[0], y+d[1]
            if board[x][y] > board[dx][dy]:
                dp[x][y] = max(dp[x][y], recur(dx, dy))
    return dp[x][y] + 1

res = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        res = max(res, recur(i, j))
print(res)