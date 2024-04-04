from heapq import *
input = __import__('sys').stdin.readline

INF = 30_000_000
dirs = [[[-1, 0], [1, 0]],
        [[0, -1], [0, 1]],
        [[-1, 0], [0, 1], [1, 0], [0, -1]]]
N, M = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())
sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1
board = [list(map(int, input().split())) for _ in range(N)]

dis = [[[INF]*3 for _ in range(M)] for _ in range(N)]
dis[sx][sy][0] = 0
q = [(0, 0, sx, sy)]
while q:
    curw, k, x, y = heappop(q)
    if x == ex and y == ey:
        print(curw)
        exit(0)
    if dis[x][y][k] < curw: continue

    dk = (k+1)%3
    for d in dirs[k]:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < N and 0 <= dy < M and board[dx][dy] != -1:
            dw = curw + board[dx][dy]
            if dis[dx][dy][dk] > dw:
                dis[dx][dy][dk] = dw
                heappush(q, (dw, dk, dx, dy))

print(-1)