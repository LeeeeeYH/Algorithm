from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
check = [[False]*M for _ in range(N)]

res = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and not check[i][j]:
            check[i][j] = True
            q = deque([[i, j]])
            while q:
                x, y = q.popleft()
                for d in dirs:
                    dx, dy = (x + d[0])%N, (y + d[1])%M
                    if board[dx][dy] == 0 and not check[dx][dy]:
                        check[dx][dy] = True
                        q.append([dx, dy])

            res += 1

print(res)