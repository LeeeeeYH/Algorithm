import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[0]*(M+1)] + [[0] + [int(i) for i in input().rstrip()] for _ in range(N)]
pre_board = [[0]*(M+1) for _ in range(N+1)]  # 이거 포함 바로 위로 몇개나 0인지

for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j] == 0:
            pre_board[i][j] = pre_board[i-1][j] + 1

res = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if pre_board[i][j]:  # 0인 부분이 존재
            can_h = pre_board[i][j]  # 가능한 높이
            for k in range(j+1, M+1):
                can_h = min(can_h, pre_board[i][k])
                res = max(res, can_h*(k-j+1))

print(res)