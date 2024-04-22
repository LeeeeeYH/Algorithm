input = __import__('sys').stdin.readline

N, K = map(int, input().split())
num, i = 1, 0
while num <= N:
    if N % num == 0:
        i += 1
        if i == K:
            print(num)
            break
    num += 1
else:
    print(0)