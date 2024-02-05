import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().split()))

prime = [False]*2 + [True]*1_000_000
numbers = [-1] * 1_000_001
for i, x in enumerate(ls):
    numbers[x] = i
res = [0]*N


for num in ls:
    for j in range(num+num, 1_000_001, num):
        if numbers[j] != -1:
            res[numbers[j]] -= 1
            res[numbers[num]] += 1

print(*res)
