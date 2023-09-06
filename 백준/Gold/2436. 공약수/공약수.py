import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def gcd(a, b):
    while a%b:
        a, b = b, a%b
    return b


multi = A*B
x = A
res_a, res_b = 0, 0
while True:
    if x > multi/x:
        break

    if multi % x == 0:
        y = multi // x
        if gcd(x, y) == A:
            res_a, res_b = x, y
    x += 1

print(res_a, res_b)