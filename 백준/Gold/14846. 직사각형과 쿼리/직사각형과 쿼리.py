import sys
input = sys.stdin.readline

N = int(input())
board = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
pre = [[[0]*11 for _ in range(N+1)] for _ in range(N+1)]  # i, j까지 k가 몇개 있나
for i in range(1, N+1):
    for j in range(1, N+1):
        pre[i][j][board[i][j]] += 1
        for k in range(1, 11):
            pre[i][j][k] += pre[i-1][j][k] + pre[i][j-1][k] - pre[i-1][j-1][k]

Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    res = 0
    for k in range(1, 11):
        if pre[x2][y2][k] - pre[x1-1][y2][k] - pre[x2][y1-1][k] + pre[x1-1][y1-1][k]:
            res += 1
    print(res)