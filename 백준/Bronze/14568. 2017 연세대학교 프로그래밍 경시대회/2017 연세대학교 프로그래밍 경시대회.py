import sys
input = sys.stdin.readline

N = int(input())
res = 0

for i in range(2, N-3, 2):
    N -= 2
    res += N//2 - 1
print(res)