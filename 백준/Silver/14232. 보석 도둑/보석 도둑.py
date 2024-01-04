import sys
input = sys.stdin.readline

k = int(input())
limit = int(k**0.5)+1
ls = []

for i in range(2, int(k**0.5)+1):
    while k % i == 0:
        ls.append(i)
        k //= i

if k != 1:
    ls.append(k)

print(len(ls))
print(*ls)