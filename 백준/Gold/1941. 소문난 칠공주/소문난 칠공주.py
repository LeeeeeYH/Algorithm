import sys
input = sys.stdin.readline

dir = [[-1,0],[0,1],[1,0],[0,-1]]
ls = []
for _ in range(5):
    ls += list(input().rstrip())
selected = [-1]*7
res = 0

def check():
    board = [[False]*5 for _ in range(5)]
    for i in range(1, 7):
        board[selected[i]//5][selected[i]%5] = True

    x, y = selected[0]//5, selected[0]%5
    q = [[x, y]]
    while q:
        x, y = q.pop(0)

        for d in dir:
            dx, dy = x+d[0], y+d[1]
            if 0<=dx<5 and 0<=dy<5 and board[dx][dy]:
                board[dx][dy] = False
                q.append([dx, dy])

    for i in range(1, 7):
        x, y = selected[i]//5, selected[i]%5
        if board[x][y]:
            return False
    return True

def combi(cur, start, count):
    if cur == 7:
        if count >= 4:
            if check():
                global res
                res += 1
        return

    for i in range(start, 25):
        selected[cur] = i
        if ls[i] == 'S':
            combi(cur+1, i+1, count+1)
        else:
            combi(cur+1, i+1, count)

combi(0, 0, 0)
print(res)