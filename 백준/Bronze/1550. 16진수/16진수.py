input = __import__('sys').stdin.readline

s = input().rstrip()
i = 1
res = 0
for num in s[::-1]:
    if num.isdigit():
        res += int(num) * i
    else:
        res += (ord(num)-55) * i
    i *= 16
print(res)