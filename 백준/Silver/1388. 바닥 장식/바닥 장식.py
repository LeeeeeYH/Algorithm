input = __import__('sys').stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
check = [[False]*M for _ in range(N)]

def dfssero(x, y):
    check[x][y] = True
    dx = x + 1
    if dx < N and board[dx][y] == '|' and not check[dx][y]:
        dfssero(dx, y)

def dfsgaro(x, y):
    check[x][y] = True
    dy = y + 1
    if dy < M and board[x][dy] == '-' and not check[x][dy]:
        dfsgaro(x, dy)

res = 0
for i in range(N):
    for j in range(M):
        if not check[i][j]:
            if board[i][j] == '|':
                dfssero(i, j)
            else:
                dfsgaro(i, j)
            res += 1
print(res)