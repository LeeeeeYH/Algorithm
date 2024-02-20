import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

dir = [[0,1], [1,0]]
N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
dp = [[[-1]*4 for _ in range(501)] for _ in range(501)]
N = N-1

def recur(x, y, word):
    if x == N and y == N:
        return 0

    if dp[x][y][word] == -1:
        dp[x][y][word] = 0
        for d in dir:
            dx, dy = x + d[0], y + d[1]
            if dx > N or dy > N:
                continue
    
            if board[dx][dy] == 'M':
                dp[x][y][word] = max(dp[x][y][word], recur(dx, dy, 1))
            elif board[dx][dy] == 'O' and word == 1:
                dp[x][y][word] = max(dp[x][y][word], recur(dx, dy, 2))
            elif board[dx][dy] == 'L' and word == 2:
                dp[x][y][word] = max(dp[x][y][word], recur(dx, dy, 3))
            elif board[dx][dy] == 'A' and word == 3:
                dp[x][y][word] = max(dp[x][y][word], recur(dx, dy, 0) + 1)
            else:
                dp[x][y][word] = max(dp[x][y][word], recur(dx, dy, 0))
    return dp[x][y][word]

print(recur(0, 0, 0) if board[0][0] != 'M' else recur(0, 0, 1))