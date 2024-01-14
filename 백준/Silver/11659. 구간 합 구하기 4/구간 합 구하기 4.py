import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ls = [0] + list(map(int, input().split()))
for i in range(1, N+1):
    ls[i] += ls[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(ls[j] - ls[i-1])