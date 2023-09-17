import sys
input = sys.stdin.readline

a = sorted([int(input()) for _ in range(9)])
# 9C7 -> 9C2 == 전체합 - 100 인거찾기
hap = sum(a) - 100

i, j = 0, 8
while i < j:
    tmp = a[i] + a[j]
    if tmp < hap:
        i += 1
    elif tmp > hap:
        j -= 1
    else:
        break

print(*(a[:i] + a[i+1:j] + a[j+1:]), sep='\n')