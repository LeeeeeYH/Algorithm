import sys
input = sys.stdin.readline

dir = [[-1,0],[0,1],[1,0],[0,-1]]
N, M = map(int, input().split())
dboard = [list(input().rstrip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if dboard[i][j] == 'U':
            dboard[i][j] = 0
        elif dboard[i][j] == 'R':
            dboard[i][j] = 1
        elif dboard[i][j] == 'D':
            dboard[i][j] = 2
        elif dboard[i][j] == 'L':
            dboard[i][j] = 3
board = [[0]*M for _ in range(N)]

cnt, res = 1, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            x, y = i, j
            while board[x][y] == 0:
                board[x][y] = cnt
                d = dboard[x][y]
                x, y = x+dir[d][0], y+dir[d][1]

            if board[x][y] == cnt:  # 현재 사이클 이라면
                res += 1
            cnt += 1
print(res)