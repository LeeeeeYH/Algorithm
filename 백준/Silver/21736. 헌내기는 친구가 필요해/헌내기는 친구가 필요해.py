import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [['X']*(M+2)] + [['X'] + list(input().rstrip()) + ['X'] for _ in range(N)] + [['X']*(M+2)]
dir = [[1,0],[0,1],[-1,0],[0,-1]]

q, res = [], 0
flag = False
for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j] == 'I':
            board[i][j] = 'X'
            q.append([i, j])
            flag = True
            break
    if flag: break

while q:
    x, y = q.pop(0)

    for d in dir:
        nx, ny = x+d[0], y+d[1]
        if board[nx][ny] == 'O':
            board[nx][ny] = 'X'
            q.append([nx, ny])
        elif board[nx][ny] == 'P':
            board[nx][ny] = 'X'
            q.append([nx, ny])
            res += 1

print(res if res > 0 else 'TT')