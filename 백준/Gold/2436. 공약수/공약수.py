import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

m, M = map(int, input().split())
gop = m*M
for i in range(int(gop**0.5), m-1, -1):
    if gop % i == 0 and gcd(i, gop//i) == m:
        print(i, gop//i)
        exit(0)