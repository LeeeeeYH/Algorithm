import sys
input = sys.stdin.readline

prime = [False]*2 + [True]*4_000_000
for i in range(2, 2001):
    if prime[i]:
        for j in range(i*i, 4_000_001, i):
            prime[j] = False

ls = []
for i in range(2, 4_000_001):
    if prime[i]:
        ls.append(i)

N = int(input())
leng = len(ls)

i, summ = 0, 0
res = 0
for j in ls:
    summ += j
    while summ > N:
        summ -= ls[i]
        i += 1
    if summ == N:
        res += 1

print(res)