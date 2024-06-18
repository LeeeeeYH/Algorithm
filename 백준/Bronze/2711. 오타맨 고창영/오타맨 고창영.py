input = __import__('sys').stdin.readline

for _ in range(int(input())):
    i, s = input().split()
    i = int(i)-1
    print(s[:i]+s[i+1:])