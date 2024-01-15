import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().split()))

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

lls, rls = [ls[0]]+[0]*(N-1), [0]*(N-1)+[ls[N-1]]
for i in range(1, N):
    lls[i], rls[N-i-1] = gcd(ls[i], lls[i-1]), gcd(ls[N-i-1], rls[N-i])

res, resK = -1, ""
if ls[0] % rls[1]:
    res, resK = rls[1], ls[0]
if ls[N-1] % lls[N-2] and res < lls[N-1]:
    res, resK = lls[N-1], ls[N-1]

for i in range(1, N-1):
    curgcd = gcd(lls[i - 1], rls[i + 1])
    if res < curgcd and ls[i] % curgcd:
        res, resK = curgcd, ls[i]

print(res, resK)