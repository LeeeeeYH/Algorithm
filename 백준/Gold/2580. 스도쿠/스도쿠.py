import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
rows, cols, sqrs = [[False]*10 for _ in range(9)], [[False]*10 for _ in range(9)], [[False]*10 for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num == 0:
            zeros.append([i, j])
        else:
            rows[i][num], cols[j][num], sqrs[i // 3 * 3 + j // 3][num] = True, True, True
leng = len(zeros)

def recur(cur):
    if cur == leng:
        for line in board:
            print(*line)
        exit(0)

    x, y = zeros[cur]
    sqridx = x//3*3 + y//3
    for num in range(1, 10):
        if not rows[x][num] and not cols[y][num] and not sqrs[sqridx][num]:
            rows[x][num], cols[y][num], sqrs[sqridx][num] = True, True, True
            board[x][y] = num
            recur(cur+1)
            rows[x][num], cols[y][num], sqrs[sqridx][num] = False, False, False

recur(0)