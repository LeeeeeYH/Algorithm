input = __import__('sys').stdin.readline

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    carry, res = 0, 0
    while a or b:
        if a%10 + b%10 + carry >= 10:
            carry = 1
            res += 1
        else:
            carry = 0

        a, b = a//10, b//10
    print(res)