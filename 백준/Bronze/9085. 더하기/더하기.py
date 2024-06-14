input = __import__('sys').stdin.readline

for _ in range(int(input())):
    N = int(input())
    print(sum(list(map(int, input().split()))))