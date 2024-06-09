input = __import__('sys').stdin.readline

N = int(input())
cnt = 0
for i in range(1, N+1):
    print(i, end=' ')
    cnt += 1
    if cnt == 6 or i == N:
        print("Go!", end=' ')
        cnt = 0