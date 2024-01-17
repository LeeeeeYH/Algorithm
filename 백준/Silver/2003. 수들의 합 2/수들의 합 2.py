import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ls = list(map(int, input().split())) + [0]

cnt = 0
i, j = 0, 1
summ = ls[0]

while True:
    if summ < M:
        if j < N:
            summ += ls[j]
            j += 1
        else:
            break
    else:
        if summ == M:
            cnt += 1
        summ -= ls[i]
        i += 1

print(cnt)