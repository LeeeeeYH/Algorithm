input = __import__('sys').stdin.readline

A, B, C = map(int, input().split())
res = 0
while True:
    if A + 2 >= C:
        break
    if B + B < A + C:
        A, B = B, B + 1
    else:
        B, C = B - 1, B
    res += 1
print(res)