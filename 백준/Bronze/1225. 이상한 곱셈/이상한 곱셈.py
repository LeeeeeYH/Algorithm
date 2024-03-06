input = __import__('sys').stdin.readline

A, B = map(int, input().split())
summ = 0
while A:
    summ += A%10
    A //= 10

res = 0
while B:
    res += summ * (B%10)
    B //= 10
print(res)