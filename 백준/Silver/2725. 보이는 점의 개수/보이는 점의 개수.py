import sys
input = sys.stdin.readline

dots = [[1]*1001 for _ in range(1001)]
for i in range(2, 1001):
    for j in range(1, i):
        if dots[i][j]:
            k = 2
            while i*k <= 1000:
                dots[i*k][j*k] = 0
                k += 1

C = int(input())
for _ in range(C):
    N = int(input())
    cnt = 0
    for i in range(2, N+1):
        for j in range(1, i):
            cnt += dots[i][j]

    print(cnt*2 + 3)