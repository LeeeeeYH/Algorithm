import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
pre_board = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        pre_board[i][j] = board[i][j] + pre_board[i - 1][j] + pre_board[i][j - 1] - pre_board[i - 1][j - 1]

res = -400000000
for i1 in range(1, N + 1):
    for j1 in range(1, M + 1):
        for i2 in range(i1):
            for j2 in range(j1):
                res = max(res, pre_board[i1][j1] - pre_board[i2][j1] - pre_board[i1][j2] + pre_board[i2][j2])

print(res)