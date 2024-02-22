input = __import__('sys').stdin.readline

board = [list(input().rstrip()) for _ in range(8)]
res = 0
for i in range(8):
    for j in range(8):
        if not (i+j)%2 and board[i][j] == 'F':
            res += 1
print(res)