from heapq import *
input = __import__('sys').stdin.readline

INF = 2501
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
inboard = [list(input().rstrip()) for _ in range(N)]
board = [[0]*M for _ in range(N)]  # 0: 깨끗, 1: 쓰레기옆, 2: 쓰레기
for i in range(N):
    for j in range(M):
        if inboard[i][j] == 'g':
            board[i][j] = 2
            for d in dirs:
                dx, dy = i+d[0], j+d[1]
                if 0 <= dx < N and 0 <= dy < M and inboard[dx][dy] == '.':
                    board[dx][dy] = 1
        elif inboard[i][j] == 'S':
            sx, sy = i, j
        elif inboard[i][j] == 'F':
            ex, ey = i, j

q = [(0, board[sx][sy], sx, sy)]
dis = [[[INF, INF] for _ in range(M)] for _ in range(N)]
dis[sx][sy] = [0, board[sx][sy]]
while q:
    t, nt, x, y = heappop(q)
    if x == ex and y == ey:
        print(t, nt)
        break
    if dis[x][y][0] < t or (dis[x][y][0] == t and dis[x][y][1] < nt):
        continue

    for d in dirs:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < N and 0 <= dy < M:
            if board[dx][dy] == 2 and dis[dx][dy][0] > t+1:
                dis[dx][dy] = [t+1, nt]
                heappush(q, (t+1, nt, dx, dy))
            elif board[dx][dy] == 1 and dis[dx][dy][0] >= t and dis[dx][dy][1] > nt+1:
                dis[dx][dy] = [t, nt+1]
                heappush(q, (t, nt+1, dx, dy))
            elif board[dx][dy] == 0 and dis[dx][dy][0] > t and dis[dx][dy][1] > nt:
                dis[dx][dy] = [t, nt]
                heappush(q, (t, nt, dx, dy))