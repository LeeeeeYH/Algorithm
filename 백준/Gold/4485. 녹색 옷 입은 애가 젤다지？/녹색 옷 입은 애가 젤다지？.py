from heapq import *
input = __import__('sys').stdin.readline

MAX = 987654321
dirs = [[-1,0],[0,1],[1,0],[0,-1]]
cnt = 1
while True:
    N = int(input())
    if N == 0: break

    board = [list(map(int, input().split())) for _ in range(N)]
    dis = [[MAX]*N for _ in range(N)]

    dis[0][0] = board[0][0]
    q = [[0, 0, board[0][0]]]
    while q:
        x, y, w = heappop(q)
        if dis[x][y] < w: continue

        for d in dirs:
            dx, dy = x+d[0], y+d[1]
            if 0 <= dx < N and 0 <= dy < N:
                dw = w + board[dx][dy]
                if dis[dx][dy] > dw:
                    dis[dx][dy] = dw
                    heappush(q, [dx, dy, dw])
    print(f"Problem {cnt}: {dis[N-1][N-1]}")
    cnt += 1