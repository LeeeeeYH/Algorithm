import sys
input = sys.stdin.readline

N = int(input())
ls = [0] + list(map(int, input().split()))
res = [-1]*(N+1)

bf, bfidx = ls[-1], -1
for i in range(N-1, -1, -1):
    cur = ls[i]
    if bf != cur:
        bf, bfidx = cur, i+1
    res[i] = bfidx
print(*res[1:])