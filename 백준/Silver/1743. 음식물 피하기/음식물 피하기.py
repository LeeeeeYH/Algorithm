from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
N, M, K = map(int, input().split())
board = [[False]*(M+2) for _ in range(N+2)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = True

res = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j]:
            board[i][j] = False
            cnt = 1
            q = deque()
            q.append([i, j])
            while q:
                x, y = q.popleft()

                for d in dirs:
                    dx, dy = x+d[0], y+d[1]
                    if board[dx][dy]:
                        board[dx][dy] = False
                        q.append([dx, dy])
                        cnt += 1
            res = max(res, cnt)
print(res)