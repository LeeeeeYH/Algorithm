import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
sqr = [[False]*10 for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num == 0:
            zeros.append([i, j])
        else:
            row[i][num] = True
            col[j][num] = True
            sqr[i//3*3 + j//3][num] = True

zero_num = len(zeros)

def recur(cur):
    if cur == zero_num:
        for i in board:
            print(*i)
        exit(0)

    i, j = zeros[cur]
    for num in range(1, 10):
        if not row[i][num] and not col[j][num] and not sqr[i//3*3 + j//3][num]:
            row[i][num] = col[j][num] = sqr[i//3*3 + j//3][num] = True
            board[i][j] = num
            recur(cur + 1)
            row[i][num] = col[j][num] = sqr[i//3*3 + j//3][num] = False

recur(0)