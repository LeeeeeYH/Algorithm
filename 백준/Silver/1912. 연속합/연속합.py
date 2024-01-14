import sys
input = sys.stdin.readline

n = int(input())
ls = [0] + list(map(int, input().split()))
mini, summ = 0, 0
res = -100000*1000
for i in ls[1:]:
    summ += i
    res = max(res, summ - mini)
    mini = min(mini, summ)

print(res)