import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

i, j = 0, n-1
res = 0
while i < j:
    hap = a[i] + a[j]
    if hap < x:
        i += 1
    elif hap > x:
        j -= 1
    else:
        res += 1
        i, j = i+1, j-1

print(res)