from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
check = [[False]*M for _ in range(N)]

cnt = 0
res = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not check[i][j]:
            q = deque()
            q.append([i, j])
            check[i][j] = True

            area = 1
            while q:
                x, y = q.popleft()

                for d in dirs:
                    dx, dy = x+d[0], y+d[1]
                    if 0 <= dx < N and 0 <= dy < M and board[dx][dy] == 1 and not check[dx][dy]:
                        check[dx][dy] = True
                        q.append([dx, dy])
                        area += 1

            cnt += 1
            res = max(res, area)

print(cnt, res, sep='\n')