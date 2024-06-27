input = __import__('sys').stdin.readline

N = int(input())
for i in range(1, N + 1):
    print(i, ". ", input(), sep='', end='')