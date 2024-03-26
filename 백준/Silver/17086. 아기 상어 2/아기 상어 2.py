from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


res = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            check = [[False]*M for _ in range(N)]
            check[i][j] = True
            q = deque()
            q.append([i, j, 0])
            found = False
            while not found:
                x, y, cnt = q.popleft()

                dcnt = cnt+1
                for d in dirs:
                    dx, dy = x+d[0], y+d[1]
                    if 0 <= dx < N and 0 <= dy < M and not check[dx][dy]:
                        check[dx][dy] = True
                        if board[dx][dy] == 0:
                            q.append([dx, dy, dcnt])
                        else:
                            res = max(res, cnt + 1)
                            found = True
                            break
print(res)