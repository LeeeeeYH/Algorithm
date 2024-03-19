from collections import deque
input = __import__('sys').stdin.readline

MAX = 1_000_001
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
check = [[[False]*2 for _ in range(M)] for _ in range(N)]
N, M = N-1, M-1

q = deque()
q.append([0, 0, 0, 1])
check[0][0][0] = True
res = []
while q:
    x, y, broken, cnt = q.popleft()
    if x == N and y == M:
        res.append(cnt)

    for d in dirs:
        dx, dy = x+d[0], y+d[1]
        if 0<=dx<=N and 0<=dy<=M:
            if board[dx][dy] == 0 and not check[dx][dy][broken]:
                check[dx][dy][broken] = True
                q.append([dx, dy, broken, cnt+1])
            if board[dx][dy] == 1 and broken == 0 and not check[dx][dy][1]:
                check[dx][dy][1] = True
                q.append([dx, dy, 1, cnt+1])

if res:
    print(min(res))
else:
    print(-1)