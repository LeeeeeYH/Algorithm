from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
check = [[False]*M for _ in range(N)]
reso, resv = 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] != '#' and not check[i][j]:
            check[i][j] = True
            o, v = 0, 0  # 양, 늑대
            q = deque([[i, j]])
            while q:
                x, y = q.popleft()
                if board[x][y] == 'o':
                    o += 1
                elif board[x][y] == 'v':
                    v += 1

                for d in dirs:
                    dx, dy = x + d[0], y + d[1]
                    if 0 <= dx < N and 0 <= dy < M and not check[dx][dy] and board[dx][dy] != '#':
                        check[dx][dy] = True
                        q.append([dx, dy])

            if o > v:
                reso += o
            else:
                resv += v

print(reso, resv)