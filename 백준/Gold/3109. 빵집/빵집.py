input = __import__('sys').stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
res = 0

def dfs(r, c):
    global res, find
    if c == C-1:
        res += 1
        find = True
        return

    for i in [-1, 0, 1]:
        dr, dc = r+i, c+1
        if 0 <= dr < R and board[dr][dc] == '.':
            board[dr][dc] = 'x'
            dfs(dr, dc)
            if find:
                break

for i in range(R):
    find = False
    dfs(i, 0)
print(res)