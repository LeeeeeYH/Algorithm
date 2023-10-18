import sys
input = sys.stdin.readline

k = int(input())
ls = list(map(str, input().split()))

maxres, minres = 0, 10**(k+1)

def recur(cur, num, check):
    if cur == k:
        global maxres, minres
        maxres = max(maxres, num)
        minres = min(minres, num)
        return

    last = num%10
    if ls[cur] == "<":
        for i in range(last+1, 10):
            if not check & 1<<i:
                recur(cur+1, num*10 + i, check | 1<<i)
    else:
        for i in range(last):
            if not check & 1<<i:
                recur(cur+1, num*10 + i, check | 1<<i)

for j in range(10):
    recur(0, j, 1<<j)

print(maxres)
if minres // (10**k) == 0:
    print(0, end="")
print(minres)