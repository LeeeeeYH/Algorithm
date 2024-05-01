input = __import__('sys').stdin.readline
res = sum(list(map(int, input().split())))
print(max(res, sum(list(map(int, input().split())))))