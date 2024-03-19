from collections import deque
input = __import__('sys').stdin.readline

dirs = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]
for _ in range(int(input())):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    board = [[False]*l for _ in range(l)]

    q = deque()
    q.append([sx, sy, 0])
    board[sx][sy] = True
    while q:
        x, y, cnt = q.popleft()
        if x == ex and y == ey:
            print(cnt)
            break

        for d in dirs:
            dx, dy = x+d[0], y+d[1]
            if 0<=dx<l and 0<=dy<l and not board[dx][dy]:
                board[dx][dy] = True
                q.append([dx, dy, cnt+1])