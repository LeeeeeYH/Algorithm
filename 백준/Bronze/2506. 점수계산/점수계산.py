input = __import__('sys').stdin.readline

N = int(input())
ls = list(map(int, input().split()))
now, res = 0, 0
for i in ls:
    if i == 1:
        now += 1
        res += now
    else:
        now = 0
print(res)