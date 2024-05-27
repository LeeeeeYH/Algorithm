input = __import__('sys').stdin.readline

N, C = map(int, input().split())
see = [0]*(C+1)
for _ in range(N):
    T = int(input())
    num = T
    while num <= C:
        see[num] = 1
        num += T

print(sum(see))