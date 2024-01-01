import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
for i in range(K):
    if N > M*2:
        N -= 1
    else:
        M -= 1

if N >= M*2:
    print(M)
else:
    print(N//2)