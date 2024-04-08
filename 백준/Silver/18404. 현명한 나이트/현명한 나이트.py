from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
N, M = map(int, input().split())
X, Y = map(int, input().split())
board = [[-1]*N for _ in range(N)]

q = deque([[X-1, Y-1, 0]])
board[X-1][Y-1] = 0
for _ in range(M):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    if board[A][B] == -1:
        while q:
            x, y, dis = q.popleft()
            if x == A and y == B:
                print(board[x][y], end=' ')
                break

            ddis = dis+1
            for d in dirs:
                dx, dy = x + d[0], y + d[1]
                if 0 <= dx < N and 0 <= dy < N and board[dx][dy] == -1:
                    board[dx][dy] = ddis
                    q.append([dx, dy, ddis])
    else:
        print(board[A][B], end=' ')