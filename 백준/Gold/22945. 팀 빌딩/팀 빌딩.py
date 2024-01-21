import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().split()))
i, j = 0, N-1
res = 0
while i < j:
    res = max(res, (j-i-1)*min(ls[i], ls[j]))

    if ls[i] < ls[j]:
        i += 1
    else:
        j -= 1
print(res)