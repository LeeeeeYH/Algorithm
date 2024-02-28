input = __import__('sys').stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(M)]
dirs = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
clouds = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]
cloudmap = [[False]*N for _ in range(N)]

for d, s in moves:
    # 1
    for i in range(len(clouds)):
        clouds[i][0], clouds[i][1] = (clouds[i][0] + dirs[d][0]*s) % N, (clouds[i][1] + dirs[d][1]*s) % N
    for x, y in clouds:
        cloudmap[x][y] = True

    # 2
    for x, y in clouds:
        board[x][y] += 1

    # 3 -> 4번을 위해 나중에 진행
    # clouds = []

    # 4
    for x, y in clouds:
        for dir in dirs[2::2]:
            dx, dy = x+dir[0], y+dir[1]
            if 0 <= dx < N and 0 <= dy < N:
                if board[dx][dy]:
                    board[x][y] += 1

    # 3
    clouds = []

    # 5
    for i in range(N):
        for j in range(N):
            if cloudmap[i][j]:
                cloudmap[i][j] = False
            else:
                if board[i][j] >= 2:
                    clouds.append([i, j])
                    board[i][j] -= 2

print(sum([sum(line) for line in board]))