from collections import deque
input = __import__('sys').stdin.readline

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
check = [[False]*M for _ in range(N)]
q = deque()  # [x, y, time, 지훈이이다
for i in range(N):
    for j in range(M):
        if board[i][j] == 'J':
            q.append((i, j, 0, True))
            check[i][j] = True
        elif board[i][j] == 'F':
            q.appendleft((i, j, 0, False))
            board[i][j] = '#'

while q:
    x, y, time, jihun = q.popleft()
    if jihun and (x == 0 or x == N-1 or y == 0 or y == M-1):
        print(time+1)
        exit(0)

    for d in dirs:
        dx, dy = x + d[0], y + d[1]
        if 0 <= dx < N and 0 <= dy < M:
            if jihun and not check[dx][dy] and board[dx][dy] == '.':
                check[dx][dy] = True
                q.append((dx, dy, time+1, jihun))
            if not jihun and board[dx][dy] == '.':
                board[dx][dy] = '#'
                q.append((dx, dy, time+1, jihun))
print("IMPOSSIBLE")