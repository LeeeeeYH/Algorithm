input = __import__('sys').stdin.readline
from collections import deque

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
x, y, curd = 0, 0, 1
dice = [1, 2, 3, 4, 5, 6]

def move(d):
    bf = dice[:]
    if d == 0:  # 북
        dice[0] = bf[4]
        dice[1] = bf[0]
        dice[2] = bf[2]
        dice[3] = bf[3]
        dice[4] = bf[5]
        dice[5] = bf[1]
    elif d == 1:  # 동
        dice[0] = bf[3]
        dice[1] = bf[1]
        dice[2] = bf[0]
        dice[3] = bf[5]
        dice[4] = bf[4]
        dice[5] = bf[2]
    elif d == 2:  # 남
        dice[0] = bf[1]
        dice[1] = bf[5]
        dice[2] = bf[2]
        dice[3] = bf[3]
        dice[4] = bf[0]
        dice[5] = bf[4]
    else:  # d == 3:  # 서
        dice[0] = bf[2]
        dice[1] = bf[1]
        dice[2] = bf[5]
        dice[3] = bf[0]
        dice[4] = bf[4]
        dice[5] = bf[3]

res = 0
for _ in range(K):
    x, y = x + dirs[curd][0], y + dirs[curd][1]
    if   x < 0: x, curd = 1, 2
    elif x >= N:x, curd = N-2, 0
    elif y < 0: y, curd = 1, 1
    elif y >= M:y, curd = M-2, 3
    move(curd)
    B = board[x][y]
    
    q = deque()
    q.append([x, y])
    check = [[False]*M for _ in range(N)]
    check[x][y] = True
    C = 1
    while q:
        cx, cy = q.popleft()
        for dir in dirs:
            dx, dy = cx + dir[0], cy + dir[1]
            if 0 <= dx < N and 0 <= dy < M and B == board[dx][dy] and not check[dx][dy]:
                check[dx][dy] = True
                q.append([dx, dy])
                C += 1

    res += B*C

    if dice[5] > B:   curd = (curd + 1) % 4
    elif dice[5] < B: curd = (curd - 1) % 4

print(res)