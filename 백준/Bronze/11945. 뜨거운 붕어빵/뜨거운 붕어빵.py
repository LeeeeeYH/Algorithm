input = __import__('sys').stdin.readline

N, M = map(int, input().split())
for _ in range(N):
    print(str(input().rstrip())[::-1])