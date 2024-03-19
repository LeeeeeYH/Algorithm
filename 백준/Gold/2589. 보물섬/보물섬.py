from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
N, M = map(int, input().split())
boardin = [list(input().rstrip()) for _ in range(N)]
board = [[False]*(M+2) for _ in range(N+2)]
for i in range(N):
    for j in range(M):
        if boardin[i][j] == 'L':
            board[i+1][j+1] = True

res = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j]:
            check = [[False]*(M+1) for _ in range(N+1)]

            q = deque()
            q.append([i, j, 0])
            check[i][j] = True
            while q:
                x, y, cnt = q.popleft()
                res = max(res, cnt)

                for d in dirs:
                    dx, dy, dcnt = x+d[0], y+d[1], cnt+1
                    if board[dx][dy] and not check[dx][dy]:
                        check[dx][dy] = True
                        q.append([dx, dy, dcnt])
print(res)