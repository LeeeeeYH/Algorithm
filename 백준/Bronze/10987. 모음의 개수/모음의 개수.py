input = __import__('sys').stdin.readline

s = input().rstrip()
res = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        res += 1
print(res)