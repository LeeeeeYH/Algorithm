import sys
input = sys.stdin.readline

N, H = map(int, input().split())
imos = [0] * H  # index 0 부터 비교했을때 이전 index보다 장애물이 몇개나 많아지거나 적어졌는가

for _ in range(N//2):
    imos[H - int(input())] += 1
    imos[int(input())] -= 1

summ = N//2
res, resnum = summ, 1
for i in range(1, H):
    summ += imos[i]
    if res > summ:
        res = summ
        resnum = 1
    elif res == summ:
        resnum += 1

print(res, resnum)