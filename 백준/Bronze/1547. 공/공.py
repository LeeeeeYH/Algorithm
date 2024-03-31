input = __import__('sys').stdin.readline

M = int(input())
res = 1
for _ in range(M):
    X, Y = map(int, input().split())
    if res == X:
        res = Y
    elif res == Y:
        res = X
print(res)