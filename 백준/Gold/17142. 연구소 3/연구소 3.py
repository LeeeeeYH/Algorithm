from collections import deque
input = __import__('sys').stdin.readline

MAX = 2501
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
viruses = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            viruses.append((i, j, 0))

selected = [-1]*M
res = MAX
def recur(cur, start):
    if cur == M:
        bfs()
        return

    for i in range(start, len(viruses)):
        selected[cur] = i
        recur(cur+1, i+1)

def bfs():
    q = deque()
    check = [[False]*N for _ in range(N)]
    for i in selected:
        q.append(viruses[i])
        check[viruses[i][0]][viruses[i][1]] = True

    max_time = 0
    while q:
        x, y, time = q.popleft()

        dtime = time+1
        for d in dirs:
            dx, dy = x+d[0], y+d[1]
            if 0 <= dx < N and 0 <= dy < N and not check[dx][dy] and board[dx][dy] != 1:
                check[dx][dy] = True
                q.append((dx, dy, dtime))
                if board[dx][dy] == 0:
                    max_time = max(max_time, dtime)

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and not check[i][j]:
                return

    global res
    res = min(res, max_time)

recur(0, 0)
print(res if res != MAX else -1)