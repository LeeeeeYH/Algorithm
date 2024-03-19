from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

time = 0
bf = 0
while True:
    summ = sum([sum(i) for i in board])
    if summ == 0:
        print(time)
        print(bf)
        break
    bf = summ

    check = [[False]*M for _ in range(N)]
    q = deque()
    for i in range(1, N-1):
        q.append([i, 0])
        q.append([i, M-1])
        check[i][0] = check[i][M-1] = True
    for j in range(1, M-1):
        q.append([0, j])
        q.append([N-1, j])
        check[0][j] = check[N-1][j] = True

    while q:
        x, y = q.popleft()
        for d in dirs:
            dx, dy = x+d[0], y+d[1]
            if 0 <= dx < N and 0 <= dy < M and not check[dx][dy]:
                check[dx][dy] = True
                if not board[dx][dy]:
                    q.append([dx, dy])
                else:
                    board[dx][dy] = 0

    time += 1
