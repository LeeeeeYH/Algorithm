ls = list(map(int, __import__('sys').stdin.readline().split()))
print(*sorted(ls))