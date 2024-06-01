input = __import__('sys').stdin.readline

N = int(input())
ls = list(map(int, input().split()))
c = int(input())

res = 0
for i in ls:
    res += ((i-1)//c+1) * c
print(res)