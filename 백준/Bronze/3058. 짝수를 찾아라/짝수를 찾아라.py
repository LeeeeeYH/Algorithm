input = __import__('sys').stdin.readline

for _ in range(int(input())):
    ls = [i for i in list(map(int, input().split())) if i%2 == 0]
    print(sum(ls), min(ls))