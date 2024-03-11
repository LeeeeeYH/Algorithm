input = __import__('sys').stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
N = int(input())
board = [list(map(int, input().rstrip())) for _ in range(N)]
check = [[False]*N for _ in range(N)]

def dfs(x, y):
    for d in dirs:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < N and 0 <= dy < N and board[dx][dy] == 1 and not check[dx][dy]:
            global cnt
            check[dx][dy] = True
            cnt += 1
            dfs(dx, dy)

res = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not check[i][j]:
            check[i][j] = True
            cnt = 1
            dfs(i, j)
            res.append(cnt)

print(len(res), *sorted(res), sep="\n")