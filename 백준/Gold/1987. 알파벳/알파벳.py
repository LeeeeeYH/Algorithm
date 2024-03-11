input = __import__('sys').stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
X, Y = map(int, input().split())
board = [list(input().rstrip()) for _ in range(X)]
for i in range(X):
    for j in range(Y):
        board[i][j] = ord(board[i][j])-65
check = [False]*26
res = 0

def dfs(x, y, cnt):
    global res
    res = max(res, cnt)

    for d in dirs:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < X and 0 <= dy < Y:
            c = board[dx][dy]
            if not check[c]:
                check[c] = True
                dfs(dx, dy, cnt+1)
                check[c] = False

check[board[0][0]] = True
dfs(0, 0, 1)
print(res)