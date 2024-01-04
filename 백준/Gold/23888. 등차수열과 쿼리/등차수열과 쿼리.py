import sys
input = sys.stdin.readline

def an(n):
    return a + (n-1)*d

def s(n):
    return (2*a + (n-1)*d)*n//2

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

a, d = map(int, input().split())
q = int(input())
for _ in range(q):
    typ, l, r = map(int, input().split())
    if typ == 1:
        print(s(r) - s(l-1))
    else:
        if l == r:
            print(an(l))
        else:
            print(gcd(a, d))