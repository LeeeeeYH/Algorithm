input = __import__('sys').stdin.readline

for _ in range(int(input())):
    N = int(input())
    ls = list(map(int, input().split()))
    days = 1
    while N >= sum(ls):
        next = [0] * 6
        for i in range(6):
            next[i] = ls[i - 1] + ls[(i + 1) % 6] + ls[(i + 3) % 6]
        for i in range(6):
            ls[i] += next[i]
        days += 1
    print(days)