from heapq import *
input = __import__('sys').stdin.readline

INF = 987654321
dirs = [[-1,0],[0,1],[1,0],[0,-1]] # 북, 동, 남, 서
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())
sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1  # 위치 재조정
conv_d = [-1, 1, 3, 2, 0]  # 1동2서3남4북 -> 0북1동2남3서로 변환
sd, ed = conv_d[sd], conv_d[ed]
dis = [[[INF]*4 for _ in range(M)] for _ in range(N)]

q = [[0, sx, sy, sd]]
dis[sx][sy][sd] = 0
while q:
    cnt, x, y, d = heappop(q)
    if x == ex and y == ey and ed == d:
        continue
    elif dis[x][y][d] < cnt: continue

    # 방향 돌리기
    for i in range(1, 4):
        dd = (d+i)%4
        ncnt = cnt + 2-abs(i-2)
        if dis[x][y][dd] > ncnt:
            dis[x][y][dd] = ncnt
            heappush(q, [ncnt, x, y, dd])

    # 앞으로 가기
    for i in range(1, 4):
        dx, dy = x + dirs[d][0]*i, y + dirs[d][1]*i
        if dx < 0 or dx >= N or dy < 0 or dy >= M: break
        ncnt = cnt+1
        if board[dx][dy] == 1: break
        if dis[dx][dy][d] > ncnt:
            dis[dx][dy][d] = ncnt
            heappush(q, [ncnt, dx, dy, d])

print(dis[ex][ey][ed])