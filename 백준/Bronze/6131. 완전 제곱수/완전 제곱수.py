import sys
input = sys.stdin.readline

N = int(input())
res = 0
for B in range(1, 500):
    for A in range(B, 501):
        if A*A == B*B+N:
            res += 1

print(res)