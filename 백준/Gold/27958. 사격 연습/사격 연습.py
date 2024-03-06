input = __import__('sys').stdin.readline

dir = [[-1,0],[0,1],[1,0],[0,-1]]
N = int(input())
K = int(input())
board = [[[0]*N for _ in range(N)] for _ in range(K+1)]
board[0] = [list(map(int, input().split())) for _ in range(N)]
scores = [[[0]*N for _ in range(N)] for _ in range(K+1)]
scores[0] = [x[:] for x in board[0]]
bullets = [0] + list(map(int, input().split()))
res = 0

# 총 쏘기
def shot(k, line):
    score = 0
    for j in range(N):
        if board[k][line][j]:  # 표적 발견
            if board[k][line][j] >= 10:  # 보너스 표적이면
                score += board[k][line][j]
                board[k][line][j] = 0
            elif board[k][line][j] > bullets[k]:  # 표적을 부수지 못하면
                board[k][line][j] -= bullets[k]
            else:  # 총알이 더 쎄면
                score += scores[k][line][j]
                newhp = board[k][line][j] // 4
                board[k][line][j] = scores[k][line][j] = 0
                for d in dir:  # 상하좌우에 표적 생성
                    dx, dy = line+d[0], j+d[1]
                    if 0 <= dx < N and 0 <= dy < N and not board[k][dx][dy]:
                        board[k][dx][dy] = newhp
                        scores[k][dx][dy] = newhp
            break
    return score

def recur(k, score):
    if k == K+1:  # 총알을 다썼다면
        global res
        res = max(res, score)
        return

    for i in range(N):
        board[k] = [x[:] for x in board[k-1]]
        scores[k] = [x[:] for x in scores[k-1]]
        recur(k+1, score + shot(k, i))

recur(1, 0)
print(res)
