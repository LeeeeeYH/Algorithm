from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
check = [[False]*M for _ in range(N)]
q = deque()
found = False
for i in range(N):
    for j in range(M):
        if board[i][j] == '2':
            q.append([i, j, 0])
            check[i][j] = True
            found = True
            break
    if found:
        break

while q:
    x, y, dis = q.popleft()
    for d in dirs:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < N and 0 <= dy < M and not check[dx][dy] and board[dx][dy] != '1':
            check[dx][dy] = True
            if board[dx][dy] == '0':
                q.append([dx, dy, dis+1])
            else:
                print('TAK', dis+1, sep='\n')
                exit(0)

print('NIE')