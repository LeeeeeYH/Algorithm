import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().split()))

i, j = 0, N-1
res = abs(ls[i] + ls[j])
resi, resj = 0, N-1
while i < j:
    if res > abs(ls[i] + ls[j]):
        res = abs(ls[i] + ls[j])
        resi, resj = i, j

    if abs(ls[i+1] + ls[j]) < abs(ls[i] + ls[j-1]):
        i += 1
    else:
        j -= 1

print(f'{ls[resi]} {ls[resj]}')