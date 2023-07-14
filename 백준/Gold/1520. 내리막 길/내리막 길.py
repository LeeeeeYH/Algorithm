# import sys
# input = sys.stdin.readline
#
# dirs = [[-1,0],[0,1],[1,0],[0,-1]]
# N, M = map(int, input().split())
# board = [[10000]*(M+2) for _ in range(N+2)]
# for i in range(1, N+1):
#     line = list(map(int, input().split()))
#     board[i][1:M+1] = line
#
# res = 0
# def recur(x, y):
#     if x == N and y == M:
#         return 1
#
#     ret = 0
#     for d in dirs:
#         dx, dy = x+d[0], y+d[1]
#         if board[x][y] > board[dx][dy]:
#             ret += recur(dx, dy)
#     return ret
#
# print(recur(1, 1))


# 백트를 dp로

import sys
input = sys.stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
N, M = map(int, input().split())
board = [[10000]*(M+2)] + [[10000] + list(map(int, input().split())) + [10000] for _ in range(N)] + [[10000]*(M+2)]
dp = [[-1]*(M+2) for _ in range(N+2)]

res = 0
def recur(x, y):
    if x == N and y == M:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for d in dirs:
            dx, dy = x+d[0], y+d[1]
            if board[x][y] > board[dx][dy]:
                dp[x][y] += recur(dx, dy)
    return dp[x][y]

print(recur(1, 1))