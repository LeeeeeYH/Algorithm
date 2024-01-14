import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sumA, sumB = 0, 0
dictA = dict()
dictA[0] = 1
res = 0
for i in range(N):
    sumA += A[i]
    sumB += B[i]
    diff = sumA - sumB
    if diff in dictA:
        res += dictA[diff]
        dictA[diff] += 1
    else:
        dictA[diff] = 1

print(res)