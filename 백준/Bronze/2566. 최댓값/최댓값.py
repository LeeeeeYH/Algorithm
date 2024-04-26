input = __import__('sys').stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
maxx = -1
for i in range(9):
    for j in range(9):
        if maxx < board[i][j]:
            maxx, x, y = board[i][j], i, j

print(maxx)
print(x+1, y+1)