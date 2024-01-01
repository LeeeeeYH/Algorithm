import math
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
x = -A + int(math.sqrt(A*A - B))
y = -A - int(math.sqrt(A*A - B))

if x == y:
    print(x)
else:
    print(y, x)