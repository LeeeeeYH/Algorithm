while True:
    s = input().rstrip()
    if s == 'END':
        break
    print(s[::-1])