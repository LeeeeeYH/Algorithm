import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = [list(map(int, input().split())) + [0] for _ in range(N)]
min_A = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N-2, -1, -1):
        A[i][j] += A[i][j+1]

min_A[0] = A[0]
for i in range(1, N):
    for j in range(N-1, -1, -1):
        min_A[i][j] = min(min_A[i-1][j], A[i][j])

for _ in range(Q):
    Sx, Sy, L = map(int, input().split())
    Sx, Sy = Sx-1, Sy-1
    res = A[Sx][Sy]
    for i in range(Sy, N):
        res = min(res, A[Sx][Sy]-A[Sx][i] + min_A[Sx-L][i])
    print(res)