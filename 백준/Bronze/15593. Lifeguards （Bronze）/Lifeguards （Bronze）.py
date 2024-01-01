import sys
input = sys.stdin.readline

times = [0 for _ in range(1001)]
N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
res = 0

for i in ls:
    for j in range(i[0], i[1]):
        if times[j] == 0:
            cnt += 1
        times[j] += 1

for i in ls:
    tmp = cnt
    for j in range(i[0], i[1]):
        if times[j] == 1:
            tmp -= 1
    res = max(res, tmp)

print(res)