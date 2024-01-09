import sys
input = sys.stdin.readline

max_num = 1299709
prime = [False]*2 + [True]*max_num

for i in range(2, int(max_num**0.5)+1):
    if prime[i]:
        for j in range(i*i, max_num+1, i):
            prime[j] = False

T = int(input())
for _ in range(T):
    k = int(input())
    l, r = k, k
    while not prime[l]:
        l -= 1
    while not prime[r]:
        r += 1
    print(r-l)