import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

N = int(input())
for _ in range(N):
    ls = list(map(int, input().split()))
    leng = len(ls)
    res = 0
    for i in range(leng-1):
        for j in range(i+1, leng):
            res = max(res, gcd(ls[i], ls[j]))
    print(res)