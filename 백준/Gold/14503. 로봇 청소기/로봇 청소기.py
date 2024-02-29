input = __import__('sys').stdin.readline

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
check = [[False]*M for _ in range(N)]
res = 0

while True:
    if not check[x][y]:
        check[x][y] = True
        res += 1

    for i in range(1,5):
        dd = (d-i) % 4
        dx, dy = x + dir[dd][0], y + dir[dd][1]
        if not check[dx][dy] and board[dx][dy] == 0:
            x, y, d = dx, dy, dd
            break
    else:
        dd = (d-2) % 4
        dx, dy = x + dir[dd][0], y + dir[dd][1]
        if board[dx][dy] == 0:
            x, y = dx, dy
        else:
            break

print(res)
