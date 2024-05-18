input = __import__('sys').stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    s = s[0].upper() + s[1:]
    print(s)