from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append([i, j, 0])

res = 0
while q:
    x, y, cnt = q.popleft()
    res = max(res, cnt)
    for d in dirs:
        dx, dy, dcnt = x+d[0], y+d[1], cnt+1
        if 0 <= dx < N and 0 <= dy < M and board[dx][dy] == 0:
            board[dx][dy] = 1
            q.append([dx, dy, dcnt])

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(-1)
            exit(0)
print(res)