import sys
input = sys.stdin.readline

N = int(input())
board = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
pre_sum = [[[0]*11 for _ in range(N+1)] for _ in range(N+1)] # index의 번호가 존재하는 갯수

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, 11):
            pre_sum[i][j][k] = pre_sum[i-1][j][k] + pre_sum[i][j-1][k] - pre_sum[i-1][j-1][k]
        pre_sum[i][j][board[i][j]] += 1

Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    have_arr = [0]*11
    for k in range(1, 11):
        have_arr[k] = pre_sum[x2][y2][k] - pre_sum[x1-1][y2][k] - pre_sum[x2][y1-1][k] + pre_sum[x1-1][y1-1][k]

    res = 0
    for k in range(1, 11):
        if have_arr[k] > 0:
            res += 1
    print(res)