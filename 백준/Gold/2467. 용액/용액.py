import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().split()))

i, j = 0, N-1
resi, resj, res = 0, N-1, 2_000_000_000
while i < j:
    summ = abs(ls[i]+ls[j])
    if res > summ:
        resi, resj, res = i, j, summ
    if abs(ls[i+1] + ls[j]) < abs(ls[i] + ls[j-1]):
        i += 1
    else:
        j -= 1

print(ls[resi], ls[resj])