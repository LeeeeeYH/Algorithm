input = __import__('sys').stdin.readline

while True:
    s = input().rstrip()
    if s == '#':
        break
    s = s.upper()
    print(s.count('A') + s.count('E') + s.count('I') + s.count('O')+ s.count('U'))