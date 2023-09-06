import sys
input = sys.stdin.readline

dirs = [[-1,0],[0,1],[1,0],[0,-1],[-1,0],[0,1]] # 위 오 아 왼,위 오 # %안쓰려고 확장
N, M = map(int, input().split())
# ex: board[2] -> 2번 cctv까지 감시를 한 뒤의 사무실 상황
board = [[[6]*(M+2) for _ in range(N+2)] for _ in range(9)] # [cctv][i][j]
cctvs = [0] # 종류, 좌표
for i in range(1, N+1):
    line = list(map(int, input().split()))
    for j in range(1, M+1):
        if 1 <= line[j-1] <= 5: # cctv는
            cctvs.append([line[j-1],i,j])
    board[0][i][1:M+1] = line
leng = len(cctvs) # cctv개수
res = 64

# 사각지대 카운트
def count_blind_spot(board):
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if board[i][j] == 0:
                cnt += 1
    return cnt

# board1을 board2에 복사
def copy_board(board1, board2):
    for i in range(1, N+1):
        for j in range(1, M+1):
            board2[i][j] = board1[i][j]

# '#'채우기
def fill_hash(board, dir, x, y):
    while board[x][y] != 6:
        if board[x][y] == 0:
            board[x][y] = '#'
        x, y = x+dir[0], y+dir[1]

def recur(cur):
    if cur == leng:
        global res
        res = min(res, count_blind_spot(board[cur-1]))
        return

    if cctvs[cur][0] == 1: # 한쪽
        for i in range(4):
            copy_board(board[cur-1], board[cur])
            fill_hash(board[cur], dirs[i], cctvs[cur][1], cctvs[cur][2])
            recur(cur+1)
    elif cctvs[cur][0] == 2: # 양쪽
        for i in range(2):
            copy_board(board[cur-1], board[cur])
            fill_hash(board[cur], dirs[i], cctvs[cur][1], cctvs[cur][2])
            fill_hash(board[cur], dirs[i+2], cctvs[cur][1], cctvs[cur][2])
            recur(cur+1)
    elif cctvs[cur][0] == 3: # 직각
        for i in range(4):
            copy_board(board[cur-1], board[cur])
            fill_hash(board[cur], dirs[i], cctvs[cur][1], cctvs[cur][2])
            fill_hash(board[cur], dirs[i+1], cctvs[cur][1], cctvs[cur][2])
            recur(cur+1)
    elif cctvs[cur][0] == 4: # 3방향
        for i in range(4):
            copy_board(board[cur-1], board[cur])
            fill_hash(board[cur], dirs[i], cctvs[cur][1], cctvs[cur][2])
            fill_hash(board[cur], dirs[i+1], cctvs[cur][1], cctvs[cur][2])
            fill_hash(board[cur], dirs[i+2], cctvs[cur][1], cctvs[cur][2])
            recur(cur+1)
    elif cctvs[cur][0] == 5: # 4방향
        copy_board(board[cur-1], board[cur])
        fill_hash(board[cur], dirs[0], cctvs[cur][1], cctvs[cur][2])
        fill_hash(board[cur], dirs[1], cctvs[cur][1], cctvs[cur][2])
        fill_hash(board[cur], dirs[2], cctvs[cur][1], cctvs[cur][2])
        fill_hash(board[cur], dirs[3], cctvs[cur][1], cctvs[cur][2])
        recur(cur+1)

recur(1)
print(res)