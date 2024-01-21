import sys
input = sys.stdin.readline

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
# 4000*4000*4000 == 64,000,000,000 안됨
# 4000*4000*2 == 32,000,000 12초니까 될듯
res = 0

have = dict()
for i in range(n):
    for j in range(n):
        hap = ls[i][0] + ls[j][1]
        if have.get(hap) is None:
            have[hap] = 1
        else:
            have[hap] += 1
for i in range(n):
    for j in range(n):
        hap = -(ls[i][2] + ls[j][3])
        if have.get(hap) is not None:
            res += have[hap]

print(res)