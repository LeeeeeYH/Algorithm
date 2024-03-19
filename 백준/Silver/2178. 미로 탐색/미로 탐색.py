from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
N, M = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
check = [[False]*M for _ in range(N)]
N, M = N-1, M-1

q = deque()
q.append([0, 0, 1])
check[0][0] = True
while q:
    x, y, cnt = q.popleft()
    if x == N and y == M:
        print(cnt)
        break

    for d in dirs:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx <= N and 0 <= dy <= M and board[dx][dy] and not check[dx][dy]:
            check[dx][dy] = True
            q.append([dx, dy, cnt+1])