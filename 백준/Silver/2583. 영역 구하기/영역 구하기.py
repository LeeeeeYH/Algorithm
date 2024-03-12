input = __import__('sys').stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
M, N, K = map(int, input().split())
board = [[False]*M for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = True

res = []
for i in range(N):
    for j in range(M):
        if not board[i][j]:
            board[i][j] = True
            q = [[i, j]]
            area = 1
            while q:
                x, y = q.pop(0)
                for d in dirs:
                    dx, dy = x+d[0], y+d[1]
                    if 0 <= dx < N and 0 <= dy < M and not board[dx][dy]:
                        board[dx][dy] = True
                        q.append([dx, dy])
                        area += 1
            res.append(area)

print(len(res))
print(*sorted(res))