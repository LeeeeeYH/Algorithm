import sys
input = sys.stdin.readline

k = int(input())

num = k
i = 2
M = int(k**0.5) + 1

jews = []
while i <= M:
    if num % i == 0:
        num //= i
        jews.append(i)
    else:
        i += 1
if num != 1:
    jews.append(num)
print(len(jews))
print(*jews)