import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[0]*(M+1)] + [[0]+[int(i) for i in input().rstrip()] for _ in range(N)]
pre_sum = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j] == 0:
            pre_sum[i][j] = pre_sum[i-1][j] + 1

res = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if pre_sum[i][j] != 0:
            min_len = 333
            for k in range(j, 0, -1):
                min_len = min(min_len, pre_sum[i][k])
                res = max(res, (j-k+1) * min_len)

print(res)