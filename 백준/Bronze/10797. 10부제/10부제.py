input = __import__('sys').stdin.readline

N = int(input())
ls = list(map(int, input().split()))
res = 0
for i in ls:
    if i%10 == N:
        res += 1
print(res)