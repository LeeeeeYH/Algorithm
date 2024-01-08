import sys
input = sys.stdin.readline

prime = [0]*2 + [1]*1000
for i in range(2, 33):
    if prime[i] == 1:
        for j in range(i+i, 1001, i):
            prime[j] = 0

N = int(input())
ls = list(map(int, input().split()))
print(sum([prime[i] for i in ls]))