import sys
input = sys.stdin.readline

N, A = map(int, input().split())

num = A
res = 0
while num <= N:
    res += N//num
    num *= A

print(res)