import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
hap = []
i, j = 0, 0
while i < N and j < M:
    if A[i] < B[j]:
        hap.append(A[i])
        i += 1
    else:
        hap.append(B[j])
        j += 1

if i == N:
    hap += B[j:]
else:
    hap += A[i:]
print(*hap)