from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
q = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            q.append((board[i][j], i, j, 0))
q = deque(sorted(q))
S, X, Y = map(int, input().split())

while q:
    virus, x, y, time = q.popleft()
    if time == S:
        break

    dtime = time+1
    for d in dirs:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < N and 0 <= dy < N and not board[dx][dy]:
            board[dx][dy] = virus
            q.append((virus, dx, dy, dtime))
print(board[X-1][Y-1])