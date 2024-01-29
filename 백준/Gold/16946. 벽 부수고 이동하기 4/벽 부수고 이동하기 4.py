import sys
input = sys.stdin.readline

dir = [[0,-1],[1,0],[0,1],[-1,0]]
N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
check = [[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and not check[i][j]:
            q = [[i,j]]
            check[i][j] = True
            change = set()  # 넓이 구하고 바꿔줄 좌표들
            cnt = 1  # 넓이

            # 0의 넓이를 구하고 인접한 벽들 리스트를 구함
            while q:
                x, y = q.pop(0)

                for d in dir:
                    dx, dy = x+d[0], y+d[1]
                    if 0 <= dx < N and 0 <= dy < M:
                        if board[dx][dy] == 0 and not check[dx][dy]:
                            check[dx][dy] = True
                            q.append([dx, dy])
                            cnt += 1
                        elif board[dx][dy]:
                            change.add((dx, dy))
            for cx, cy in change:
                board[cx][cy] += cnt

for i in range(N):
    for j in range(M):
        print(board[i][j]%10, end="")
    print()