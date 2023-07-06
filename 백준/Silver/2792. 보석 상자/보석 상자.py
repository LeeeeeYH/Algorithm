import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jews = [int(input()) for _ in range(M)]

i, j = 1, 10**9
res = j

while i <= j:
    mid = (i+j)//2
    total = 0
    for jew in jews:
        total += (jew-1)//mid + 1
    if total <= N:
        j = mid - 1
        res = mid
    else:
        i = mid + 1

print(res)