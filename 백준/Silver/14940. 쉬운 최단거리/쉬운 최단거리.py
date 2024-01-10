import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0]*(m+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0]*(m+2)]
dis = [[-1]*(m+2) for _ in range(n+2)]
dir = [[-1,0], [0,1], [1,0], [0,-1]]

for i in range(n+2):
    for j in range(m+2):
        if board[i][j] == 0:
            dis[i][j] = 0
        if board[i][j] == 2:
            dis[i][j] = 0
            fx, fy = i, j



q = [[fx, fy, 0]]
while q:
    x, y, cnt = q.pop(0)

    for d in dir:
        dx, dy = x+d[0], y+d[1]
        if dis[dx][dy] == -1:
            dis[dx][dy] = cnt+1
            q.append([dx, dy, cnt+1])

for i in dis[1:-1]:
    print(*i[1:-1])
