from heapq import *
input = __import__('sys').stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
MAX = 10001
M, N = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dis = [[MAX]*M for _ in range(N)]

q = []
heappush(q, [0, 0, 0])
dis[0][0] = 0
while q:
    x, y, w = heappop(q)

    if dis[x][y] < w: continue

    for d in dirs:
        dx, dy = x + d[0], y + d[1]
        if 0 <= dx < N and 0 <= dy < M:
            dw = w + board[dx][dy]
            if dis[dx][dy] > dw:
                heappush(q, [dx, dy, dw])
                dis[dx][dy] = dw

print(dis[N-1][M-1])