import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = [list(map(int, input().split())) + [0] for _ in range(N)]  # 오른쪽까지 가기위한 누적합
min_A = [[0]*N for _ in range(N)]  # 이보다 위의 좌표에 대해 오른쪽까지 가기 위한 누적값의 최솟값
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
    res = A[Sx][Sy]  # 점프없이 가기
    for i in range(Sy, N):  # i번째에서 점프하기
        res = min(res, A[Sx][Sy]-A[Sx][i] + min_A[Sx-L][i])
    print(res)