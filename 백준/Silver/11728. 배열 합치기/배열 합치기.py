import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i, j = 0, 0
while i<N and j<M:
    if A[i] < B[j]:
        print(A[i], end=" ")
        i += 1
    else:
        print(B[j], end=" ")
        j += 1

if i<N:
    print(*A[i:])
else:
    print(*B[j:])